'''
Sometimes tests need to invoke functionality which depends on global settings or which invokes code which cannot be easily tested such as network access. The monkeypatch fixture helps you to safely set/delete an attribute, dictionary item or environment variable, or to modify sys.path for importing.

The monkeypatch fixture provides these helper methods for safely patching and mocking functionality in tests:
 - monkeypatch.setattr(obj, name, value, raising=True)
 - monkeypatch.delattr(obj, name, raising=True)
 - monkeypatch.setitem(mapping, name, value)
 - monkeypatch.delitem(obj, name, raising=True)
 - monkeypatch.setenv(name, value, prepend=None)
 - monkeypatch.delenv(name, raising=True)
 - monkeypatch.syspath_prepend(path)
 - monkeypatch.chdir(path)
 - monkeypatch.context()
'''
import os
from pathlib import Path
import requests

import pytest


# Monkeypatch a function to return path irrespective of the user
def getssh():
    return Path.home() / ".ssh"


def test_getssh(monkeypatch):
    # Mock return to replace Path.home() and always return the same path
    def mock_return():
        return Path("/abc")
    
    # Use monkeypatch to replace Path.home and return what the path defined above
    monkeypatch.setattr(Path, "home", mock_return)

    x = getssh()

    assert x == Path("/abc/.ssh")

# Monkeypatching returned objects
def get_url(url):
    res = requests.get(url)

    return res.json()

# Stop requests happening during your tests automatically (not necessary for the test to work, just safety precaution)
@pytest.fixture(autouse=True)
def stop_requests(monkeypatch):
    """Remove the requests.sessions.Session.request for all test automatically."""
    monkeypatch.delattr("requests.sessions.Session.request")

# Mock object to replace actual requests
class MockRequestsResponse:

    @staticmethod
    def json():
        return {"status_code": 200, "val": "test"}
    
def test_get_url(monkeypatch):
    # Get mocked object replacement
    def get_mock(*args, **kwargs):
        return MockRequestsResponse()
    
    # Use monkeypatch to update the behaviour of the requests.get method
    monkeypatch.setattr(requests, "get", get_mock)

    # Run the code that's being tested
    json_res = get_url("https://fakeurl.com")

    # Test the result is our mocked object
    assert json_res == {"status_code": 200, "val": "test"}

# Monkeypatching environment variables
def get_user_creds():
    username = os.getenv("USER")
    password = os.getenv("PASSWORD")

    if username is None or password is None:
        raise OSError("User credentials are not set in the environment.")
    
    return f"User creds: {username}:{password}"

def test_get_user_creds(monkeypatch):
    monkeypatch.setenv("USER", "TestUser")
    monkeypatch.setenv("PASSWORD", "TestPass")

    creds = get_user_creds()
    expected_value = "User creds: TestUser:TestPass"
    assert creds == expected_value

def test_user_failing(monkeypatch):
    monkeypatch.delenv("USER", raising=False)
    monkeypatch.setenv("PASSWORD", "TestPass")

    with pytest.raises(OSError):
        _ = get_user_creds()

def test_pass_failing(monkeypatch):
    monkeypatch.setenv("USER", "TestUser")
    monkeypatch.delenv("PASSWORD", raising=False)

    with pytest.raises(OSError):
        _ = get_user_creds()

# Monkeypatching dictionaries
DEFAULT_SERVER_CONFIGS = {
    "server_name": "actual_server",
    "backup_server": "actual_backup_server",
    "user": "actual_user",
    "pass": "actual_pass"
}

def create_connection_string(configs=DEFAULT_SERVER_CONFIGS):
    return f"Server: {configs['server_name']}; User: {configs['user']}; Pass: {configs['pass']}"

# Monkeypatch the config dict values for the test
def test_create_connection_string(monkeypatch):
    monkeypatch.setitem(DEFAULT_SERVER_CONFIGS, "server_name", "test_server")
    monkeypatch.setitem(DEFAULT_SERVER_CONFIGS, "user", "test_user")
    monkeypatch.setitem(DEFAULT_SERVER_CONFIGS, "pass", "test_pass")

    actual_value = create_connection_string()
    expected_value = "Server: test_server; User: test_user; Pass: test_pass"

    assert actual_value == expected_value

def test_connection_string_fails(monkeypatch):
    monkeypatch.delitem(DEFAULT_SERVER_CONFIGS, "server_name", raising=False)

    with pytest.raises(KeyError):
        _ = create_connection_string()
