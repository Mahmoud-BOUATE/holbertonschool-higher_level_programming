import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_products_from_json(file_path):
	with open(file_path, "r", encoding="utf-8") as file:
		data = json.load(file)

	if isinstance(data, dict):
		products = data.get("products", [])
	else:
		products = data

	return [
		{
			"id": int(product.get("id")),
			"name": product.get("name", ""),
			"category": product.get("category", ""),
			"price": float(product.get("price", 0)),
		}
		for product in products
	]


def read_products_from_csv(file_path):
	products = []
	with open(file_path, "r", encoding="utf-8") as file:
		reader = csv.DictReader(file)
		for row in reader:
			products.append(
				{
					"id": int(row.get("id", 0)),
					"name": row.get("name", ""),
					"category": row.get("category", ""),
					"price": float(row.get("price", 0)),
				}
			)
	return products


def read_products_from_sqlite(db_path):
	products = []
	connection = sqlite3.connect(db_path)
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT id, name, category, price FROM Products")
	rows = cursor.fetchall()
	connection.close()

	for row in rows:
		products.append(
			{
				"id": int(row["id"]),
				"name": row["name"],
				"category": row["category"],
				"price": float(row["price"]),
			}
		)

	return products


@app.route("/products")
def products():
	source = request.args.get("source", "").lower()
	product_id = request.args.get("id")

	if source == "json":
		product_list = read_products_from_json("products.json")
	elif source == "csv":
		product_list = read_products_from_csv("products.csv")
	elif source == "sql":
		try:
			product_list = read_products_from_sqlite("products.db")
		except sqlite3.Error:
			return render_template(
				"product_display.html", error="Database error", products=[]
			)
	else:
		return render_template("product_display.html", error="Wrong source", products=[])

	if product_id is not None:
		try:
			target_id = int(product_id)
		except ValueError:
			return render_template(
				"product_display.html", error="Product not found", products=[]
			)

		filtered_products = [
			product for product in product_list if product.get("id") == target_id
		]

		if not filtered_products:
			return render_template(
				"product_display.html", error="Product not found", products=[]
			)

		return render_template("product_display.html", products=filtered_products, error=None)

	return render_template("product_display.html", products=product_list, error=None)


if __name__ == "__main__":
	app.run(debug=True, port=5000)
