"""
Simple Flask app for demonstration purposes.

This application exposes a single endpoint at the root URL ("/")
that returns a greeting message. It is intended as a minimal
example for a DevOps practice exercise.
"""

from flask import Flask


def create_app() -> Flask:
    """Factory function to create and configure the Flask application.

    Returns:
        Flask: A configured Flask app instance.
    """
    app = Flask(__name__)

    @app.route("/")
    def hello() -> str:
        """Return a friendly greeting.

        Returns:
            str: Greeting string "Hola Mundo".
        """
        return "Hola Mundo"

    return app


if __name__ == "__main__":
    # Only run the development server if executed directly.
    # In production the application will be served by a WSGI server
    # like gunicorn configured in the Dockerfile.
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
