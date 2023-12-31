import pytest
import sqlite3
from modules.common.database import Database

# This part is an individual task to practice testing skills after the QA Automation Course.

# Check if Error message appears if Null id inserted.
@pytest.mark.database
def test_null_id_insert():
    db = Database()

    with pytest.raises(sqlite3.OperationalError):
        db.insert_product(None, 'any product', 'any description', 200)

# Select all products with minimum amount.
@pytest.mark.database
def test_min_amount_of_product():
    db = Database()
    db.get_product_with_min_quantity()
    low_stock_products = db.get_product_with_min_quantity()
    print("Products are about to run out", low_stock_products)

    assert len(low_stock_products) != 0
    assert low_stock_products[0][0] == 'солодка вода'
    assert low_stock_products[0][1] == 10
    assert low_stock_products[1][0] == 'молоко'
    assert low_stock_products[1][1] == 10

# Select all products with maximum amount.
@pytest.mark.database
def test_max_amount_of_product():
    db = Database()
    db.get_product_with_max_quantity()
    plenty_stock_products = db.get_product_with_max_quantity()
    print("Products are enough", plenty_stock_products)

    assert len(plenty_stock_products) != 0

# Check inserting unexpected datatype.
@pytest.mark.database
def test_incorrect_datatype_insert():
    db = Database()

    with pytest.raises(sqlite3.OperationalError):
        db.insert_product('number', 666, True, 'quantity')

    with pytest.raises(sqlite3.OperationalError):
        db.insert_product(99, 666, True, 'quantity')

# Check if Error message appears if not unique id inserted.
@pytest.mark.database
def test_existing_id_insert():
    db = Database()
    db.insert_order(99, 1, 1, '03:14:08')

    with pytest.raises(sqlite3.IntegrityError):
        db.insert_order(99, 2, 2, '03:14:08')

    db.delete_order_by_id(99)
    orders = db.get_all_orders()
    # Check quantity of orders still remains equal to 1
    assert len(orders) == 1


# This part is from QA Automation Course.

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1.
    assert len(orders) == 1

    # Check the structure of data.
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'