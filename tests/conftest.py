import os
import tempfile

import pytest
from blogitt import create_app
from blogitt.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')
    
    
@pytest.fixture
def app():
    db_fh, db_path = tempfile.mkstemp()
    
    app = create_app({'TESTING':True, 'DATABASE':db_path})
    with app.app_context():
        init_db()   # initialize temp database with tables
        get_db().executescript(_data_sql) # populate temp database with some data
        
    yield app
    
    os.close(db_fh)
    os.unlink(db_path)
    
    
@pytest.fixture
def client(app):
    return app.test_client()
    
    
@pytest.fixture
def runner(app):
    return app.test_cli_runner()
    
    
class AuthActions(object):
    def __init__(self, client):
        self._client = client
        
    def login(self, username='test', password='test'):
        return self._client.post(
              '/auth/login',
              data={'username':username, 'password':password}
        )
        
    def logout(self):
        return self._client.get('/auth/logout')
        
        
@pytest.fixture
def auth(client):
    return AuthActions(client)
        
        
