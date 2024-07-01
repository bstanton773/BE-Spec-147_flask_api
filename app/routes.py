from app import app # from the app folder, import the app variable (Flask instance)
from flask import request
from app.schemas.customerSchema import customer_input_schema, customer_output_schema, customers_schema
from marshmallow import ValidationError

@app.route('/')
def index():
    return 'Goodbye'


customers = [
    {
        "id": 1,
        "first_name": "Brian",
        "last_name": "Stanton",
        "username": "brians",
        "email": "brians@codingtemple.com",
        "password": "abc123",
    },
    {
        "id": 2,
        "first_name": "Ryan",
        "last_name": "Rhoades",
        "username": "ryanr",
        "email": "ryanr@codingtemple.com",
        "password": "cba321"
    },
]

# Customer Routes

# Get all customers
@app.route('/customers', methods=['GET'])
def get_all_customers():
    return customers_schema.jsonify(customers)


# Get a single customer by ID
@app.route('/customers/<int:customer_id>', methods=["GET"])
def get_single_customer(customer_id):
    # Search for a customer with that ID
    for customer in customers:
        if customer['id'] == customer_id:
            return customer_output_schema.jsonify(customer)
    return {"error": f"Customer with ID {customer_id} does not exist"}, 404 # Not Found


# Create a new customer
@app.route('/customers', methods=["POST"])
def create_customer():
    # Check if the request has a JSON body
    if not request.is_json:
        return {"error": "Request body must be application/json"}, 400 # Bad Request by Client
    try:
        # Get the request JSON body
        data = request.json
        # Check if the body has all of the required fields
        customer_data = customer_input_schema.load(data)
        # Add the data (with a new id) to the customers list
        customer_data["id"] = len(customers) + 1
        customers.append(customer_data)
        return customer_output_schema.jsonify(customer_data), 201 # Created - Success
    except ValidationError as err:
        return err.messages, 400
    except ValueError as err:
        return {"error": str(err)}, 400

