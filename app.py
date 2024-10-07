from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

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
        # Mock user creation logic (since actual user management commands do not work on Windows)
        flash(f"User '{username}' would be created with the specified password (this is a simulation).")
        
        # Normally, you would save the user details to a database here
        
        return redirect(url_for('home'))
    except Exception as e:
        return render_template('index.html', error="An error occurred: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
