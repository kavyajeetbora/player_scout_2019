import pandas as pd
import numpy as np
import json

### create global variables
__players = None
__attributes = None
__basic_df = None
__player_names = None


def cosine_similarity(vec1,vec2):
    '''
    Returns the cosine similarity between two vectors of n dimension
    '''
    a = np.array(vec1).ravel()
    b = np.array(vec2).ravel()
    denom = np.sqrt(np.sum(np.square(vec1))) * np.sqrt(np.sum(np.square(vec2)))
    return np.round(np.dot(a,b) / denom * 100, 2)

def load_saved_artifacts():

    print('Loading artifacts')

    global __players
    global __attributes
    global __basic_df
    global __player_names

    with open('artifacts/players.json','r') as json_file:
        __players = json.load(json_file)   ## this will return a python dictionary
        __basic_df = pd.DataFrame.from_dict(data=__players, orient='index')
        __basic_df.index = __basic_df.index.astype(int)
        __player_names = list(__basic_df.iloc[:,0].values)
    with open('artifacts/players_attributes.json','r') as json_file:
        __attributes = json.load(json_file) ## python dictionary
        ## # WARNING:  in __attributes dictionary the key is string by default

def get_all_player_names():
    return __player_names

def similar_players(index=0,top=10):
    '''
    This function returns the cosine similarity score for a given players
    takes the player index as input and the num players to be displayed
    '''
    similarity_scores = {}
    for k,v in __attributes.items():
        similarity_scores[int(k)] = cosine_similarity(__attributes[str(index)],v)
    similarity_scores = sorted(similarity_scores.items(), key = lambda item: item[1], reverse=True)
    return similarity_scores[1:top+1]

def get_index(player):
    '''
    This function takes the player name and returns the index
    '''
    index = __basic_df[__basic_df.iloc[:,0]==player].index.values[0]
    return index

def display_similar_players(player,top):
    '''
    This function displays the top similar players with basic basic_info
    and return as python dictionary
    '''
    index = get_index(player)
    top_sim_players = similar_players(index=int(index),top=int(top))

    top_players = {}
    for i,(index,similarity) in enumerate(top_sim_players):
        print(index)
        info = list(__basic_df.iloc[index,[0,4,9,10]].values)
        info.insert(len(info),similarity)
        top_players[i] = info

    return top_players

if __name__ == "__main__":
    load_saved_artifacts()
    print(display_similar_players('De Gea',10))
