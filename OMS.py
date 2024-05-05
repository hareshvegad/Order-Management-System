import sqlite3
import pandas as pd
from datetime import datetime

# Function to create database and table if not exists
def create_database():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS orders
                 (order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 order_name TEXT,
                 product_name TEXT,
                 order_quantity INTEGER,
                 order_amount REAL,
                 order_date TEXT,
                 order_time TEXT)''')  # Added order_date and order_time columns
    conn.commit()
    conn.close()

# Function to add a new order
def add_order(order_name, product_name, order_quantity, order_amount):
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    order_date = datetime.now().strftime('%Y-%m-%d')  # Get current date
    order_time = datetime.now().strftime('%H:%M:%S')  # Get current time
    c.execute("INSERT INTO orders (order_name, product_name, order_quantity, order_amount, order_date, order_time) VALUES (?, ?, ?, ?, ?, ?)",
              (order_name, product_name, order_quantity, order_amount, order_date, order_time))
    conn.commit()
    order_id = c.lastrowid  # Retrieve the last inserted row id
    conn.close()
    return order_id

# Function to update an existing order
def update_order(order_id, new_order_name, new_product_name, new_order_quantity, new_order_amount):
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("UPDATE orders SET order_name=?, product_name=?, order_quantity=?, order_amount=? WHERE order_id=?",
              (new_order_name, new_product_name, new_order_quantity, new_order_amount, order_id))
    conn.commit()
    conn.close()

# Function to format orders into Excel
def export_to_excel():
    conn = sqlite3.connect('orders.db')
    df = pd.read_sql_query("SELECT * FROM orders", conn)
    df.to_excel('orders.xlsx', index=False)
    conn.close()

# Function to take product information from the user
def get_product_info_from_user():
    order_name = input("Enter order name: ")
    product_name = input("Enter product name: ")
    order_quantity = int(input("Enter order quantity: "))
    order_amount = float(input("Enter order amount: "))
    return order_name, product_name, order_quantity, order_amount

# Function to display menu options
def display_menu():
    print("1. Add Order")
    print("2. Update Order")
    choice = input("Enter your choice: ")
    return choice

# Example usage
create_database()

while True:
    choice = display_menu()
    if choice == '1':
        # Take product information from the user
        order_name, product_name, order_quantity, order_amount = get_product_info_from_user()

        # Add the order in the database and retrieve the order_id
        order_id = add_order(order_name, product_name, order_quantity, order_amount)
        print("Order added with ID:", order_id)

    elif choice == '2':
        order_id = input("Enter order ID to update: ")
        new_order_name, new_product_name, new_order_quantity, new_order_amount = get_product_info_from_user()

        # Update the order
        update_order(order_id, new_order_name, new_product_name, new_order_quantity, new_order_amount)
        print("Order updated successfully.")

    else:
        print("Invalid choice. Please select again.")
        continue

    export_to_excel()
    print("Orders exported to Excel.")
