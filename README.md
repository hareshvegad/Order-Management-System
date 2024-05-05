# Order Management System

## Overview
This Python script manages orders using a SQLite3 database. It allows users to add orders, update existing orders, and export orders to an Excel file.

## Setup
1. **Dependencies**: Ensure you have Python 3.x installed along with the `sqlite3` and `pandas` libraries.
2. **Database Creation**: Upon running the script, a SQLite3 database named `orders.db` will be created (if not exists) with a table named `orders`.

## Functions

### `create_database()`
- Creates the SQLite3 database and the `orders` table if they don't exist.

### `add_order(order_name, product_name, order_quantity, order_amount)`
- Adds a new order to the database.
- Parameters:
  - `order_name`: Name of the order.
  - `product_name`: Name of the product.
  - `order_quantity`: Quantity of the product ordered.
  - `order_amount`: Total amount of the order.
- Returns the ID of the newly added order.

### `update_order(order_id, new_order_name, new_product_name, new_order_quantity, new_order_amount)`
- Updates an existing order in the database.
- Parameters:
  - `order_id`: ID of the order to be updated.
  - `new_order_name`: New name for the order.
  - `new_product_name`: New name for the product.
  - `new_order_quantity`: New quantity of the product ordered.
  - `new_order_amount`: New total amount of the order.

### `export_to_excel()`
- Reads orders from the database and exports them to an Excel file named `orders.xlsx`.

### `get_product_info_from_user()`
- Prompts the user to input product information (order name, product name, quantity, amount).
- Returns the entered information.

### `display_menu()`
- Displays menu options for the user to choose from.
- Returns the user's choice.

## Example Usage
- Upon execution, the script displays a menu.
- Users can add new orders by providing product information or update existing orders by specifying the order ID and entering new information.
- Orders are exported to an Excel file after each addition or update.

## Files
- `orders.db`: SQLite3 database file containing order data.
- `orders.xlsx`: Excel file containing exported order data.

