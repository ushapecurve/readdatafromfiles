/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [RecordID]
      ,[TimeStamp]
      ,[Temperature]
      ,[Hummidity]
      ,[LocationID]
  FROM [tempandhummidity].[dbo].[temperature]


  SELECT @@SERVERNAME AS SERVER_NAME