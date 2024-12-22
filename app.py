from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store flight data in memory for simplicity
flights = []

@app.route('/')
def home():
    return render_template('index.html', flights=flights)

@app.route('/add_flight', methods=['GET', 'POST'])
def add_flight():
    if request.method == 'POST':
        # Get form data
        departure = request.form.get('departure')
        destination = request.form.get('destination')
        distance = request.form.get('distance')
        price = request.form.get('price')

        # Validate and add to flights list
        if departure and destination and distance.isdigit() and price.isdigit():
            flights.append((departure, destination, int(distance), int(price)))
            return redirect(url_for('home'))
        else:
            return "Invalid input. Please try again.", 400

    return render_template('add_flight.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
