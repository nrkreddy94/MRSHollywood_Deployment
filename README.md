# Movie Recommendation System

### Movie Recommendation System with Cosine Similiarty

URL: http://mrshollywood.herokuapp.com/index.html

Homepage | MovieReviews 
-------- | ------------ 
 ![Homepage](/webpage_home.PNG)   | ![MovieReviews](/webpage_moviereviews.PNG) 

### Life cycle of Data Science Project

1. Data Gathering - ( example: collect data from Kaggel )
2. Data Analysis - ( Analyze the data and find the relationship among the tables )
3. Feature Engineering - ( Fix missing values, Temporal, Categorical variables, Standardization, Normalization ) 
4. Feature Selection - ( Extract features which are necessary and imporve the perfomance respect to output )
5. Model building - ( creat a model which suites to our requirements )
6. Train the model
7. Save the model as pickle file - (.pkl)
8. Create a web application with Flask Microservices Framework
9. Read the pickle file in the python flask file and predict the output of model
10. Deploy the webapplication and model in the could servers

From the above Life cycle of  Datascience project, Steps 1 to 7 are implemented in MRSHollywood_Develpment project. Steps 8 to 10 are implemented in MRSHollywood_Deployment.


Flask web application is implemented with set of controllers and UI pages. html pages are available in  templates folder and all style and js files are in static folder. Rest Controllers are in app.py.

This application is deployed in [Heroku](https://dashboard.heroku.com/) cloud server. During deployment time need to specify all requried libraries in requirments.txt and Procfile.file tells what is our application starting point here app.py is starting point.


```python
web: gunicorn app:app --timeout 90
```

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.

### Useful Links

[MRSHollywood_Development](https://github.com/nrkreddy94/MRSHollywood_Development)

[MRSHollywood_Android](https://github.com/nrkreddy94/MRSHollywood_Android )

[MRSHollywood_LiveChat](https://github.com/nrkreddy94/MRSHollywood_LiveChat)


