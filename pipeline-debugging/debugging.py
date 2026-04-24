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
return "Unknown Issue"

def analyze_pipelines():
    summary = defaultdict(int)

    for repo in REPOS:
        print(f"Repository: {repo}")
        runs = get_workflow_runs(repo)

        for run in runs[:5]:
            if run.get("conclusion") != "failure":
                continue

            print(f"Run: {run.get('name')} | ID: {run.get('id')}")
            jobs = get_jobs(repo, run.get("id"))

            for job in jobs:
                if job.get("conclusion") == "failure":
                    log_reference = job.get("html_url", "")
                    error_type = classify_error(log_reference)

                    print(f"Job: {job.get('name')}")
                    print(f"Issue: {error_type}")
                    print(f"Logs: {log_reference}")

                    summary[error_type] += 1

    return summary

def print_summary(summary):
    print("Summary")
    for issue, count in summary.items():
        print(f"{issue}: {count}")

if __name__ == "__main__":
    result = analyze_pipelines()
    print_summary(result)
