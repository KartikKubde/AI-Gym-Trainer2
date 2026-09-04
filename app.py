import os
import sys

# Ensure 'Main App' directory is in Python path
main_app_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Main App")
if main_app_dir not in sys.path:
    sys.path.insert(0, main_app_dir)

# Change working directory to 'Main App'
os.chdir(main_app_dir)

from main import main

if __name__ == "__main__":
    main()
