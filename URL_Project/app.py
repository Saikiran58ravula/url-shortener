from flask import Flask, request, redirect, render_template_string
import uuid

app = Flask(__name__)

# Simulating a database using a Python dictionary
url_database = {}

# Simple HTML User Interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Python URL Shortener</title></head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    <h1>URL Shortener</h1>
    <form method="POST">
        <input type="text" name="original_url" placeholder="Enter long URL here" style="width: 300px; padding: 10px;" required>
        <button type="submit" style="padding: 10px;">Shorten</button>
    </form>
    {% if short_url %}
        <br><br>
        <p>Your shortened URL is: <b><a href="{{ short_url }}" target="_blank">{{ short_url }}</a></b></p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None
    if request.method == 'POST':
        original_url = request.form['original_url']
        # Generate unique ID
        unique_id = str(uuid.uuid4())[:6]
        short_url = f"http://127.0.0.1:5000/{unique_id}"
        
        # Store in database
        url_database[unique_id] = original_url
        
    return render_template_string(HTML_TEMPLATE, short_url=short_url)

@app.route('/<short_id>')
def redirect_url(short_id):
    # Retrieve original URL and redirect
    original_url = url_database.get(short_id)
    if original_url:
        return redirect(original_url)
    return "URL not found!", 404

if __name__ == '__main__':
    app.run(debug=True)