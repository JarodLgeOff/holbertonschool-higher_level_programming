from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)


def read_json_products(product_id=None):
    """Read products from JSON file, optionally filter by id"""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            products = json.load(f)

        if product_id is not None:
            products = [p for p in products if p['id'] == product_id]

        return products
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def read_csv_products(product_id=None):
    """Read products from CSV file, optionally filter by id"""
    try:
        products = []
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)

        if product_id is not None:
            products = [p for p in products if p['id'] == product_id]

        return products
    except (FileNotFoundError, ValueError):
        return None


@app.route('/products')
def display_products():
    """Route to display products based on source and optional id"""
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', type=int)

    if source not in ['json', 'csv']:
        return render_template('product_display.html', 
                               error="Wrong source", products=None)

    if source == 'json':
        products = read_json_products(product_id)
    else:  
        products = read_csv_products(product_id)

    if products is None:
        return render_template('product_display.html',
                               error="Unable to load products", products=None)

    if product_id is not None and len(products) == 0:
        return render_template('product_display.html', 
                               error="Product not found", products=None)

    return render_template('product_display.html', error=None, 
                           products=products, source=source)


if __name__ == '__main__':
    app.run(debug=True)
