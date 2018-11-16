--TYPY ��NR�
select distinct genres from imdb.Movie;
/*
komedie = Comedy
krimi = crime
triller = Thriller, Adventure
horor = Mystery, Horror
animovan� = Animation
ak�n� = Action
romantika = Romance
pro dosp�l� ?

???P�idat do filtru?????
Sci-fi + Fantasy
Documentary + Biography
Music
Sport
Family
Western
War
Talk-Show
Reality-TV
*/

select distinct top 50 m.originalTitle as m, genres, [language]
from imdb.Movie as m
join imdb.Region as r 
on r.titleId = m.tconst
where m.genres like '%Comedy%'
and r.[language] in ('cs', 'uk', 'en', 'sk');