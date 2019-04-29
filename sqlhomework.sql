-- 1a
USE sakila;
SELECT first_name, last_name
FROM actor;
-- 1b
USE sakila;
SELECT CONCAT(first_name, ' ', last_name) AS Actor_Name
FROM actor;
-- 2a
SELECT * FROM sakila.actor;
SELECT * FROM sakila.actor WHERE first_name = "Joe";
-- 2b
SELECT * FROM sakila.actor WHERE last_name LIKE "%GEN%";
-- ac
SELECT * FROM sakila.actor WHERE last_name LIKE "%Li%" ;
-- 2d
SELECT country_id, country
FROM sakila.country 
WHERE country IN ("Afghanistan", "Bangladesh","China");
-- 3a
ALTER TABLE sakila.actor
ADD description BLOB;
-- 3b
ALTER TABLE sakila.actor
DROP COLUMN description;
-- 4a
SELECT last_name, COUNT(*)
FROM sakila.actor
GROUP BY last_name;
-- 4b
SELECT last_name, COUNT(*)
FROM sakila.actor
GROUP BY last_name
HAVING COUNT(*) > 2;
-- 4c
UPDATE sakila.actor
SET first_name = 'HARPO', last_name = 'WILLIAMS'
WHERE actor_id = 172;
-- 4d 
UPDATE sakila.actor
SET first_name = 'GROUCHO', last_name = 'WILLIAMS'
WHERE actor_id = 172;
-- 5a
-- 6a
SELECT first_name, last_name,  (SELECT address FROM sakila.address WHERE sakila.staff.address_id = sakila.address.address_id) AS 'address'  
FROM sakila.staff;
-- 6b
SELECT B.first_name, B.last_name, A.staff_id, SUM(A.amount)
FROM sakila.payment A, sakila.staff B WHERE A.staff_id = B.staff_id AND A.payment_date BETWEEN '2005-8-1' AND '2005-8-31' GROUP BY A.staff_id;
-- 6c
SELECT title, (SELECT COUNT(actor_id) FROM sakila.film_actor WHERE sakila.film_actor.film_id = sakila.film.film_id) AS 'number of actor'
FROM sakila.film;

-- 6d
SELECT film_id, (SELECT COUNT(inventory_id) FROM sakila.inventory WHERE sakila.film.film_id = sakila.inventory.film_id) AS 'number of copies'
FROM sakila.film
WHERE film_id IN (
	SELECT film_id 
    FROM sakila.film
    WHERE title = 'Hunchback Impossible'
);
-- 6e
SELECT first_name, last_name, (SELECT SUM(amount) FROM sakila.payment WHERE sakila.customer.customer_id = sakila.payment.customer_id) AS 'totla payment'
FROM sakila.customer;


-- 7a
SELECT title
FROM sakila.film
WHERE language_id IN (
SELECT language_id 
FROM sakila.language
WHERE name = 'English'
)
AND (title LIKE 'K%' OR title LIKE 'Q%');
-- 7b
SELECT first_name, last_name
FROM sakila.actor
WHERE actor_id IN (
	SELECT actor_id
	FROM sakila.film_actor
	WHERE film_id IN (
		SELECT film_id
		FROM sakila.film 
		WHERE title = 'Alone trip'
	)
);
-- 7c
SELECT first_name, last_name, email
FROM sakila.customer
WHERE address_id IN (
	SELECT address_id
    FROM sakila.address
    WHERE city_id IN (
		SELECT city_id
        FROM sakila.city
        WHERE country_id IN (
			SELECT country_id 
            FROM sakila.country
            WHERE country = 'Canada'
		)
	)
);
-- 7d
SELECT title 
FROM sakila.film
WHERE film_id IN (
	SELECT film_id 
    FROM sakila.film_category
    WHERE category_id IN (
		SELECT category_id 
        FROM sakila.category
        WHERE name = 'Family'
	)
);
-- 7e
SELECT title
FROM sakila.film
ORDER BY rental_rate DESC;






	
    





