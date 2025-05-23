from flask import Flask, render_template_string

app = Flask(__name__)

# Define a simple HTML template with CSS
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome Page</title>
    <style>
        body {
            background-color: #f0f8ff;
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        h1 {
            color: #2c3e50;
        }
        p {
            font-size: 18px;
            color: #34495e;
        }
    </style>
</head>
<body>
    <h1>Welcome to IISN</h1>
    <p>Get Training From the Expert</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(debug=True)
