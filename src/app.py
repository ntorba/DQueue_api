#src/app.py

from flask import Flask, render_template, request,jsonify

from .config import app_config
from .models import db, bcrypt

from .views.UserView import user_api as user_blueprint
from .views.PartyView import party_api as party_blueprint
from .views.SongView import song_api as song_blueprint

def create_app(env_name):
    """
    Create app
    """
    # app initialization
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    #initializing bcrypt and db
    bcrypt.init_app(app)
    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
    app.register_blueprint(party_blueprint, url_prefix='/api/v1/parties')
    app.register_blueprint(song_blueprint, url_prefix='/api/v1/songs')


    @app.route('/')
    def index():
        """
        index endpoint
        """
        return render_template('index.html')

    @app.route('/welcome')
    def welcome():
        return render_template('welcome.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/signup')
    def signUp():
        return render_template('signup.html')

    #This is for the template I took from codecademy requests class
    #I found a long decorator function on stack overflow that might
    #have let me call other api's, but I think the right solution
    #would be to use:
    #flask_cors
    #find that if I ever want to call another api
    #AKA THE SPOTIFY API
    @app.route('/datamuse-example')#, methods=['OPTIONS'])
    #@crossdomain(origin='*')
    def datamuse():
        return render_template('datamuse_example.html')




    return app
