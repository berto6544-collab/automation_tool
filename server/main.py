from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import os


# CONFIG
SCRIPTS_DIR = "./recorded_scripts"  # Keep outside FastAPI watched folder

ALLOWED_ORIGINS = [
    "chrome-extension://amojbadkapkcjifkcociofbjkafmeboi",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "*"
]

os.makedirs(SCRIPTS_DIR, exist_ok=True)


# FASTAPI INIT
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# UTILITIES
def launch_playwright_codegen(script_name: str, url: str):
    """
    Launch Playwright Codegen interactively in Chrome.
    Saves actions to a Python file. Non-blocking.
    """
    path = os.path.join(SCRIPTS_DIR, f"{script_name}.py")
    subprocess.Popen(
        f'python -m playwright codegen --channel=chrome --output "{path}" {url}',
        shell=True
    )
    return path

def run_script_file(script_name: str):
    """
    Run an existing Python script asynchronously.
    """
    path = os.path.join(SCRIPTS_DIR, f"{script_name}.py")
    if os.path.exists(path):
        subprocess.Popen(f'python "{path}"', shell=True)
        return True
    return False

# API ENDPOINTS
@app.get("/")
def root():
    return {"status": "Playwright Script Server Running"}

@app.get("/scripts")
def list_scripts():
    try:
        files = os.listdir(SCRIPTS_DIR)
        scripts = [f.replace(".py", "") for f in files if f.endswith(".py")]

        return {"scripts": scripts}
    except Exception as e:
        return {"error": str(e)}

@app.post("/run/{script_name}")
async def run_script(script_name: str, request: Request):
    """
    Run script or launch Codegen interactively if script does not exist.
    Expects JSON: { "url": "https://example.com" }
    """
    try:
        data = await request.json()
        url = data.get("url")
        if not url:
            return {"error": "Missing URL parameter"}

        path = os.path.join(SCRIPTS_DIR, f"{script_name}.py")
        created = False

        if not os.path.exists(path):
            launch_playwright_codegen(script_name, url)
            created = True
            return {
                "status": "Codegen launched. Record actions in Chrome.",
                "script": script_name,
                "created": created,
                "url": url
            }

        run_script_file(script_name)
        return {"status": "Script launched", "script": script_name}

    except Exception as e:
        return {"error": str(e)}

@app.post("/create/{script_name}")
async def create_script(script_name: str, request: Request):
    """
    Only create script interactively using Codegen.
    """
    try:
        data = await request.json()
        url = data.get("url")
        if not url:
            return {"error": "Missing URL parameter"}

        path = os.path.join(SCRIPTS_DIR, f"{script_name}.py")
        if os.path.exists(path):
            return {"status": "already exists", "script": script_name}

        launch_playwright_codegen(script_name, url)
        return {
            "status": "Codegen launched interactively.",
            "script": script_name,
            "url": url
        }

    except Exception as e:
        return {"error": str(e)}

@app.delete("/delete/{script_name}")
def delete_script(script_name: str):
    try:
        path = os.path.join(SCRIPTS_DIR, f"{script_name}.py")
        if os.path.exists(path):
            os.remove(path)
            return {"status": "deleted", "script": script_name}
        return {"error": "Script not found"}
    except Exception as e:
        return {"error": str(e)}
