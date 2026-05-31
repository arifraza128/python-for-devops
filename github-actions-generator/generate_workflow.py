import os

TEMPLATES = {
    "python": "templates/python-ci.yml",
    "node": "templates/nodejs-ci.yml",
    "docker": "templates/docker-build.yml"
}

print("\nAvailable Workflows:")
print("python")
print("node")
print("docker")

workflow_type = input("\nEnter workflow type: ").lower()

if workflow_type not in TEMPLATES:
    print("Invalid workflow type!")
    exit()

os.makedirs(".github/workflows", exist_ok=True)

template_path = TEMPLATES[workflow_type]

with open(template_path, "r") as template:
    content = template.read()

output_file = f".github/workflows/{workflow_type}.yml"

with open(output_file, "w") as workflow:
    workflow.write(content)

print(f"\nWorkflow created successfully!")
print(f"Location: {output_file}")
