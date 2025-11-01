
import pytest
import requests
from app import app, db, Product, Order

# Test data
product_data = {'name': 'New Product', 'price': 19.99}
order_data = {'product_id': 1, 'quantity': 2}

@pytest.fixture
def client():
    # Create a test client
    with app.test_client() as client:
        yield client

def test_create_product(client):
    # Create a new product
    response = client.post('/products', json=product_data)
    assert response.status_code == 201
    assert response.get_json()['name'] == product_data['name']
    assert response.get_json()['price'] == product_data['price']

def test_get_product(client):
    # Create a new product
    response = client.post('/products', json=product_data)
    product_id = response.get_json()['id']

    # Get the product
    response = client.get(f'/products/{product_id}')
    assert response.status_code == 200
    assert response.get_json()['name'] == product_data['name']
    assert response.get_json()['price'] == product_data['price']

def test_update_product(client):
    # Create a new product
    response = client.post('/products', json=product_data)
    product_id = response.get_json()['id']

    # Update the product
    updated_product_data = {'name': 'Updated Product', 'price': 29.99}
    response = client.put(f'/products/{product_id}', json=updated_product_data)
    assert response.status_code == 200
    assert response.get_json()['name'] == updated_product_data['name']
    assert response.get_json()['price'] == updated_product_data['price']

def test_delete_product(client):
    # Create a new product
    response = client.post('/products', json=product_data)
    product_id = response.get_json()['id']

    # Delete the product
    response = client.delete(f'/products/{product_id}')
    assert response.status_code == 204

    # Verify that the product is removed from the database
    with app.app_context():
        product = db.session.get(Product, product_id)
        assert product is None