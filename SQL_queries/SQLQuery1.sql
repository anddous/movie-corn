use MovieCorn
go


alter procedure dbo.usp_GetMovies(@yearFrom int, @yearTo int)
as
begin

select distinct top 6 r.title as movie
from imdb.Movie m
join imdb.Region r on r.titleId = m.tconst
where m.startYear >= @yearFrom
and m.startYear <= @yearTo
--and r.[region] in ('CZ')
and r.[language] = 'cs'
--and m.genres like '%'+@category+'%'

end

select * from imdb.Region r where r.title like '%na zabití 2%'