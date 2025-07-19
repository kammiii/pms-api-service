from fastapi import status

def test_root_endpoint(public_client):
    response = public_client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Welcome to the PMS Integration Service"}

def test_health_endpoint(public_client):
    response = public_client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok"}
