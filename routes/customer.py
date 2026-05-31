from flask import Blueprint, render_template
from database.customer_table import CUSTOMERS

customer_route = Blueprint('customer', __name__)

@customer_route.route('/')
def list_customers():
    """ list customers """
    return render_template('list_customers.html', customers=CUSTOMERS)


@customer_route.route('/', methods=['POST'])
def insert_customer():
    """ inserts customer data into the database """
    pass

@customer_route.route('/new')
def form_customer():
    """ form to register a new customer """
    return render_template('form_customer.html')

@customer_route.route('/<int:customer_id>')
def detail_customer(customer_id):
    """ shows customer details by ID """
    return render_template('detail_customer.html')

@customer_route.route('/<int:customer_id>/edit')
def form_edit_customer(customer_id):
    """ form to update a specific customer by ID """
    return render_template('form_edit_customer.html')

@customer_route.route('/<int:customer_id>/update', methods=['PUT'])
def update_customer(customer_id):
    """ updates a specific customer by ID """
    pass

@customer_route.route('/<int:customer_id>/delete', methods=['DELETE'])
def delete_customer(customer_id):
    """ deletes a specific customer by ID """
    pass