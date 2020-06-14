#!/usr/bin/env python
# coding: utf-8

from flask import Flask, jsonify, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

movie_name_index_df=pd.read_csv("movie_user_rating_index.csv",encoding ='utf-8',compression='gzip')

movie_user_rating_df=pd.read_csv("movie_user_rating_pivottable.csv",
                                         encoding ='utf-8',compression='gzip')

move_review_final_df = pd.read_csv("move_review_final_dataset.csv",
                                                 encoding='utf-8',compression='gzip')

model_knn = pickle.load( open( "collaborativeFiltering_model.pkl", "rb" ) )

model_classifier = pickle.load( open( "collaborativeFiltering_NLP_model.pkl", "rb" ) )

vectorizer = pickle.load(open("collaborativeFiltering_NLP_vectorizer.pkl", 'rb'))  


# pass movie name and get movie index which can be used in recommendation modelmodel_knn
def getMovieIndex(name):
    name=name.strip().lower()
    firstValue="10 cloverfield lane".lower()
    test_vector= vectorizer.transform([name])
    predicted = model_classifier.predict(test_vector)
    
    available =   name in firstValue
    # return -1 for unavailable movies
    if((predicted[0] == 0) & (~available)):
        return -1
    else:
        return predicted[0]
    


def getRecomendedMoviesByIndex(queryIndex):
    distances, indices = model_knn.kneighbors(movie_user_rating_df.iloc[queryIndex,:].values
                                              .reshape(1,-1), n_neighbors = 11)
    return distances,indices


def recommendedMovies(name):
    movieList=list()
    query_index=getMovieIndex(name)
    if query_index == -1:
        return movieList
    
    distances, indices =getRecomendedMoviesByIndex(query_index)
    for i in range(0, len(distances.flatten())):
        movieList.append(movie_name_index_df.title[indices.flatten()[i]])
    return movieList

def moveieReviewsByYear(year):
    movieList=move_review_final_df.query('year == @year')
    json=movieList.to_json(orient = "records")
    return json 

def moveieReviewsByName(name):
    name=name.strip().lower()
    movieList= move_review_final_df[move_review_final_df["title"].str.contains(name)]
    json=movieList.to_json(orient = "records")
    return json 

def moveieReviewsByGenres(genres):
    genres=genres.strip().lower()
    movieList= move_review_final_df[move_review_final_df["genres"].str.contains(genres)]
    json=movieList.to_json(orient = "records")
    return json
def moveieReviewsByGenresAndYear(genres,year):
    genres=genres.strip().lower()
    movieList= move_review_final_df[(move_review_final_df["genres"].str.contains(genres)) & (move_review_final_df["year"] == year)]
    json=movieList.to_json(orient = "records")
    return json 

@app.route('/')
def home():
    return render_template('index.html',title="Home")
@app.route('/index.html')
def index():
    return render_template('index.html',title="Home")
@app.route('/about.html')
def about():
    return render_template('about.html',title="About")
@app.route('/review.html')
def review():
    return render_template('review.html',title="Review")
@app.route('/contact.html')
def contact():
    return render_template('contact.html',title="Contact")


@app.route('/api/movierecommendname', methods=['GET'])
def movieListByRecommendation():
    name = request.args['name']
    movieList=list()
    try:
        movieList=recommendedMovies(name)
    except:
       # print("{0} - Movie Not found".format(name))
        movieList.append(name)
    return jsonify(movieList)

@app.route('/api/moviereviewyear', methods=['GET'])
def movieListByYear():
    year = request.args['year']
    return moveieReviewsByYear(year)
   

@app.route('/api/moviereviewname', methods=['GET'])
def movieListByName():
    name = request.args['name']
    return moveieReviewsByName(name)

@app.route('/api/moviereviewgenres', methods=['GET'])
def moveieListByGenres():
    name = request.args['name']
    return moveieReviewsByGenres(name)

@app.route('/api/moviereviewgenresyear', methods=['GET'])
def moveieListByGenresAndYear():
    name = request.args['name']
    year = int(request.args['year'])
    return moveieReviewsByGenresAndYear(name,year)

if __name__ == '__main__':
   app.run(port=5003)






