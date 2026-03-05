# schema.py — Define your database tables here
# The LLM reads this to understand what tables and columns exist

DATABASE_SCHEMA = """
You have access to a PostgreSQL e-commerce database with the following tables:

TABLE: customers
  - customer_id (INTEGER, PRIMARY KEY)
  - email (VARCHAR)
  - first_name (VARCHAR)
  - last_name (VARCHAR)
  - city (VARCHAR)
  - country (VARCHAR)
  - created_at (TIMESTAMP)

TABLE: products
  - product_id (INTEGER, PRIMARY KEY)
  - product_name (VARCHAR)
  - category (VARCHAR)         -- e.g. 'Electronics', 'Clothing', 'Books'
  - price (DECIMAL)            -- in USD
  - stock_quantity (INTEGER)

TABLE: orders
  - order_id (INTEGER, PRIMARY KEY)
  - customer_id (INTEGER, FOREIGN KEY -> customers.customer_id)
  - order_date (DATE)
  - status (VARCHAR)           -- 'pending', 'shipped', 'delivered', 'cancelled'
  - total_amount (DECIMAL)

TABLE: order_items
  - item_id (INTEGER, PRIMARY KEY)
  - order_id (INTEGER, FOREIGN KEY -> orders.order_id)
  - product_id (INTEGER, FOREIGN KEY -> products.product_id)
  - quantity (INTEGER)
  - unit_price (DECIMAL)

Important notes:
- Always use table aliases for clarity (e.g., c for customers, o for orders)
- Use date_trunc('month', order_date) for monthly groupings
- Cancelled orders should be excluded from revenue calculations
- All prices are in USD
"""