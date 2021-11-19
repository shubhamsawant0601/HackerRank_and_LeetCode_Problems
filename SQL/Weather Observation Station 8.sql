# Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your # result cannot contain duplicates.

select distinct(city) from station 
where substring(city, 1,1) in ("a", "i", "e", "o", "u") and substring(city, length(city),1) in ("a", "i", "e", "o", "u")

