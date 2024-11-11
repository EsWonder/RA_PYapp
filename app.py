from flask import Flask  # Import the Flask class from the flask module

# Create an instance of the Flask class, which will be the main application
app = Flask(__name__)

# Define the route for the root URL ("/")
@app.route('/')
def hello_world():
    # This function returns a message that will be displayed in the web browser
    return "Hola Mundo desde Python!"

# The if statement ensures that the application runs only if this script is executed directly, not if it is imported as a module
if __name__ == '__main__':
    # Run the application on all available network interfaces ('0.0.0.0') on port 5000
    app.run(host='0.0.0.0', port=5000)
