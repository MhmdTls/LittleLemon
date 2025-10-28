Little Lemon Restaurant API

This project is a Django REST Framework application for the Little Lemon restaurant. It includes APIs for Menu items and Table Booking, with user registration and token-based authentication.

API Endpoints
Menu API

List all menu items / Create new menu item
GET / restaurant/menu/
POST / restaurant/menu/
Body (JSON for POST):

{
  "title": "Pizza",
  "price": 15.50,
  "inventory": 50
}


Retrieve, Update, Delete a single menu item
GET / restaurant/menu/<id>/
PUT / restaurant/menu/<id>/
DELETE / restaurant/menu/<id>/
Body (JSON for PUT):

{
  "title": "Updated Pizza",
  "price": 16.00,
  "inventory": 45
}

Table Booking API

List all bookings / Create new booking
GET / restaurant/booking/
POST / restaurant/booking/
Requires authentication

User Authentication (Djoser)

Register new user
POST / auth/users/
Body (JSON):

{
  "username": "yourusername",
  "password": "yourpassword"
}


Obtain auth token (Login)
POST / auth/token/login/
Body (JSON):

{
  "username": "yourusername",
  "password": "yourpassword"
}


Logout user
POST / auth/token/logout/
Requires authentication

Notes

All authenticated requests (Booking API) require the token to be passed as Bearer Token in the Authorization header.

You can test the API using the Insomnia REST Client or any other API client like Postman.
