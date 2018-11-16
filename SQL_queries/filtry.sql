--TYPY ��NR�
select distinct genres from imdb.Movie;

-- JAZYKY, REGION
select distinct top 60 [language], [region] from imdb.Region;

select distinct top 100 r.title as movie, r.[language]
from imdb.Movie as m
join imdb.Region as r 
on r.titleId = m.tconst
--where r.[language] in ('cs', 'uk', 'eu', 'en', 'sk');

--RUNTIME
select TOP 100 originalTitle, runtimeMinutes from imdb.Movie
where runtimeMinutes is not null
order by runtimeMinutes DESC;

--MOVIE_TYPE
select top 100 m.originalTitle as movie, seasonNumber
from imdb.Movie as m
join imdb.Episode as e 
on e.tconst = m.tconst;



