from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the main page that shows the form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # If the form is submitted, process the form data and perform calculations
        # You might want to redirect to the results page after processing
        return results()
    # If it's a GET request, just render the form
    return render_template('index.html')

# Route for the results page that processes the form data and shows the results
@app.route('/results', methods=['POST'])
def results():
    # Extract form data
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    days = int(request.form['days'])
    initial_equity = float(request.form['initial_equity'])
    
    # Perform calculations and generate plots
    # ...

    # Render the results page with the calculated data
    return render_template('results.html', equity_curves=equity_curves)

if __name__ == '__main__':
    app.run(debug=True)





