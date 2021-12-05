"""
This is the principal file for execute
the web server.
"""

from flask import Flask, render_template

# initialating the server
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    """
    This route is for the initial route.
    """
    return render_template('home.html')


@app.route('/about')
def about():
    """
    This route is for the
    about page.
    """
    return render_template('about.html')


if __name__ == '__main__':
    # starting the server
    app.run(port = 5000, debug = True)
