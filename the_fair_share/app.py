from flask import Flask, render_template, request, jsonify
import script  # Import the processing script

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        inputs = request.form.to_dict()  # Get user inputs
        result = script.process_multiple_inputs(inputs)  # Process them
        return jsonify({"result": result})  # Return sum as JSON
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
