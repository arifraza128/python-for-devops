import requests
import re
from collections import defaultdict

GITHUB_TOKEN = "your_token_here"

REPOS = [
    "owner1/repo1",
    "owner2/repo2"
]

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

ERROR_PATTERNS = {
    "Dependency Issue": r"(ModuleNotFoundError|No module named)",
    "Permission Issue": r"(Permission denied)",
    "Memory Issue": r"(Out of memory|Killed)",
    "Syntax Error": r"(SyntaxError|IndentationError)",
    "Build Failure": r"(build failed|Compilation failed)"
}

def get_workflow_runs(repo):
    url = f"https://api.github.com/repos/{repo}/actions/runs"
    response = requests.get(url, headers=HEADERS)
    return response.json().get("workflow_runs", [])

def get_jobs(repo, run_id):
    url = f"https://api.github.com/repos/{repo}/actions/runs/{run_id}/jobs"
    response = requests.get(url, headers=HEADERS)
    return response.json().get("jobs", [])

def classify_error(text):
    for category, pattern in ERROR_PATTERNS.items():
        if re.search(pattern, text, re.IGNORECASE):
            return category
