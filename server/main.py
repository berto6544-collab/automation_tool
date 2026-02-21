from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import os
import threading
import time

from openai import OpenAI


load_dotenv()
# =============================
# CONFIG
# =============================
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))  # Replace with your OpenAI API key

SCRIPTS_DIR = "./recorded_scripts"

ALLOWED_ORIGINS = [
    "chrome-extension://amojbadkapkcjifkcociofbjkafmeboi",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "*"
]

os.makedirs(SCRIPTS_DIR, exist_ok=True)

# =============================
# FASTAPI INIT
# =============================
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================
# AI DOCUMENTATION FUNCTION
# =============================
def generate_ai_documentation(script_name: str):
    script_path = os.path.join(SCRIPTS_DIR, f"{script_name}.py")
    doc_path = os.path.join(SCRIPTS_DIR, f"{script_name}_DOC.md")

    if not os.path.exists(script_path):
        return False

    with open(script_path, "r", encoding="utf-8") as f:
        script_content = f.read()

    prompt = f"""
You are a senior QA Automation Engineer and technical documentation expert.

Analyze this Playwright Python script and create EXTREMELY CLEAR documentation.

Write it for someone with basic programming knowledge.

Include the following sections:

# Overview
Explain in simple terms what the automation does.

# What the script does
Describe the full workflow from start to finish.

# Step-by-step explanation
Break down EVERY action in order.
For EACH step include:
• What the script is doing  
• What element it interacts with  
• What text is being entered (if any)  
• WHY that text is being entered  
• What the expected result is  

# Text Inputs Explained
List ALL typed text values and explain:
• Where the text is entered
• What the text represents
• Why it is needed

# Selectors used
List all selectors and explain what element each selector targets.

# How to run the script
Include exact command:
python {script_name}.py

# Improvements
Suggest real professional improvements such as:
• Better selectors
• Error handling
• Wait conditions
• Security improvements

SCRIPT:

{script_content}
"""

    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )

    documentation = response.output_text

    with open(doc_path, "w", encoding="utf-8") as f:
        f.write(documentation)

    print(f"Documentation created: {doc_path}")
    return True

# =============================
# PLAYWRIGHT FUNCTIONS
# =============================
def launch_playwright_codegen(script_name: str, url: str):
    path = os.path.join(SCRIPTS_DIR, f"{script_name}.py")
    print(f"Launching Playwright codegen for {script_name} at {url}...")

    # Launch Playwright codegen
    proc = subprocess.Popen(
        f'python -m playwright codegen --channel=chrome --output "{path}" {url}',
        shell=True
    )

    # Wait for the browser/codegen to finish and generate documentation
    def wait_and_document():
        print(f"Waiting for Playwright session to finish for {script_name}...")
        proc.wait()  # Blocks until user closes the browser
        print(f"Playwright finished for {script_name}, generating documentation...")
        generate_ai_documentation(script_name)

    threading.Thread(target=wait_and_document, daemon=True).start()
    return path

def run_script_file(script_name: str):
    path = os.path.join(SCRIPTS_DIR, f"{script_name}.py")

    if os.path.exists(path):
        subprocess.Popen(f'python "{path}"', shell=True)
        # Generate documentation after running (optional, can skip if you only want codegen docs)
        generate_ai_documentation(script_name)
        return True
    return False

# =============================
# API ENDPOINTS
# =============================
@app.get("/")
def root():
    return {"status": "Playwright Script Server Running with AI"}

@app.get("/scripts")
def list_scripts():
    files = os.listdir(SCRIPTS_DIR)
    scripts = [f.replace(".py", "") for f in files if f.endswith(".py")]
    return {"scripts": scripts}

@app.post("/run/{script_name}")
async def run_script(script_name: str, request: Request):
    try:
        data = await request.json()
        url = data.get("url")
        if not url:
            return {"error": "Missing URL parameter"}

        path = os.path.join(SCRIPTS_DIR, f"{script_name}.py")

        if not os.path.exists(path):
            launch_playwright_codegen(script_name, url)
            return {
                "status": "Codegen launched. Documentation will auto generate after browser closes.",
                "script": script_name
            }

        run_script_file(script_name)
        return {"status": "Script launched and documented", "script": script_name}
    except Exception as e:
        return {"error": str(e)}

@app.post("/create/{script_name}")
async def create_script(script_name: str, request: Request):
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
            "status": "Codegen launched. Documentation will auto generate after browser closes.",
            "script": script_name
        }
    except Exception as e:
        return {"error": str(e)}

@app.post("/document/{script_name}")
def document_script(script_name: str):
    success = generate_ai_documentation(script_name)
    if success:
        return {"status": "Documentation created", "script": script_name}
    return {"error": "Script not found"}

@app.delete("/delete/{script_name}")
def delete_script(script_name: str):
    path = os.path.join(SCRIPTS_DIR, f"{script_name}.py")
    if os.path.exists(path):
        os.remove(path)
        doc_path = os.path.join(SCRIPTS_DIR, f"{script_name}_DOC.md")
        if os.path.exists(doc_path):
            os.remove(doc_path)
        return {"status": "deleted", "script": script_name}
    return {"error": "Script not found"}