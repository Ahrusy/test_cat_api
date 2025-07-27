import pytest
from cat_api import get_random_cat_image_url
from unittest.mock import patch
import requests

def test_get_random_cat_image_url_success():
    mock_response = [{"url": "https://cdn2.thecatapi.com/images/abc123.jpg"}]

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = get_random_cat_image_url()
        assert result == "https://cdn2.thecatapi.com/images/abc123.jpg"

def test_get_random_cat_image_url_404():
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404

        result = get_random_cat_image_url()
        assert result is None
