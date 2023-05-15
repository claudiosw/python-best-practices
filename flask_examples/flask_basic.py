""" Basic Flask Example
"""


from flask import Flask


def create_basic_flask_app():
    """ Basic Flask Example
    """
    app_basic = Flask(__name__)

    @app_basic.route("/")
    def index():
        """ Index route
        """
        return "Hello World!"

    return app_basic


if __name__ == "__main__":
    app = create_basic_flask_app()
    app.run(debug=True)
