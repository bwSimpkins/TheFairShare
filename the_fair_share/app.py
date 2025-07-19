from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import script  # Import the processing script

app = Flask(__name__)

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        inputs = request.form.to_dict()  # Get user inputs
        rent_or_buy = inputs.get("rentOrBuy", "")  # Get rent or buy selection
        inputs["rentOrBuy"] = rent_or_buy  # Ensure it's included in inputs
        result = script.process_multiple_inputs(inputs)  # Process them
        return jsonify({'result': result['result'], 'percentage_income_one': result['percentage_income_one'], 'percentage_income_two': result['percentage_income_two'],
                        'year': result['year'], 'investment_total': result['investment_total']})  # Return values calculated in the script class
    
    return send_from_directory(parent_directory, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)
