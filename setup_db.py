from config import *
from models import *
from utils import *

db.drop_all()
db.create_all()

# создание таблицы 'users' с данными из 'users.json'
users_json = get_data_json(USERS_PATH)

users_list = []
for user in users_json:
    users_list.append(
        User(id=user["id"],
             first_name=user["first_name"],
             last_name=user["last_name"],
             age=user["age"],
             email=user["email"],
             role=user["role"],
             phone=user["phone"]
             )
    )

db.session.add_all(users_list)
db.session.commit()


# создание таблицы 'offers' с данными из 'offers.json'
offers_json = get_data_json(OFFERS_PATH)

offers_list = []
for offer in offers_json:
    offers_list.append(
        Offer(id=offer["id"],
              order_id=offer["order_id"],
              executor_id=offer["executor_id"]
              )
    )

db.session.add_all(offers_list)
db.session.commit()


# создание таблицы 'orders' с данными из 'orders.json'
orders_json = get_data_json(ORDERS_PATH)

orders_list = []
for order in orders_json:
    orders_list.append(
        Order(id=order["id"],
              name=order["name"],
              description=order["description"],
              start_date=get_datetime(order["start_date"]),
              end_date=get_datetime(order["end_date"]),
              address=order["address"],
              price=order["price"],
              customer_id=order["customer_id"],
              executor_id=order["executor_id"]
              )
    )


db.session.add_all(orders_list)
db.session.commit()

