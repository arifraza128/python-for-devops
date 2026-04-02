import subprocess
import os

repo_url = "https://github.com/username/repo.git"
project_dir = "/path/to/project"
image_name = "username/myapp:latest"
docker_username = "username"
docker_password = "your_password"
k8s_deployment_file = "deployment.yaml"

def run_cmd(cmd_list):
    subprocess.run(cmd_list, check=True)

# Step 1: Pull or clone repo
if not os.path.exists(project_dir):
    print("Cloning repository...")
    run_cmd(["git", "clone", repo_url, project_dir])
else:
    print("Pulling latest changes...")
    run_cmd(["git", "-C", project_dir, "pull"])

# Step 2: Build Docker image
print("Building Docker image...")
run_cmd(["docker", "build", "-t", image_name, project_dir])

# Step 3: Login to Docker Hub
print("Logging in to Docker Hub...")
run_cmd(["docker", "login", "-u", docker_username, "-p", docker_password])

# Step 4: Push Docker image
print("Pushing Docker image to Docker Hub...")
run_cmd(["docker", "push", image_name])

# Step 5: Deploy to Kubernetes
print("Deploying to Kubernetes...")
run_cmd(["kubectl", "apply", "-f", k8s_deployment_file])
run_cmd(["kubectl", "get", "pods"])
