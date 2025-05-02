from flask import Flask, render_template
import json
import pymysql

app = Flask(__name__)

@app.route('/create')
def create(): 
    endpoint = "database-233523a.crobh44znaqo.us-east-1.rds.amazonaws.com"
    username = "admin"
    password = "Qwas1357"
    database_name = "db1"

    try:
        conn = pymysql.connect(host=endpoint, user=username, password=password, database=database_name)

        if conn.open:
            cursor = conn.cursor()
            query = f"""CREATE TABLE products (product_id INT NOT NULL AUTO_INCREMENT, product_name VARCHAR(255) NOT NULL,
 product_price DECIMAL(10,2) NOT NULL, product_description TEXT NOT NULL, PRIMARY KEY (product_id));"""
            cursor.execute(query)
            conn.commit()
            return f"Table products is created."
    except pymysql.Error as e:
        return f"There is an issue in creating Table products. {e}"

@app.route('/delete')
def delete():
    endpoint = "database-233523a.crobh44znaqo.us-east-1.rds.amazonaws.com"
    username = "admin"
    password = "Qwas1357"
    database_name = "db1"

    try:
        conn = pymysql.connect(host=endpoint, user=username, password=password, database=database_name)

        if conn.open:
            cursor = conn.cursor()
            query = f"""DROP TABLE products;"""
            cursor.execute(query)
            conn.commit()
            return f"Table products is deleted."
    except pymysql.Error as e:
        return f"There is an issue in deleting Table products. {e}"

@app.route('/insert/<product_name>/<float:product_price>/<string:product_description>')
def insert(product_name, product_price, product_description):
    endpoint = "database-233523a.crobh44znaqo.us-east-1.rds.amazonaws.com"
    username = "admin"
    password = "Qwas1357"
    database_name = "db1"

    try:
        conn = pymysql.connect(host=endpoint, user=username, password=password, database=database_name)

        if conn.open:
            cursor = conn.cursor()
            query = "INSERT INTO products (product_name, product_price, product_description) VALUES (%s, %s, %s)"
            cursor.execute(query, (product_name, product_price, product_description))
            conn.commit()
            return f"Product {product_name} is inserted."
    except pymysql.Error as e:
        return f"There is an issue in inserting Product {product_name}. {e}"

@app.route('/update/<int:product_id>/<product_name>/<float:product_price>/<string:product_description>')
def update(product_id, product_name, product_price, product_description):
    endpoint = "database-233523a.crobh44znaqo.us-east-1.rds.amazonaws.com"
    username = "admin"
    password = "Qwas1357"
    database_name = "db1"

    try:
        conn = pymysql.connect(host=endpoint, user=username, password=password, database=database_name)

        if conn.open:
            cursor = conn.cursor()
            query = "UPDATE products SET product_name = %s, product_price = %s, product_description = %s WHERE product_id = %s"
            cursor.execute(query, (product_name, product_price, product_description, product_id))
            conn.commit()
            return f"Product {product_name} is updated."
    except pymysql.Error as e:
        return f"There is an issue in updating Product {product_name}. {e}"

@app.route('/select')
def select():
    endpoint = "database-233523a.crobh44znaqo.us-east-1.rds.amazonaws.com"
    username = "admin"
    password = "Qwas1357"
    database_name = "db1"
    products = []

    try:
        conn = pymysql.connect(host=endpoint, user=username, password=password, database=database_name)

        if conn.open:
            cursor = conn.cursor()
            query = "SELECT * FROM products"
            cursor.execute(query)
            conn.commit()
            rows = cursor.fetchall()

            products = []
            product_id = ''
            product_name = ''
            product_description = ''

            for row in rows:
                product_id, product_name, product_price, product_description = row
                products.append({'product_id': str(product_id), 'product_name': product_name, 'product_price': str(product_price), 'product_description': product_description})

            return json.dumps(products)

    except pymysql.Error as e:
        return f"There is an issue in selecting the products. {e}"

@app.route('/')
def index():
    endpoint = "database-233523a.crobh44znaqo.us-east-1.rds.amazonaws.com"
    username = "admin"
    password = "Qwas1357"
    database_name = "db1"
    products = []

    try:
        conn = pymysql.connect(host=endpoint, user=username, password=password, database=database_name)

        if conn.open:
            cursor = conn.cursor()
            query = "SELECT * FROM products"
            cursor.execute(query)
            conn.commit()
            rows = cursor.fetchall()

            products = []
            product_id = ''
            product_name = ''
            product_description = ''

            for row in rows:
                product_id, product_name, product_price, product_description = row
                products.append({'product_id': str(product_id), 'product_name': product_name, 'product_price': str(product_price), 'product_description': product_description})

            return render_template('index.html', products=products)

    except pymysql.Error as e:
        return f"There is an issue in selecting the products. {e}"

if __name__ == "__main__":
        app.run()