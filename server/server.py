from flask import Flask, request, jsonify
import util

app = Flask(__name__)
# app.config["JSON_SORT_KEYS"] = False  ## prevent flask jsonify from sorting the data

@app.route('/hello')
def hello():
    return "Hey";

@app.route('/load_player_names')
def load_player_names():
    '''
    This function will load all the player names from the json file
    and return a list or a json file
    '''
    response = jsonify({
        'all_players': util.get_all_player_names()
    })
    response.headers.add('Access-control-Allow-Origin','*')

    return response


@app.route('/similar_players', methods=['POST'])
def similar_players():
    '''
    This function takes the inputs from the client
    The player and number of similar_players to be displayed
    And returns a table of players in json format
    '''
    player = request.form['player']
    num_player = int(request.form['num_player'])

    response = jsonify({
        'similar_players': util.display_similar_players(player,num_player)
    })
    response.headers.add('Access-control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print('Starting Python Flask Server for Player Scout')
    util.load_saved_artifacts()
    app.debug = True
    app.run()
