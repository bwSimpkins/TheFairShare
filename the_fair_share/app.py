from flask import Flask, render_template, request  
import RentCalculator  # Import your Python script  

app = Flask(__name__)  

@app.route('/', methods=['GET', 'POST'])  
def index():  
    if request.method == 'POST':  
        user_input = request.form['user_input']  # Get input from form  
        result = RentCalculator.process_input(user_input)  # Process input in script.py  
        return render_template('index.html', result=result)  

    return render_template('index.html', result=None)  

if __name__ == '__main__':  
    app.run(debug=True)  