from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/base.db"
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/users/')
def get_users():
    users = User.query.all()
    users_result = []
    for user in users:
        users_result.append(user.get_user_dict())

    return jsonify(users_result)


@app.route('/users/<int:id>')
def get_one_user(id: int):
    user = User.query.get(id)

    if user is None:
        return "user not found"

    return jsonify(user.get_user_dict())


@app.route('/orders/')
def get_orders():
    orders = Order.query.all()
    orders_result = []
    for order in orders:
        orders_result.append(order.get_order_dict())

    return jsonify(orders_result)


@app.route('/orders/<int:id>')
def get_one_order(id: int):
    order = Order.query.get(id)

    if order is None:
        return "order not found"

    return jsonify(order.get_order_dict())


@app.route('/offers/')
def get_offers():
    offers = Offer.query.all()
    offers_result = []
    for offer in offers:
        offers_result.append(offer.get_offer_dict())

    return jsonify(offers_result)


@app.route('/offers/<int:id>')
def get_one_offer(id: int):
    offer = Offer.query.get(id)

    if offer is None:
        return "offer not found"

    return jsonify(offer.get_offer_dict())


@app.route('/users/', methods=['POST'])
def create_user():
    data = request.form
    user = User(first_name=data.get("first_name", None),
                last_name=data.get("last_name", None),
                age=data.get("age", None),
                email=data.get("email", None),
                role=data.get("role", None),
                phone=data.get("phone", None)
                )

    db.session.add(user)
    db.session.commit()

    return jsonify(user.get_user_dict())


@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def update_delete_user(id: int):
    user = db.session.query(User).get(id)

    if user is None:
        return "user not found"

    if request.method == 'GET':

        return jsonify(user.get_user_dict())

    elif request.method == 'PUT':
        data = request.form
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.age = data.get('age')
        user.email = data.get('email')
        user.role = data.get('role')
        user.phone = data.get('phone')

        db.session.add(user)
        db.session.commit()

        return "user updated"
        # return jsonify(user.get_user_dict())

    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()

        return "user deleted"


@app.route('/orders/', methods=['POST'])
def create_order():
    data = request.form

    start_date = data.get('start_date', None)
    if start_date is not None:
        start_date = get_datetime(start_date)

    end_date = data.get('end_date', None)
    if end_date is not None:
        end_date = get_datetime(end_date)

    order = Order(name=data.get("name", None),
                  description=data.get("description", None),
                  start_date=start_date,
                  end_date=end_date,
                  address=data.get("address", None),
                  price=data.get("price", None),
                  customer_id=data.get("customer_id", None),
                  executor_id=data.get("executor_id", None)
                  )

    db.session.add(order)
    db.session.commit()

    return jsonify(order.get_order_dict())


@app.route('/orders/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def update_delete_order(id: int):
    order = db.session.query(Order).get(id)

    if order is None:
        return "order not found"

    if request.method == 'GET':

        return jsonify(order.get_order_dict())

    elif request.method == 'PUT':
        data = request.form

        order.name = data.get('name')
        order.description = data.get('description')
        order.start_date = data.get('start_date')
        order.end_date = data.get('end_date')
        order.address = data.get('address')
        order.price = data.get('price')
        order.customer_id = data.get('customer_id')
        order.executor_id = data.get('executor_id')

        db.session.add(order)
        db.session.commit()

        return "order updated"

    elif request.method == 'DELETE':
        db.session.delete(order)
        db.session.commit()

        return "order deleted"


@app.route('/offers/', methods=['POST'])
def create_offer():
    data = request.form
    offer = Offer(order_id=data.get("order_id", None),
                  executor_id=data.get("executor_id", None)
                  )

    db.session.add(offer)
    db.session.commit()

    return jsonify(offer.get_offer_dict())


@app.route('/offers/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def update_delete_offer(id: int):
    offer = db.session.query(Offer).get(id)

    if offer is None:
        return "offer not found"

    if request.method == 'GET':

        return jsonify(offer.get_offer_dict())

    elif request.method == 'PUT':
        data = request.form

        offer.order_id = data.get('order_id')
        offer.executor_id = data.get('executor_id')

        db.session.add(offer)
        db.session.commit()

        return "offer updated"

    elif request.method == 'DELETE':
        db.session.delete(offer)
        db.session.commit()

        return "offer deleted"


if __name__ == '__main__':
    app.run(debug=True)
