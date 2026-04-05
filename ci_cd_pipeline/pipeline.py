import os
import subprocess
import sys

# CONFIG
REPO_URL = "https://github.com/your-username/your-repo.git"
PROJECT_DIR = "project"

def run_command(command):
    print(f"\nRunning: {command}")
    result = subprocess.run(command, shell=True)
    
    if result.returncode != 0:
        print(" Command failed!")
        sys.exit(1)
    else:
        print(" Success")

# 1. Pull Code
def pull_code():
    if not os.path.exists(PROJECT_DIR):
        run_command(f"git clone {REPO_URL} {PROJECT_DIR}")
    else:
        os.chdir(PROJECT_DIR)
        run_command("git pull")
        os.chdir("..")

# 2. Install Dependencies
def install_dependencies():
    os.chdir(PROJECT_DIR)
    if os.path.exists("requirements.txt"):
        run_command("pip install -r requirements.txt")
    os.chdir("..")

# 3. Run Tests
def run_tests():
    os.chdir(PROJECT_DIR)
    if os.path.exists("tests"):
        run_command("python -m unittest discover tests")
    else:
        print(" No tests found")
    os.chdir("..")

# 4. Build (Docker)
def build():
    os.chdir(PROJECT_DIR)
    if os.path.exists("Dockerfile"):
        run_command("docker build -t myapp .")
    else:
        print(" No Dockerfile found, skipping build")
    os.chdir("..")

# 5. Deploy (Dummy)
def deploy():
    print("\n Deploying application...")
    print(" App deployed successfully (simulated)")

# MAIN PIPELINE
def main():
    print("⚙️ Starting CI/CD Pipeline...\n")

    pull_code()
    install_dependencies()
    run_tests()
    build()
    deploy()

    print("\n🎉 Pipeline completed successfully!")

if __name__ == "__main__":
    main()
