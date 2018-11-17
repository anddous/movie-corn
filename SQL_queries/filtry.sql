--TYPY ŽÁNRÙ
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
select m.originalTitle, e.seasonNumber
from imdb.Movie as m
left join imdb.Episode as e 
on m.tconst = e.tconst
where e.seasonNumber > 0;

--jméno filmu
select top 100 m.originalTitle, m.genres, r.region, m.titleType
from imdb.Movie as m 
join imdb.Region as r 
on r.titleId = m.tconst
where m.titleType like '%videoGame%';
--where m.originalTitle like '%Julius Caesar%'






