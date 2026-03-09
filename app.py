from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Simple Bill Generator</h2>
    <form action="/bill" method="post">
        Customer Name:<br>
        <input type="text" name="name"><br><br>

        Item Name:<br>
        <input type="text" name="item"><br><br>

        Quantity:<br>
        <input type="number" name="quantity"><br><br>

        Price per Item:<br>
        <input type="number" name="price"><br><br>

        <input type="submit" value="Generate Bill">
    </form>
    """

@app.route("/bill", methods=["POST"])
def bill():
    name = request.form["name"]
    item = request.form["item"]
    quantity = int(request.form["quantity"])
    price = float(request.form["price"])

    total = quantity * price

    return f"""
    <h2>Bill Details</h2>
    <p><b>Customer Name:</b> {name}</p>
    <p><b>Item:</b> {item}</p>
    <p><b>Quantity:</b> {quantity}</p>
    <p><b>Price per Item:</b> ₹{price}</p>
    <p><b>Total Amount:</b> ₹{total}</p>
    <br>
    <a href="/">Create Another Bill</a>
    """

if __name__ == "__main__":
    app.run(debug=True,port=5001)
