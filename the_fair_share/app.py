from flask import Flask, render_template, request, jsonify
import script  # Import your Python script

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]  # Get input from form
        result = script.process_input(user_input)  # Process input in script.py
        return jsonify({"result": result})  # Send JSON response
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
