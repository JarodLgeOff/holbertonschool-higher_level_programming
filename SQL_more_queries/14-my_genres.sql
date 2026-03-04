-- Write a SQL query that lists all genres of the TV show “Dexter” in alphabetical order
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres 
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_shows.title = 'Dexter' and tv_show_genres.genre_id IS NOT NULL
ORDER BY tv_genres.name ASC;