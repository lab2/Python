# REST tests
# Refer to source simple_rest_api.py

import os

import pytest
import requests

IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"

urls = ["http://localhost:5000/first", "http://localhost:5000/books"]


def make_request(base_url):
    response = requests.get(f'{base_url}')
    return response


@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Test doesn't work in Github actions")
def test_rest_with_sucess():
    assert '200' in str(make_request(urls[0]))
    assert '200' in str(make_request(urls[1]))


@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Test doesn't work in Github Actions.")
def test_rest_with_fail():
    assert "Java in action" in str(make_request(urls[1]).content)
    assert "Github in a nutshell" in str(make_request(urls[0]).content)


@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Test doesn't work in Github Actions.")
def test_rest_with_content():
    assert "Java in action" in str(make_request(urls[0]).content)
    assert "Github in a nutshell" in str(make_request(urls[1]).content)
