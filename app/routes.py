from app import app # from the app folder, import the app variable (Flask instance)
from flask import request
from app.schemas.customerSchema import customer_input_schema, customer_output_schema, customers_schema
from app.schemas.productSchema import product_schema, products_schema
from marshmallow import ValidationError
from app.database import db
from app.models import Customer, Product
from werkzeug.security import generate_password_hash

@app.route('/')
def index():
    return 'Goodbye'

# Customer Routes

# Get all customers
@app.route('/customers', methods=['GET'])
def get_all_customers():
    query = db.select(Customer)
    customers = db.session.scalars(query).all()
    return customers_schema.jsonify(customers)


# Get a single customer by ID
@app.route('/customers/<int:customer_id>', methods=["GET"])
def get_single_customer(customer_id):
    # Search the database for a customer with that ID
    customer = db.session.get(Customer, customer_id)
    # Check if we get a customer back or None
    if customer is not None:
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
        # Query the customer table to see if any customers have that username or email
        query = db.select(Customer).where( (Customer.username == customer_data['username']) | (Customer.email == customer_data['email']) )
        check_customers = db.session.scalars(query).all()
        if check_customers: # If there are customers in the check_customers list (empty list evaluates to False)
            return {"error": "Customer with that username and/or email already exists"}, 400 # Bad Request by Client
        # Create a new instance of Customer 
        new_customer = Customer(
            first_name=customer_data['first_name'],
            last_name=customer_data['last_name'],
            username=customer_data['username'],
            email=customer_data['email'],
            password=generate_password_hash(customer_data['password'])
        )
        # and add to the database
        db.session.add(new_customer)
        db.session.commit()
        # Serialize the new customer object and return with 201 status
        return customer_output_schema.jsonify(new_customer), 201 # Created - Success
    except ValidationError as err:
        return err.messages, 400
    except ValueError as err:
        return {"error": str(err)}, 400



# Product Endpoints 

# Get all products
@app.route('/products', methods=["GET"])
def get_all_products():
    query = db.select(Product)
    products = db.session.scalars(query).all()
    return products_schema.jsonify(products)   

# Get a single product by ID
@app.route('/products/<int:product_id>', methods=["GET"])
def get_single_product(product_id):
    # Search the database for a product with that ID
    product = db.session.get(Product, product_id)
    # Check if we get a customer back or None
    if product is not None:
        return product_schema.jsonify(product)
    return {"error": f"Product with ID {product_id} does not exist"}, 404 # Not Found
