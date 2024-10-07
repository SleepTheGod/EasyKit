from flask import Flask, request, render_template, redirect, url_for
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    username = request.form['username']
    password = request.form['password']

    # Ensure the username and password are not empty
    if not username or not password:
        return render_template('index.html', error="Please provide both username and password.")

    try:
        # Create a new user
        subprocess.run(['adduser', username], check=True)
        # Set the password
        subprocess.run(['passwd', password], check=True)
        # Add user to the wheel group
        subprocess.run(['usermod', '-aG', 'wheel', username], check=True)

        return render_template('success.html', username=username)
    except subprocess.CalledProcessError as e:
        return render_template('index.html', error="An error occurred: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
