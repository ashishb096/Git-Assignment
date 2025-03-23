from flask import Flask, jsonify
import json

app =Flask(__name__)

#Function to load data from file
def load_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

@app.route('/api',methods=['GET'])
def get_data():
    #Read the data from backend file
    data= load_data()

    #Return the data as JSON response
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)