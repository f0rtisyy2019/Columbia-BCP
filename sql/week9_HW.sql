USE sakila;

-- 1.a Display the first and last names of all actors from the table actor.
SELECT first_name, last_name FROM actor;

-- 1.b Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name
SELECT concat(UPPER(first_name), ' ', UPPER(last_name)) AS `Actor Name` FROM actor;

-- 2.a You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." 
SELECT actor_id, first_name, last_name FROM actor WHERE first_name = "Joe";

-- 2.b Find all actors whose last name contain the letters GEN:
SELECT * FROM actor WHERE last_name LIKE '%GEN%';

-- 2.c Find all actors whose last names contain the letters LI, order the rows by last name and first name
SELECT * FROM actor WHERE last_name LIKE '%LI%' ORDER BY last_name, first_name;

-- 2.d Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT country_id, country FROM country WHERE country IN ("Afghanistan", "Bangladesh", "China");

-- 3.a create a column in the table actor named description and use the data type BLOB
ALTER TABLE actor ADD description BLOB;

-- 3.b Delete the description column.
ALTER TABLE actor DROP description;

-- 4.a List the last names of actors, as well as how many actors have that last name.
SELECT last_name, count(*) AS actor_num FROM actor GROUP BY last_name;

-- 4.b List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
SELECT last_name, count(*) AS actor_num FROM actor GROUP BY last_name HAVING actor_num >= 2;

-- 4.c The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.
UPDATE actor SET first_name = "HARPO" WHERE first_name = "GROUCHO" AND last_name = "WILLIAMS";

-- 4.d Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO.
UPDATE actor SET first_name = "GROUCHO" WHERE first_name = "HARPO" AND last_name = "WILLIAMS";

-- 5.a You cannot locate the schema of the address table. Which query would you use to re-create it?
SHOW CREATE TABLE address;

-- 6.a Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
SELECT s.first_name, s.last_name, a.address FROM staff s LEFT JOIN address a USING (address_id);

-- 6.b Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
SELECT s.staff_id, SUM(p.amount) AS total_amount FROM staff s RIGHT JOIN payment p USING (staff_id)
WHERE p.payment_date LIKE "2005-08%" GROUP BY staff_id;

-- 6.c List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
SELECT f.film_id, f.title, count(*) AS actor_num FROM film f INNER JOIN film_actor a USING (film_id) GROUP BY film_id;

-- 6.d How many copies of the film Hunchback Impossible exist in the inventory system?
SELECT count(*) AS copies FROM inventory WHERE film_id = (SELECT film_id FROM film WHERE title = "Hunchback Impossible");

-- 6.e Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
SELECT c.first_name, c.last_name, SUM(p.amount) AS `Total Amount Paid` 
FROM customer c LEFT JOIN payment p USING (customer_id)
GROUP BY customer_id
ORDER BY last_name;

-- 7.a The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity. Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
SELECT title FROM film
JOIN language USING(language_id)
WHERE name = "English"
and (title LIKE "K%" OR title LIKE "Q%");

-- 7.b Use subqueries to display all actors who appear in the film Alone Trip.
SELECT first_name, last_name FROM actor WHERE actor_id IN 
	(SELECT actor_id FROM film_actor WHERE film_id = 
		(SELECT film_id FROM film WHERE title = "Alone Trip"));
        
-- 7.c You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
SELECT c.first_name, c.last_name, c.email 
FROM customer c 
LEFT JOIN address a USING(address_id) 
WHERE a.city_id IN 
	(SELECT city_id FROM city WHERE country_id = 
		(SELECT country_id FROM country WHERE country = "Canada"));
        
-- 7.d Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as family films.
SELECT title, description, rating FROM film_list WHERE category = "Family";

-- 7.e Display the most frequently rented movies in descending order.
SELECT f.title, f.film_id, count(i.inventory_id) as rental_time 
FROM inventory i 
LEFT JOIN film f USING(film_id) 
GROUP BY f.film_id 
ORDER BY rental_time DESC;

-- 7.f Write a query to display how much business, in dollars, each store brought in.
SELECT s.store_id, sum(p.amount) as Total_amount 
FROM payment p
LEFT JOIN customer c USING(customer_id)
LEFT JOIN store s USING(store_id)
GROUP BY s.store_id
ORDER BY Total_amount DESC;

-- 7.g Write a query to display for each store its store ID, city, and country.
SELECT s.store_id, ci.city, cu.country  FROM store s 
LEFT JOIN address a USING(address_id)
LEFT JOIN city ci USING(city_id)
LEFT JOIN country cu USING(country_id);

-- 7.h List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT c.name AS category, SUM(p.amount) AS total_sales
FROM payment p
INNER JOIN rental r USING(rental_id)
INNER JOIN inventory i USING(inventory_id)
INNER JOIN film f USING(film_id)
INNER JOIN film_category fc USING(film_id)
INNER JOIN category c USING(category_id)
GROUP BY c.name
ORDER BY total_sales DESC;

-- 8.a In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
CREATE VIEW top_five_genres AS
SELECT c.name AS category, SUM(p.amount) AS total_sales
FROM payment p
INNER JOIN rental r USING(rental_id)
INNER JOIN inventory i USING(inventory_id)
INNER JOIN film f USING(film_id)
INNER JOIN film_category fc USING(film_id)
INNER JOIN category c USING(category_id)
GROUP BY c.name
ORDER BY total_sales DESC
LIMIT 5;

-- 8.b How would you display the view that you created in 8a?
SELECT * FROM top_five_genres;

-- 8.c You find that you no longer need the view top_five_genres. Write a query to delete it.
DROP VIEW if exists top_five_genres;
