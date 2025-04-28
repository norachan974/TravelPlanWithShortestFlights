from flask import Flask, render_template, request, redirect, url_for
from algorithm import flights, build_graph, shortest_path_to_visit_all_nodes, graph, shortest_flights_for_path

app = Flask(__name__)

# Store flight data in memory for simplicity
flights = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get city names from the form
        cities = request.form.getlist('city')
        # Process the city names
        result = shortest_flights_for_path(cities, graph)
        # Render result on the page
        return render_template('index.html', cities=cities, result=result)
    return render_template('index.html')

@app.route('/add_flight', methods=['GET', 'POST'])
def add_flight():
    if request.method == 'POST':
        # Get form data
        departure = request.form.get('departure')
        destination = request.form.get('destination')
        distance = request.form.get('duration')
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
