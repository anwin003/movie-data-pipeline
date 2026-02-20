# Movie Data Pipeline – Data Engineering Assignment (tsworks)

This project is a complete end-to-end ETL pipeline that processes movie data from two different sources, enriches it using an external API, stores it in a relational database, and answers analytical questions using SQL.

This assignment was completed as part of the tsworks Data Engineer (0–1 years) selection process.

---

## 📌 **Project Overview**

The goal of this project is to:

1. Ingest movie data from:
   - MovieLens Dataset (movies.csv, ratings.csv)
   - OMDb API (for Director, Plot, Box Office)
2. Transform & clean the data
3. Enrich movie metadata using the external API
4. Load the final dataset into a relational database (SQLite)
5. Write SQL queries to answer analytical questions

---

## 📁 **Project Structure**
moviepro/
│── etl.py
│── schema.sql
│── queries.sql
│── README.md
│
└── data/
│── movies.csv
│── ratings.csv


## 🚀 **How to Run the Project**

### **1. Install dependencies**
Run:


### **2. Download MovieLens dataset**
Download from:  
https://grouplens.org/datasets/movielens/latest/  
Extract and place **movies.csv** and **ratings.csv** inside the `/data` folder.

### **3. Get OMDb API key**
Sign up at:  
http://www.omdbapi.com/apikey.aspx

Add the API key inside **etl.py**:

```python
API_KEY = "your_api_key_here"


python etl.py




Extract

Load movies.csv & ratings.csv using pandas

Transform

Clean missing values

Remove duplicates

Call OMDb API to fetch:

Director

Plot

Box Office

Load

Connect to SQLite database

Clear previous data (idempotent)

Insert clean, enriched movie & rating records



📊 SQL Queries

All analytical queries are inside queries.sql:

Movie with the highest average rating

Top 5 genres with highest average rating

Director with the most movies

Average movie rating per year

Run queries inside any SQLite viewer or Python.

🧠 Design Choices & Assumptions

SQLite was chosen for convenience and simplicity.

Movie titles were used for API lookup (OMDb supports title-based search).

A delay was added between API requests to avoid rate limiting.

ETL is idempotent, meaning running it multiple times will NOT duplicate data.

Genre parsing was kept simple for this assignment.

