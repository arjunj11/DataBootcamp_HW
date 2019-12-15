import pandas as pd
from flask import Flask, jsonify
cities_df=pd.read_csv('Resources/cities.csv')
city_df=cities_df.set_index('City_ID')

app=Flask(__name__)

app.route('/')
def home():
    return (index.html)
