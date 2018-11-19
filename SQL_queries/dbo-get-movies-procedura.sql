USE [MovieCorn]
GO
/****** Object:  StoredProcedure [dbo].[usp_GetMovies]    Script Date: 19.11.2018 20:19:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE procedure [dbo].[usp_GetMovies](
@yearFrom int, 
@yearTo int, 
@category nvarchar(255), 
@runtimeFrom int, 
@runtimeTo int, 
@movieType nvarchar(255), 
@ratingFrom int, 
@ratingTo int)
as
begin

select distinct top 6 r.title as movie, m.startYear as rok, r.region as country, rat.averageRating as stars, m.genres as genre
from imdb.Movie as m
join imdb.Region as r 
	on r.titleId = m.tconst
join imdb.Rating as rat
	on rat.tconst = m.tconst 
left join imdb.Episode as e
	on m.tconst = e.tconst
-- ASI NENÍ TŘEBA PŘIPOJOVAT - VEZMEME Z API
--left join imdb.Writer as w
--on m.tconst = w.tconst
--left join imdb.Person as p
--on w.nconst = p.nconst
where (@yearFrom is null or m.startYear >= @yearFrom)

and (@yearTo is null or m.startYear <= @yearTo)
and r.region in ('CZ', 'SK', 'GB', 'US')
-- @category parametr - obsahuje aspoň jednu za kagorií
and (@category is null or m.genres like '%'+@category+'%')


and (@runtimeFrom is null or m.runtimeMinutes > @runtimeFrom)
and (@runtimeTo is null or m.runtimeMinutes < @runtimeTo)
and 
(
	(@movieType is null)
	or
	(@movieType = 'film' and e.seasonNumber is null)
	or
	(@movieType = 'serial' and e.seasonNumber is not null)
)
and (@ratingFrom is null or rat.averageRating >= @ratingFrom)
and (@ratingTo is null or rat.averageRating <= @ratingTo)
and m.titleType in ('movie', 'tvMovie', 'tvEpisode')

end

