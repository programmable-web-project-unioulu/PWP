from flask import Flask, app

default_config = { 'MONGODB_SETTINGS': {
    'db': 'logbotdatabase',
    'host': 'mongodb://128.214.254.176',
    'port': '9005'   
}}

def get_flask_app(config: dict = None) -> app.Flask:
    """
    Initializes Flask app with given configuration.
    :param config: Configuration dictionary
    :return: app
    """
    # init flask
    flask_app = Flask(__name__)

    # configure app
    config = default_config if config is None else config
    flask_app.config.update(config)

    return flask_app


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app = get_flask_app()
    app.run(debug=True)