# import the Flask class from the flask module
from flask import Flask, send_file, make_response, render_template, request
import n_monty_hall

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('input_data.html')


@app.route('/results', methods = ['GET','POST'])
def chart():
    if request.method == 'POST':
        result = request.form
        mydata = n_monty_hall.generateGameData(num_doors_power = int(result['numDoors']), num_trials_power = int(result['numTrials']), switch_strategy = 'switch')
        bytes_obj = n_monty_hall.plotThings(mydata)
        return send_file(bytes_obj, attachment_filename='plot.png', mimetype='image/png')

    elif request.method == 'GET':
        mydata = n_monty_hall.generateGameData(num_doors_power = 5, num_trials_power = 8, switch_strategy = 'switch')
        bytes_obj = n_monty_hall.plotThings(mydata)
        return send_file(bytes_obj, attachment_filename='plot.png', mimetype='image/png')

@app.route('/about')
def about():
    return "This is Mike's project about the Monty Hall Program"

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)