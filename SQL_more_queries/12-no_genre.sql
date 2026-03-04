-- Write a SQL script that lists all the shows without genres
SELECT tv_show.title, tv_show_genres.genre_id
FROM tv_show
LEFT JOIN tv_show_genres 
ON tv_show.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_show.title ASC, tv_show_genres.genre_id ASC;
