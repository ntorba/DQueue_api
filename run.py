#/run.py

import os
from src.app import create_app
from flask import render_template


if __name__ == '__main__':
    env_name=os.getenv('FLASK_ENV')
    app=create_app(env_name)
    app.run()
