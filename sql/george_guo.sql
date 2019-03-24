USE sakila;

-- 1.a
SELECT first_name, last_name FROM actor;
-- 1.b
SELECT concat(UPPER(first_name), ' ', UPPER(last_name)) AS `Actor Name` FROM actor;

-- 2.a
SELECT actor_id, first_name, last_name FROM actor WHERE first_name = "Joe";
-- 2.b
SELECT * FROM actor WHERE last_name LIKE '%GEN%';
-- 2.c
SELECT * FROM actor WHERE last_name LIKE '%LI%' ORDER BY last_name, first_name;
-- 2.d
SELECT country_id, country FROM country WHERE country IN ("Afghanistan", "Bangladesh", "China");

-- 3.a
ALTER TABLE actor ADD description BLOB;
-- 3.b
ALTER TABLE actor DROP description;

-- 4.a
SELECT last_name, count(*) AS actor_num FROM actor GROUP BY last_name;
-- 4.b
SELECT * FROM (SELECT last_name, count(*) AS actor_num FROM actor GROUP BY last_name) g WHERE g.actor_num >= 2;
-- 4.c
UPDATE actor SET first_name = "HARPO" WHERE first_name = "GROUCHO" AND last_name = "WILLIAMS";
-- 4.d
UPDATE actor SET first_name = "GROUCHO" WHERE first_name = "HARPO" AND last_name = "WILLIAMS";

-- 5.a
SHOW CREATE TABLE address;

-- 6.a
SELECT s.first_name, s.last_name, a.address FROM staff s LEFT JOIN address a USING (address_id);
-- 6.b
SELECT s.staff_id, SUM(p.amount) AS total_amount FROM staff s RIGHT JOIN payment p USING (staff_id)
WHERE p.payment_date LIKE "2005-08%" GROUP BY staff_id;
-- 6.c
SELECT f.film_id, f.title, count(*) AS actor_num FROM film f INNER JOIN film_actor a USING (film_id) GROUP BY film_id;
-- 6.d
SELECT Count(*) AS copies FROM inventory WHERE film_id = (SELECT film_id FROM film WHERE title = "Hunchback Impossible");
-- 6.e
SELECT c.first_name, c.last_name, SUM(p.amount) AS `Total Amount Paid` 
FROM customer c LEFT JOIN payment p USING (customer_id)
GROUP BY customer_id
ORDER BY last_name;

-- 7.a
SELECT title FROM film WHERE title LIKE "K%" OR title LIKE "Q%";
-- 7.b
SELECT first_name, last_name FROM actor WHERE actor_id IN 
	(SELECT actor_id FROM film_actor WHERE film_id = 
		(SELECT film_id FROM film WHERE title = "Alone Trip"));
-- 7.c
SELECT c.first_name, c.last_name, c.email 
FROM customer c 
LEFT JOIN address a USING(address_id) 
WHERE a.city_id IN 
	(SELECT city_id FROM city WHERE country_id = 
		(SELECT country_id FROM country WHERE country = "Canada"));
-- 7.d
select * from country;
-- 7.e
SELECT f.title, f.film_id, count(i.inventory_id) as rental_time 
FROM inventory i 
LEFT JOIN film f USING(film_id) 
GROUP BY f.film_id 
ORDER BY rental_time DESC;
-- 7.f
SELECT s.store_id, sum(p.amount) as Total_amount 
FROM payment p
LEFT JOIN customer c USING(customer_id)
LEFT JOIN store s USING(store_id)
GROUP BY s.store_id
ORDER BY Total_amount DESC;
-- 7.g
SELECT s.store_id, ci.city, cu.country  FROM store s 
LEFT JOIN address a USING(address_id)
LEFT JOIN city ci USING(city_id)
LEFT JOIN country cu USING(country_id);
-- 7.h


-- 8.a

-- 8.b

-- 8.c


