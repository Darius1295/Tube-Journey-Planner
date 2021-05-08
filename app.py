from flask import Flask, request, render_template
from dijkstra import shortest_time
app = Flask(__name__)

app.config['SECRET_KEY'] = '7873abd825c5446b5bf76aaff507a337'


@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    result = None
    route_list = []
    travel_time = None

    if request.method == 'POST':
        start = request.form['start']
        finish = request.form['finish']
        result = shortest_time(start, finish)
        
        if result != "Error":
            stations = result[0]
            travel_time = result[1]

            for i in range(0, len(stations)):
                if stations[i].split()[0] != stations[i-1].split()[0]:
                    route_list.append(stations[i])


    route_list = route_list[1:]

    return render_template('home.html', title='Home', route_list=route_list, travel_time = travel_time, result=result)

