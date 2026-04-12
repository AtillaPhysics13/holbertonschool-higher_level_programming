from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route("/products")
def home():
    source = request.args.get("source")
    id = request.args.get("id")

    if source not in ["json", "csv"]:
        return render_template("product_display.html", error="Wrong source")

    if source == "json":
        with open("products.json", "r") as f:
            products = json.load(f)

    elif source == "csv":
        with open("products.csv", "r") as f:
            reader = csv.DictReader(f)
            products = list(reader)

    if id:
        new_products = []

        for p in products:
            if str(p["id"]) == id:
                new_products.append(p)

        if not new_products:
            return render_template("product_display.html", error="Product not found")

        products = new_products

    return render_template("product_display.html", products=products)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
