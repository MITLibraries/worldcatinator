import os
import pytest
import redirector
import requests_mock


@pytest.fixture
def client():
    redirector.app.config['TESTING'] = True

    with redirector.app.test_client() as client:
        yield client


def load_response(name):
    with open(_fixtures(name)) as f:
        r = f.read()
        return r


def _fixtures(path):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_dir, 'fixtures', path)


def test_ping(client):
    rv = client.get('/ping')
    assert b'pong' in rv.data


def test_redirect_to_item(client):
    with requests_mock.Mocker() as m:
        m.post(requests_mock.ANY, status_code=200,
               text=load_response('002544293.json'))
        response = client.get('/?bibid=002544293')
        assert 'https://mit.worldcat.org/oclc/962751146' in response.location


def test_redirect_generic_bad_bibid(client):
    with requests_mock.Mocker() as m:
        m.post(requests_mock.ANY, status_code=200,
               text=load_response('bad_bibid.json'))
        response = client.get('/?bibid=asdf')
        assert 'https://mit.worldcat.org/' in response.location


def test_redirect_bad_response(client):
    with requests_mock.Mocker() as m:
        m.post(requests_mock.ANY, status_code=500)
        response = client.get('/?bibid=asdf')
        assert 'https://mit.worldcat.org/' in response.location


def test_redirect_no_oclcs(client):
    with requests_mock.Mocker() as m:
        m.post(requests_mock.ANY, status_code=200,
               text=load_response('no_oclcs.json'))
        response = client.get('/?bibid=002544293')
        assert 'https://mit.worldcat.org/' in response.location


def test_redirect_with_no_bibid(client):
    response = client.get('/?yo=stuff')
    assert 'https://mit.worldcat.org/' in response.location


def test_redirect_with_no_args(client):
    response = client.get('/')
    assert 'https://mit.worldcat.org/' in response.location
