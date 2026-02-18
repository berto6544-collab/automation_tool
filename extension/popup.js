const select = document.getElementById("scripts");
const customScriptInput = document.getElementById("customScript");
const serverInput = document.getElementById("server");
const urlInput = document.getElementById("url");
const runButton = document.getElementById("run");
const refreshButton = document.getElementById("refresh");
const deleteButton = document.getElementById("deleteScript");
const statusBox = document.getElementById("status");

// Load server from Chrome storage
chrome.storage.local.get(["server"], (result) => {
    if (result.server) {
        serverInput.value = result.server;
        loadScripts(result.server);
    }
});

// Save server URL on change
serverInput.addEventListener("change", () => {
    const server = serverInput.value.trim();
    if (!server) return;
    chrome.storage.local.set({ server }, () => loadScripts(server));
});

// Enable/disable custom script input and show/hide delete button
select.addEventListener("change", () => {
    if (select.value === "__custom__") {
        customScriptInput.disabled = false;
        customScriptInput.focus();
        deleteButton.style.display = "none"; // hide delete for custom
    } else if (select.value) {
        customScriptInput.value = "";
        customScriptInput.disabled = true;
        deleteButton.style.display = "block"; // show delete for predefined scripts
    } else {
        deleteButton.style.display = "none";
    }
});

// Load scripts from server
async function loadScripts(server) {
    if (!server) return;

    try {
        const res = await fetch(`${server}/scripts`);
        const data = await res.json();
        const scripts = data.scripts || [];

        // Clear existing options
        select.innerHTML = "";
        select.innerHTML += `<option disabled selected>Select script</option>`;

        // Add fetched scripts
        scripts.forEach(name => {
            const option = document.createElement("option");
            option.value = name;
            option.text = name;
            select.appendChild(option);
        });

        // Add custom script option
        select.innerHTML += `<option value="__custom__">Write custom script...</option>`;

        runButton.disabled = false;
        statusBox.textContent = "Scripts loaded ✅";
    } catch (err) {
        console.error(err);
        select.innerHTML = `<option disabled>Failed to load scripts</option>`;
        runButton.disabled = true;
        statusBox.textContent = "Failed to load scripts ❌";
    }
}

// Run script or Codegen
runButton.onclick = async () => {
    let script = select.value;
    const server = serverInput.value.trim();
    const url = urlInput.value.trim();

    if (!server) {
        statusBox.textContent = "Enter server URL ❌";
        return;
    }

    if (script === "__custom__") {
        script = customScriptInput.value.trim();
        if (!script) {
            statusBox.textContent = "Enter custom script name ❌";
            return;
        }
    }

    if (script === "codegen") {
        if (!url) {
            statusBox.textContent = "Enter URL for Codegen ❌";
            return;
        }

        try {
            statusBox.textContent = "Launching Playwright Codegen...";
            const res = await fetch(`${server}/run/codegen`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ url })
            });
            const data = await res.json();
            statusBox.textContent = data.error
                ? `Error: ${data.error} ❌`
                : "Playwright Codegen launched ✅";
        } catch (err) {
            console.error(err);
            statusBox.textContent = "Failed to launch Codegen ❌";
        }
        return;
    }

    try {
        statusBox.textContent = "Running script...";
        const res = await fetch(`${server}/run/${script}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url })
        });
        const data = await res.json();
        statusBox.textContent = data.error
            ? `Error: ${data.error} ❌`
            : `Script "${script}" completed ✅`;
    } catch (err) {
        console.error(err);
        statusBox.textContent = "Failed to run script ❌";
    }
};

// Refresh scripts
refreshButton.onclick = async () => {
    const server = serverInput.value.trim();
    if (!server) return;
    statusBox.textContent = "Refreshing scripts...";
    await loadScripts(server);
};

// Delete script
deleteButton.addEventListener("click", async () => {
    const server = serverInput.value.trim();
    const script = select.value;

    if (!script || script === "__custom__") return;

    if (!confirm(`Are you sure you want to delete "${script}"?`)) return;

    try {
        const res = await fetch(`${server}/delete/${script}`, { method: "DELETE" });
        const data = await res.json();

        if (data.error) {
            statusBox.textContent = `Error deleting script: ${data.error} ❌`;
        } else {
            statusBox.textContent = `Script "${script}" deleted ✅`;
            await loadScripts(server);
        }
    } catch (err) {
        console.error(err);
        statusBox.textContent = "Failed to delete script ❌";
    }
});
