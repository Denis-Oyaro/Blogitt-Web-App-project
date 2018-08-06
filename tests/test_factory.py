from blogitt import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING':True}).testing
    

def test_ciao(client):
    response = client.get('/ciao')
    assert response.data == b'Ciao, World!'