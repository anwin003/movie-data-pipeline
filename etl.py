import pandas as pd
import requests
import sqlite3
import time


movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")


conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

with open("schema.sql", "r") as f:
    conn.executescript(f.read())



API_KEY = "401d78ec"

def fetch_movie_data(title):
     url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"

    try:
        response = requests.get(url).json()
    except:
        return None, None, None  

    if response.get("Response") == "True":
        return (
            response.get("Director"),
            response.get("Plot"),
            response.get("BoxOffice")
        )

    return None, None, None  




movies.rename(columns={"movieId": "movie_id"}, inplace=True)
ratings.rename(columns={"movieId": "movie_id", "userId": "user_id"}, inplace=True)


movies.drop_duplicates(subset=["movie_id"], inplace=True)
ratings.drop_duplicates(subset=["user_id", "movie_id"], inplace=True)


movies["director"] = None
movies["plot"] = None
movies["box_office"] = None



print("Fetching additional movie details from OMDb API...")

for index, row in movies.iterrows():

    title = row["title"]

   
    if "(" in title and title.endswith(")"):
        clean_title = title.rsplit("(", 1)[0].strip()
    else:
        clean_title = title

    director, plot, box_office = fetch_movie_data(clean_title)

    movies.at[index, "director"] = director
    movies.at[index, "plot"] = plot
    movies.at[index, "box_office"] = box_office

    time.sleep(0.2)  




movies = movies[["movie_id", "title", "genres", "director", "plot", "box_office"]]


cursor.execute("DELETE FROM movies")
cursor.execute("DELETE FROM ratings")
conn.commit()


movies.to_sql("movies", conn, if_exists="append", index=False)
ratings.to_sql("ratings", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("ETL Pipeline Completed Successfully!")

