select distinct top 50 r.title, m.startYear, r.region, rat.averageRating, e.seasonNumber, p.primaryName
from imdb.Movie as m
join imdb.Region as r 
on r.titleId = m.tconst
join imdb.Rating as rat
on rat.tconst = m.tconst 
left join imdb.Episode as e
on m.tconst = e.tconst
left join imdb.Writer as w
on m.tconst = w.tconst
left join imdb.Person as p
on w.nconst = p.nconst
where m.startYear >= 1950
and m.startYear <= 2018
and r.region in ('CZ', 'SK', 'GB', 'US')
-- @category parametr - obsahuje aspoò jednu za kagorií
and m.genres like '%crime%'
-- @runtime parametr - délka
and m.runtimeMinutes > 100
and m.runtimeMinutes < 120
-- @movie_type 
and e.seasonNumber is  null
-- @rating
and rat.averageRating >= 7.0
and rat.averageRating <= 10.0;
