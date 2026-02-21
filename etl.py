import pandas as pd
import requests
import sqlite3
import time


# 1. READ CSV FILES


movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# 2. CONNECT TO SQLITE DATABASE


conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

# Run schema.sql to create tables
with open("schema.sql", "r") as f:
    conn.executescript(f.read())


# 3. OMDb API DETAILS


API_KEY = "401d78ec"   # Your API key

def fetch_movie_data(title):
    """Fetch director, plot, box office from OMDb."""
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    response = requests.get(url).json()

    if response.get("Response") == "True":
        return (
            response.get("Director"),
            response.get("Plot"),
            response.get("BoxOffice")
        )
    return None, None, None


# 4. ENRICH MOVIES WITH API DATA


directors = []
plots = []
box_offices = []

print("Fetching movie details from OMDb API...")

for index, row in movies.iterrows():
    title = row["title"]

    director, plot, box_office = fetch_movie_data(title)
    directors.append(director)
    plots.append(plot)
    box_offices.append(box_office)

    print(f"{index+1}/{len(movies)} fetched: {title}")
    time.sleep(0.2) 

movies["director"] = directors
movies["plot"] = plots
movies["box_office"] = box_offices


# 5. LOAD DATA INTO DATABASE (IDEMPOTENT)



cursor.execute("DELETE FROM movies")
cursor.execute("DELETE FROM ratings")
conn.commit()


movies.drop_duplicates(subset=["movie_id"], inplace=True)
ratings.drop_duplicates(subset=["user_id", "movie_id"], inplace=True)


movies.to_sql("movies", conn, if_exists="append", index=False)
ratings.to_sql("ratings", conn, if_exists="append", index=False)

conn.commit()
conn.close()


print("ETL Pipeline Completed Successfully!")
