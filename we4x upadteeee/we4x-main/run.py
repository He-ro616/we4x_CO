import sys
import os

# Ensure the project folder is in Python's path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

try:
    from project import create_app
except ModuleNotFoundError as e:
    print("ERROR: Could not import 'project'. Make sure 'project/' exists and contains '__init__.py'.")
    raise e

# Create Flask app
app = create_app()

# =========================
# Main entry
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
