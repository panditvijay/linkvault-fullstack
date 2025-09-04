# user_service/api/tests.py
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_user_registration():
    """
    Ensure we can register a new user.
    """
    client = APIClient()
    url = reverse('register') # 'register' is the name we gave in api/urls.py
    data = {
        'username': 'newtestuser',
        'password': 'strongpassword123',
        'email': 'test@example.com'
    }
    
    response = client.post(url, data, format='json')
    
    # Assert that the request was successful
    assert response.status_code == 201 # 201 Created
    
    # Assert that the user was actually created in the database
    assert User.objects.filter(username='newtestuser').exists()

@pytest.mark.django_db
def test_user_login():
    """
    Ensure a registered user can log in and get a token.
    """
    # First, create a user to log in with
    User.objects.create_user(username='loginuser', password='loginpassword')
    
    client = APIClient()
    url = reverse('token_obtain_pair')
    data = {
        'username': 'loginuser',
        'password': 'loginpassword'
    }
    
    response = client.post(url, data, format='json')
    
    # Assert the request was successful
    assert response.status_code == 200 # 200 OK
    
    # Assert that 'access' and 'refresh' tokens are in the response data
    assert 'access' in response.data
    assert 'refresh' in response.data