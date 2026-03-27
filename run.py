"""Local run entrypoint for Windows/macOS/Linux.

Usage:
    python run.py
"""

from fastapi_translation_platform.app.app import app

if __name__ == "__main__":
    app.run(debug=True)
