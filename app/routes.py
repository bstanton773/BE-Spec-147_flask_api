from app import app # from the app folder, import the app variable (Flask instance)
from flask import request

@app.route('/')
def index():
    return 'Goodbye'


customers = [
    {
        "id": 1,
        "first_name": "Brian",
        "last_name": "Stanton",
        "username": "brians",
        "email": "brians@codingtemple.com"
    },
    {
        "id": 2,
        "first_name": "Ryan",
        "last_name": "Rhoades",
        "username": "ryanr",
        "email": "ryanr@codingtemple.com"
    },
]

# Customer Routes

# Get all customers
@app.route('/customers', methods=['GET'])
def get_all_customers():
    return customers


# Get a single customer by ID
@app.route('/customers/<int:customer_id>', methods=["GET"])
def get_single_customer(customer_id):
    # Search for a customer with that ID
    for customer in customers:
        if customer['id'] == customer_id:
            return customer
    return {"error": f"Customer with ID {customer_id} does not exist"}, 404 # Not Found


# Create a new customer
@app.route('/customers', methods=["POST"])
def create_customer():
    # Check if the request has a JSON body
    if not request.is_json:
        return {"error": "Request body must be application/json"}, 400 # Bad Request by Client
    # Get the request JSON body
    data = request.json
    # Check if the body has all of the required fields
    required_fields = ["first_name", "last_name", "username", "email"]
    for field in required_fields:
        if field not in data:
            return {"error": f"{field} is required to create a customer"}, 400
    # Add the data (with a new id) to the customers list
    data["id"] = len(customers) + 1
    customers.append(data)
    return data, 201 # Created - Success

