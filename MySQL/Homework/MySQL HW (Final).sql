-- Use Sakila dabatase --
USE sakila;

-- View all columns & rows from actor table --
SELECT * FROM actor;

-- View only the first name and last name columnn & all rows from 'actor' table (1a.) --
SELECT 
	first_name, 
    last_name
FROM actor;

-- View as one column the first name and last name of all rows from 'actor' table (1b.) --
SELECT CONCAT(first_name, ' ', last_name) as 'Actor Name'
FROM actor;

-- View the 3 specific columns of an actor named Joe from actor table (2a.) --
SELECT 
	actor_id, 
    first_name, 
    last_name
FROM actor
WHERE first_name = 'Joe';

-- View all actors with a last name that has the letters GEN from 'actor' table (2b.) --
SELECT 
	actor_id, 
    first_name, 
    last_name
FROM actor
WHERE last_name LIKE '%GEN%';

-- View all actors with a last name that has the letters LI, sorted by last name and first name from 'actor' table (2c.) -- 
SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name LIKE '%LI%'
ORDER BY last_name, first_name;

-- View country id of 3 specific countries from 'country table' (2d.) -- 
SELECT 
	country_id, 
    country
FROM country
WHERE country IN ('Afghanistan' , 'Bangladesh' , 'China');

-- Add column named description to 'actor' table (3a.) -- 
ALTER TABLE actor 
    ADD COLUMN description BLOB;
    
-- Delete column named description to 'actor' table (3b.) --    
 ALTER TABLE actor 
    DROP COLUMN description;
    
-- View last name count in 'actor' table (4a.) --
SELECT last_name, COUNT(*)
FROM actor
GROUP BY last_name;
    
-- View last name count in 'actor' table for only those shared by at least two actors (4b.) --     
SELECT last_name, COUNT(*)
FROM actor
GROUP BY last_name
HAVING COUNT(*) > 1;

-- View all actors with first name 'GROUCHO' and last name 'WILLIAMS' -- 
SELECT first_name, last_name
FROM actor
WHERE first_name = 'GROUCHO' AND last_name = 'WILLIAMS';

-- Update actor's first name (Groucho Williams) to Harpo (4c.) --
UPDATE actor
	SET first_name = 'HARPO'
    WHERE first_name = 'GROUCHO' AND last_name = 'WILLIAMS';
    
-- View all actors with first name 'HARPO' and last name 'WILLIAMS' -- 
SELECT first_name, last_name
FROM actor
WHERE first_name = 'HARPO' AND last_name = 'WILLIAMS';

-- Change again actor's first name to Groucho (4d.) --
UPDATE actor
	SET first_name = 'GROUCHO'
    WHERE first_name = 'HARPO' AND last_name = 'WILLIAMS';

-- View all actors with first name 'GROUCHO' and last name 'WILLIAMS' -- 
SELECT first_name, last_name
FROM actor
WHERE first_name = 'GROUCHO' AND last_name = 'WILLIAMS';

-- Show SQL script used to create table 'address' (5a.) -- 
SHOW CREATE TABLE address

-- View all columns and rows from 'staff' table -- 
SELECT * 
FROM staff;

-- View all columns and rows from 'address' table -- 
SELECT * 
FROM address;

-- View the address of the staff members  (6a.) -- 
SELECT 
	S.first_name, 
	S.last_name, 
	A.address
FROM address as A INNER JOIN staff as S ON A.address_id = S.address_id;

-- View total amount spent by staff on August of 2005 (6b.) -- 
SELECT
	S.staff_id,
	S.first_name,
	S.last_name,
SUM(P.amount)
FROM staff as S INNER JOIN payment as P ON S.staff_id = P.staff_id
WHERE P.payment_date LIKE '2005-08%'
GROUP BY S.staff_id;

-- View all columns & rows from 'film actor' table, ordered by film id column -- 
SELECT *
FROM film_actor
ORDER BY film_id;

-- View each film on the "film table' and the actor count in each film listed on the 'film actor' table (6c.) --
SELECT 
	F.film_id,
	F.title,
    COUNT(A.actor_ID) AS '# of Actors'
FROM film as F INNER JOIN film_actor as A ON F.film_id = A.film_id
GROUP BY F.film_id;

-- View inventory count of film titled 'Hunchback Impossible' (6d.) --
SELECT COUNT(film_id) AS 'Inventory count'
FROM inventory
WHERE film_id IN
    (
    SELECT film_id
    FROM film
    WHERE title = 'Hunchback Impossible'
    );
    
-- Check that film ID belongs to film titled 'Hunchback Impossible' --
SELECT film_id, title
FROM film
WHERE title = 'Hunchback Impossible'

-- Checked count of film titled 'Hunchback Impossible' using inventory ID on the inventory table -- 
SELECT *
FROM inventory
WHERE film_id = '439';   

-- View total amount paid by customer (6e.) -- 
SELECT 
C.first_name,
C.last_name,
SUM(P.amount)
FROM payment as P INNER JOIN customer as C ON P.customer_id = C.customer_id
GROUP BY P.customer_id
ORDER BY C.last_name;
 
-- View titles that start with letters K or Q and in English language (7a.) --
SELECT title, language_id
FROM film
WHERE title LIKE 'K%' OR title LIKE 'Q%'
AND language_id IN 
		(
		SELECT language_id
		FROM language
		WHERE name = 'English'
		)
        
-- Check language id of English language --
SELECT *
FROM language	

-- View actors' first and last name from the movie titled 'Alone Trip' (7b.) -- 	
SELECT first_name, last_name
FROM actor
WHERE actor_id IN
		(
		SELECT actor_id
        FROM film_actor
        WHERE film_id IN
			(
			SELECT film_id
            FROM film
            WHERE title = 'Alone Trip'
            )
		);
 
 -- View e-mails of customers living in Canada (7c.) -- 
SELECT
C.first_name,
C.last_name,
C.email,
A.district,
CY.country
FROM customer as C 
INNER JOIN address as A ON C.address_id = A.address_id
INNER JOIN city as CT on A.city_id = CT.city_id
INNER JOIN country as CY on CT.country_id = CY.country_id
WHERE CY.country = 'Canada';

-- View all movie titles that can be categorized as family movies (7d.) --
SELECT title, description, rating
FROM film
WHERE rating = 'PG-13' OR rating = 'PG' OR rating = 'G'
ORDER BY title;

-- View most frequently rented movie titles in descending order (7e.)  --
SELECT 
	F.title, COUNT(*)
FROM film as F 
INNER JOIN inventory as I ON F.film_id = I.film_id
INNER JOIN rental as R ON I.inventory_id = R.inventory_id
GROUP BY F.title
ORDER BY COUNT(*) DESC;

-- View business rental dollars generated by store (7f.) --
SELECT 
	SUM(P.amount) as 'Total rental (in $)',
	S.store_id
FROM payment as P
INNER JOIN staff as S ON P.staff_id = S.staff_id
INNER JOIN store as ST ON S.store_id = ST.store_id
GROUP BY S.store_id;

-- View store ID, city, and country (7g.) --
SELECT 
S.store_id,
C.city,
CN.country
FROM STORE as S
INNER JOIN address as A ON S.address_id = A.address_id
INNER JOIN city as C ON A.city_id = C.city_id
INNER JOIN country as CN ON C.country_id = CN.country_id;

-- View top 5 categories in gross revenues (7h.) --
SELECT
	C.name,
	SUM(P.amount) as 'Gross revenue'
FROM payment as P
INNER JOIN rental as R ON P.rental_id = R.rental_id
INNER JOIN inventory as I ON R.inventory_id = I.inventory_id
INNER JOIN film_category as FC ON I.film_id = FC.film_id
INNER JOIN category as C ON FC.category_id = C.category_id
GROUP BY C.name
ORDER BY SUM(P.amount) DESC
LIMIT 5;

-- Create view of Top 5 genres (8a.) --
CREATE VIEW Top_rev_genres AS
SELECT 
	C.name,
	SUM(P.amount) as 'Gross revenue'
FROM payment as P
INNER JOIN rental as R ON P.rental_id = R.rental_id
INNER JOIN inventory as I ON R.inventory_id = I.inventory_id
INNER JOIN film_category as FC ON I.film_id = FC.film_id
INNER JOIN category as C ON FC.category_id = C.category_id
GROUP BY C.name
ORDER BY SUM(P.amount) DESC
LIMIT 5;

-- Execute view saved on previous step (8b.) -- 
SELECT * 
FROM top_rev_genres;

-- Eliminate view created on step 8.a (8c.) -- 
DROP VIEW top_rev_genres;
