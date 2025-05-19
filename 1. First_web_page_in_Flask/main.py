# Importing the Flask class and the render_template function from the flask module
from flask import Flask, render_template

# Creating an instance of the Flask class.
# __name__ is a special variable that gets the name of the current module.
# Flask uses it to determine the root path for the application.
app = Flask(__name__)

# This is a route decorator.
# It tells Flask to execute the 'home' function when someone visits the "/" URL (i.e., the homepage).
@app.route("/")
def home():
    # This function will return the rendered 'index.html' file from the 'templates' folder.
    return render_template("index.html")

# This condition checks if this script is being run directly (not imported as a module).
if __name__ == "__main__":
    # Runs the Flask web server in debug mode.
    # Debug mode allows automatic reloading and gives detailed error messages.
    app.run(debug=True)
