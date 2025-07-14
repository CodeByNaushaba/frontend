from flask import Flask
from blueprints import blueprint_list

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add this if you use session

# Register blueprints
for bp in blueprint_list:
    app.register_blueprint(bp)

# Default route
@app.route('/')
def index():
    return "Welcome to Upwork Project Handler!"
