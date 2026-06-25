⚡ Python URL Shortener
A clean, fast, and lightweight URL shortener built with Python and Flask. This project converts long, cumbersome URLs into short, manageable links that seamlessly redirect to the original destination.


✨ Features
Instant Shortening: Generates a unique 6-character short link in milliseconds.
Seamless Redirection: Automatically redirects short links to the original long URLs.
Minimalist UI: Clean and responsive web interface built with native HTML/CSS.
In-Memory Storage: Utilizes a high-performance dictionary for instant URL mapping (ideal for demos and lightweight deployments).
🛠️ Tech Stack
Backend: Python 3.14
Web Framework: Flask
Production Server: Gunicorn
Hosting: Render
Version Control: Git & GitHub
🚀 Getting Started (Run Locally)
Follow these steps to get a copy of the project up and running on your local machine for development and testing.

Prerequisites
Python 3.8+ installed on your machine.
Basic knowledge of using a terminal/command prompt.
Installation
Clone the repository:
git clone https://github.com/Saikiran58ravula/url-shortener.git
Navigate to the project directory:
bash

cd url-shortener
Create a virtual environment (Optional but recommended):
bash

python -m venv venv
Activate it:
Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate
Install the required dependencies:
bash

pip install -r requirements.txt
Running the App
Run the Flask development server:

bash

python app.py
The application will now be running locally at: http://127.0.0.1:5000

📂 Project Structure
text

url-shortener/
│
├── app.py               # Main application logic, routing, and HTML template
├── requirements.txt     # Python dependencies (Flask, Gunicorn)
├── README.md            # Project documentation (you are here!)
└── .gitignore           # Files ignored by Git (if added later)
🚧 Future Enhancements
Integrate a persistent database (PostgreSQL or SQLite) to save links permanently.
Add custom alias support (e.g., site.com/my-custom-name).
Implement link expiration dates.
Add click analytics/tracking.
📄 License
This project is open source and available under the MIT License.

Built with ❤️ by Saikiran58ravula
