# Playwright Runner Chrome Extension

The **Playwright Runner Chrome Extension** is a lightweight popup interface that connects to a **Python backend server** to manage and execute browser automation scripts with **Playwright**. It also allows launching **Playwright Codegen** sessions directly from your browser.

---

## Features

1. **Server Configuration**
   - Enter and save the Python server URL.
   - Automatically loads available scripts from the server on popup open.

2. **Script Selection**
   - Choose a predefined script from a dropdown.
   - Optionally write a custom script name.
   - The input field is dynamically enabled for custom scripts.

3. **Run Scripts**
   - Runs the selected or custom script.
   - Optionally sends a URL to the server for browser automation.
   - Launches Playwright Codegen sessions for recording automated flows.

4. **Refresh Scripts**
   - Reloads the script list from the server without reopening the popup.

5. **Delete Scripts**
   - Delete predefined scripts from the server directly from the extension.
   - Confirmation prompt prevents accidental deletion.

6. **Status Feedback**
   - Real-time status updates in the popup for loading, running, errors, and completion.

7. **Documentation Link**
   - Quick access to [Playwright Codegen docs](https://playwright.dev/docs/cli#codegen).

---

## How It Works

1. The extension fetches scripts from the Python server when opened.
2. Users select a script or enter a custom script name.
3. The extension sends a `POST` request to the server to run the script or launch Codegen.
4. The server executes the script and returns a status message.
5. Users can delete scripts from the server without leaving the extension popup.

---

## Installation

1. Open Chrome and navigate to `chrome://extensions/`.
2. Enable **Developer Mode** in the top-right corner.
3. Click **Load unpacked** and select the extension folder containing:
   - `popup.html`
   - `popup.js`
   - Any other assets like icons or CSS.
4. Pin the extension to your toolbar for easy access.

---

## Usage

1. Click the extension icon to open the popup.
2. Enter your Python server URL (e.g., `http://127.0.0.1:8000`).
3. Select a script from the dropdown or choose **Write custom script...**.
4. Enter a URL for Codegen or scripts that require it.
5. Click **Run** to execute the script.
6. Use **Refresh Scripts** to reload the list of available scripts.
7. Use **Delete Selected Script** to remove a predefined script from the server.

---

## Recommended Improvements

- Add authentication for multi-user environments.
- Show inline delete buttons next to each script for faster management.
- Add tooltips or descriptions for each script.
- Log script execution results in the extension for easier debugging.

---

## License

This extension is open source under the [MIT License](LICENSE).
