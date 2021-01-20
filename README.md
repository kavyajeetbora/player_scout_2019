## Soccer Player recommendation system based on player's similarity

**Objective**: Finding similar players to a given player based on [cosine similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)
<img src="player_scout_2019.gif" width="70%">

**Outline of the project** - 
1. Convert the player features to standardised vectors. Player features are based on [FIFA 19 dataset](https://www.kaggle.com/karangadiya/fifa19)
2. Find out the similarity or the cosine angle between the two vectors (of players), smaller the angle more is the similarity. The cosine similarity formula between two vectors is shown below: 
<img src="https://neo4j.com/docs/graph-algorithms/current/images/cosine-similarity.png" width="50%">
where A and B are the two vectors of nth dimension.


3. Based on the similarity scores, output the top 30 players

[Run the notebook on Google Colaboratory](https://colab.research.google.com/github/kavyajeetbora/player_scout_2019/blob/master/data/Similar_players.ipynb)
