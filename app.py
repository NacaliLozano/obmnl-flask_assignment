# Import libraries
fomr flask import Flask, request, url_for, redirect, render_template
# Instantiate Flask functionality
app = Flask(__name__)
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route('/', methods=['GET'])
def get_transacions():
    return render_template("transactions.html", transactions=transactions), 200

# Create operation
@app.route('/add', methods=['POST', "GET"])
def add_transaction():
    if request.method == "GET":
        return render_template("form.html"), 200
    else:
        transaction = {
              'id': len(transactions)+1
              'date': request.form['date']
              'amount': float(request.form['amount'])
             }
        transactions.append(transaction)
        return {"message": "Transaction added succesfully\n"}, 200

# Update operation
@app.route('/edit/<int: transaction_id>', methods=['POST', "GET"])
def edit_transaction(transaction_id):
    if request.method == "GET":
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                # Render the edit form template and pass the transaction to be edited
                return render_template("edit.html", transaction=transaction)
    else:
        for transaction in transactions:
            if transaction["id"] == transaction_id:
                transaction['date'] = request.form['date']
                transaction['amount'] = float(request.form['amount'])
                return {"message": "Transaction updated succesfully\n"}, 200
    # If the transaction with the specified ID is not found, handle this case
    return {"message": "Transaction not found"}, 404
# Delete operation

# Run the Flask app
    