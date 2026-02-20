SELECT m.title, AVG(r.rating) AS avg_rating
FROM ratings r
JOIN movies m ON r.movie_id = m.movie_id
GROUP BY r.movie_id
ORDER BY avg_rating DESC
LIMIT 1;




SELECT m.genres, AVG(r.rating) AS avg_rating
FROM ratings r
JOIN movies m ON r.movie_id = m.movie_id
GROUP BY m.genres
HAVING COUNT(*) > 5
ORDER BY avg_rating DESC
LIMIT 5;



SELECT director, COUNT(*) AS movie_count
FROM movies
WHERE director IS NOT NULL
GROUP BY director
ORDER BY movie_count DESC
LIMIT 1;



SELECT 
    strftime('%Y', datetime(timestamp, 'unixepoch')) AS year,
    AVG(rating) AS avg_rating
FROM ratings
GROUP BY year
ORDER BY year;