# EasyKit RootKit By SleepTheGod aka ClumsyLulz

# Installation
Note type this in your terminal I use gitbash witch you can download here https://git-scm.com/downloads
```bash
git clone https://github.com/SleepTheGod/EasyKit
chmod +x EasyKit
cd EasyKit
chmod +x app.py
pip install -r requirements.txt
python app.py
http://127.0.0.1:5000
```

Security Warning: The code provided here can have serious security implications, especially if misused. This Flask app directly executes system commands based on user input, which can lead to command injection vulnerabilities. Ensure that this is used in a controlled environment and never in production or public-facing applications.
Permissions: Running this code will require administrative privileges. Make sure the Flask server is running in an environment where the user has the necessary permissions to execute these commands.
Environment Setup: To run this Flask app, you need to have Flask installed. You can do this with the command pip install Flask.
Run the App: Save the Python code in a file named app.py and run it using python app.py. The application will be accessible at http://127.0.0.1:5000.
