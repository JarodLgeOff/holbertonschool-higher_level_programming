-- Write a SQL script that lists all the shows and their genres
SELECT tv_show.title, tv_show_genres.genre_id
FROM tv_show
JOIN tv_show_genres 
ON tv_show.id = tv_show_genres.show_id
ORDER BY tv_show.title ASC, tv_show_genres.genre_id ASC;