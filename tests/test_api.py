import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_criar_post():
    novo_post = {
        "title": "teste QA",
        "body": "conteúdo do post",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=novo_post)
    assert response.status_code == 201
    assert response.json()["title"] == "teste QA"

def test_get_post_inexistente():
    response = requests.get(f"{BASE_URL}/posts/99999")
    assert response.status_code == 404  

def test_get_lista_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert len(response.json()) == 100  