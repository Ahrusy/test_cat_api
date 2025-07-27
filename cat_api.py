import requests
from typing import Optional

def get_random_cat_image_url() -> Optional[str]:
    """
    Делает запрос к TheCatAPI для получения случайного изображения кошки.

    Returns:
        str: URL изображения кошки, если запрос успешен.
        None: Если запрос завершился ошибкой.
    """
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data and isinstance(data, list) and "url" in data[0]:
                return data[0]["url"]
        return None
    except requests.RequestException:
        return None
