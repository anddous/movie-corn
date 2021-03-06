USE [MovieCorn]
GO
/****** Object:  StoredProcedure [dbo].[usp_GetMovies]    Script Date: 21.11.2018 1:43:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

alter procedure [dbo].[usp_GetMovies](
@yearFrom int, 
@yearTo int, 
@category nvarchar(255), 
@runtimeFrom int, 
@runtimeTo int, 
@movieType nvarchar(255), 
@ratingFrom int, 
@ratingTo int,
@tconst nvarchar(255))
as
begin
SELECT top 6 * FROM (
   select distinct  r.title as movie, m.startYear as startY, r.region as country, rat.averageRating as stars, m.genres as genre, m.runtimeMinutes as runMin, m.titleType as tType, m.tconst as tconst 
from imdb.Movie as m
join imdb.Region as r 
	on r.titleId = m.tconst
join imdb.Rating as rat
	on rat.tconst = m.tconst 
left join imdb.Episode as e
	on m.tconst = e.tconst

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
and (@ratingFrom is null or rat.averageRating > @ratingFrom)
and (@ratingTo is null or rat.averageRating <= @ratingTo)
and m.titleType in ('movie', 'tvMovie', 'tvEpisode')
--and @tconst = m.tconst
 
) as t
ORDER BY NEWID()

end

