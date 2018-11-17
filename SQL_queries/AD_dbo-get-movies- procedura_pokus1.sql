use MovieCorn
go

alter procedure dbo.usp_GetMovies(@yearFrom int, @yearTo int, @category nvarchar, @runtimeFrom int, @runtimeTo int, @movieType nvarchar, @ratingFrom int, @ratingTo int)
as
begin

select distinct top 6 r.title as movie, m.startYear as startY, r.region as country, rat.averageRating as stars, m.genres as genre, m.runtimeMinutes as runMin, m.titleType as tType
from imdb.Movie as m
join imdb.Region as r 
on r.titleId = m.tconst
join imdb.Rating as rat
on rat.tconst = m.tconst 
left join imdb.Episode as e
on m.tconst = e.tconst
-- ASI NENÍ TØEBA PØIPOJOVAT - VEZMEME Z API
--left join imdb.Writer as w
--on m.tconst = w.tconst
--left join imdb.Person as p
--on w.nconst = p.nconst
where m.startYear >= @yearFrom
and m.startYear <= @yearTo
and r.region in ('CZ', 'SK', 'GB', 'US')
-- @category parametr - obsahuje aspoò jednu za kagorií
and m.genres like '%'+@category+'%'
-- @runtime parametr - délka
and m.runtimeMinutes > @runtimeFrom
and m.runtimeMinutes < @runtimeTo
-- @movie_type -- nebere dotaz s 'is null', nevíme, jak se na to zeptat
and e.seasonNumber is @movieType null
-- @rating
and rat.averageRating >= @ratingFrom
and rat.averageRating <= @ratingTo
-- omezení typu
and m.titleType in ('movie', 'tvMovie', 'tvEpisode')

end

