import os
from flask import Flask


def create_app(test_config=None):
    """create and configure the app"""
    
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(SECRET_KEY='random', DATABASE=os.path.join(app.instance_path, 'blogitt.sqlite'))
    
    if test_config == None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
        
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
        
    # add a simple page that says ciao
    @app.route('/ciao')
    def greeting():
        return "Ciao, World!"
        
    # register database related functions with app
    from . import db
    db.init_app(app)
    
    # regsiter auth blueprint
    from . import auth
    app.register_blueprint(auth.bp)
    
    # register blog blueprint
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
        
    return app