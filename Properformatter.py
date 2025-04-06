import json

# Load the notebook
with open("bug_detection.ipynb", "r", encoding="utf-8") as f:
    notebook = json.load(f)

# Remove the problematic widgets metadata
if "widgets" in notebook.get("metadata", {}):
    del notebook["metadata"]["widgets"]
    print("Removed metadata['widgets']")

# Save the cleaned notebook
with open("bug_detection_clean.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1)

print("modified the .ipynb file to be visited properly at github")
