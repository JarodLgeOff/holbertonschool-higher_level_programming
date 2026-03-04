-- Write a SQL script that lists all the TV shows in the database that have the genre “Comedy”
SELECT tv_show.title
FROM tv_shows
JOIN tv_show_genres 
ON tv_shows.id = tv_show_genres.tv_show_id
JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_show.title ASC;
