/****** Script for SelectTopNRows command from SSMS  ******/
SELECT distinct region, language
  FROM [MovieCorn].[imdb].[Region] where region = 'CZ'