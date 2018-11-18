use MovieCorn
go

alter procedure dbo.usp_GetMovies(@luckyCategory nvarchar)
as
begin

select distinct top 5 r.title as movie, m.genres as genre
from imdb.Movie as m
join imdb.Region as r 
on r.titleId = m.tconst
join imdb.Rating as rat
on rat.tconst = m.tconst 

where m.startYear >= 2010
and r.region in ('CZ', 'SK', 'GB', 'US')
---and m.genres like '%'+@category+'%'
and m.genres like '%''thriller''%'
and rat.averageRating >= 7
and m.titleType in ('movie', 'tvMovie')

end
