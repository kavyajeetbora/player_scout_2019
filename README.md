## Soccer Player recommendation system based on player's similarity

**Objective**: Finding similar players to a given player based on [cosine similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)

This is a short demo showing how the web application works:

![presentation](https://user-images.githubusercontent.com/38955297/192730749-e59780c3-36c9-420a-b9f4-d1dd021fd219.gif)

**Outline of the project** - 
1. Convert the player features to standardised vectors. Player features are based on [FIFA 19 dataset](https://www.kaggle.com/karangadiya/fifa19)
2. Find out the similarity or the cosine angle between the two vectors (of players), smaller the angle more is the similarity. The cosine similarity formula between two vectors is shown below: 

<img src = "https://miro.medium.com/max/720/1*IhpY-6LYV75983THCpWo-w.png" height=300 align="center"/>

$similarity(A,B) = cos(\theta) = \frac{A \cdot B}{\|A\|\|B\|}$

where A and B are the two vectors of nth dimension.

**The similarity of two vectors is measured by the cosine of the angle between them:**

The similarity can take values between -1 and +1. Smaller angles between vectors produce larger cosine values, indicating greater cosine similarity. For example:

- When two vectors have the same orientation, the angle between them is 0, and the cosine similarity is 1.
- Perpendicular vectors have a 90-degree angle between them and a cosine similarity of 0.
- Opposite vectors have an angle of 180 degrees between them and a cosine similarity of -1.
<img src="https://storage.googleapis.com/lds-media/images/cosine-similarity-vectors.original.jpg" height=300>

3. Based on the similarity scores, output the top 30 players

[Run the notebook on Google Colaboratory](https://colab.research.google.com/github/kavyajeetbora/player_scout_2019/blob/master/data/Similar_players.ipynb)
