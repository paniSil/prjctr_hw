create table host(
	host_id int primary key,
	first_name varchar(100),
	e_mail varchar(100),
	phone_number bigint,
	host_rating float,
	summary varchar(200),
	account_balance float,
	room_id int
	);
	
create table room(
	room_id int primary key,
	room_title varchar(100),
	available_dates text,
	adress varchar(100),
	accomodation_type varchar(50),
	bedroom_quantity int,
	pet_friendly char,
	wifi char,
	kitchen char,
	extras varchar(200),
	host_id int references host(host_id)
	);

ALTER TABLE host
ADD CONSTRAINT fk_host_room
FOREIGN KEY (room_id) REFERENCES room(room_id);

create table quest(
	guest_id int primary key,
	first_name varchar(100),
	last_name varchar(100),
	e_mail varchar(100),
	phone_number bigint,
	guest_quantity int,
	children_quantity int,
	pets_quantity int,
	account_balance float,
	bonus_balance float,
	room_id int references room(room_id)
	);
	
CREATE TABLE review (
    review_num int primary key,
    guest_id int REFERENCES quest(guest_id),
    room_id int REFERENCES room(room_id),
    review_date varchar(11),
    room_rating float,
    reviewer_comments varchar(500),
    host_answer varchar(500)
	);

create table reservation (
	reservation_id int primary key,
	start_date varchar(11),
	end_date varchar(11),
	high_season char,
	price float,
	pre_payment_need char,
	guest_id int references quest(guest_id),
	payment_due_date varchar(11),
	room_id int references room(room_id)
	);
	
create table payment (
	receit_num int primary key,
	reservation_id int references reservation(reservation_id),
	total_sum float,
	pre_payment_sum float,
	payment_date varchar(11),
	payment_option varchar(100),
	transaction_fee float,
	refusal_reason varchar(100)
	)
	
insert into host (host_id, first_name, e_mail, phone_number, host_rating, summary, account_balance)
values (0001, 'Bilbo', 'thehobbit@gmail.com', '380680000000', 5.0, 'As a hobbit of simple tastes, I would be honored to offer my cozy hobbit-hole as a welcoming retreat for fellow travelers seeking a peaceful and restful stay in the beautiful Shire', 1200)

INSERT INTO host (host_id, first_name, e_mail, phone_number, host_rating, summary, account_balance) 
VALUES (0002, 'Sam', 'gardenerofmiddleearth@gmail.com', '380680000001', 4.8, 'As a gardener at heart, I take pride in offering a comfortable and verdant space for weary travelers to rest and recharge during their adventures in Middle Earth', 900)

UPDATE host
SET room_id = 0001
WHERE host_id = 0001; 

UPDATE host
SET room_id = 0002
WHERE host_id = 0002; 

UPDATE host
SET room_id = 0004
WHERE host_id = 0003; 

INSERT INTO host (host_id, first_name, e_mail, phone_number, host_rating, summary, account_balance)
VALUES (0003, 'Elrond', 'elrond@rivendell.com', '380680000002', 4.9, 'As the Lord of Rivendell, I offer my home as a sanctuary for travelers seeking respite from the dangers of Middle-earth, with luxurious accommodations and breathtaking views of the valley.', 25000);

INSERT INTO room (room_id, room_title, available_dates, adress, accomodation_type, bedroom_quantity, pet_friendly, wifi, kitchen, extras, host_id)
values
	(0001, 'Cozy Hobbit-Hole', '2023-05-01,2023-05-02,2023-05-03,2023-05-04,2023-05-05', 'Bag End, Hobbiton, The Shire', 'Private room in house', 1, 'N', 'Y', 'Y', 'Garden view, Fireplace, Complimentary breakfast', 0001);
	(0002, 'Rustic Cottage in the Shire', '2023-05-01,2023-05-02,2023-05-03,2023-05-04,2023-05-05', 'Bagshot Row, Hobbiton, The Shire', 'Entire house', 2, 'Y', 'Y', 'Y', 'Private garden, Mountain view, BBQ grill', 0002);
	(0003, 'Rivendell Suite', '2023-05-01,2023-05-02,2023-05-03,2023-05-04,2023-05-05', 'Rivendell, Eriador', 'Private room in castle', 1, 'N', 'Y', 'Y', 'Mountain view, Spa access, Daily maid service', 0002),
	(0004, 'Lothlórien Cottage', '2023-06-01,2023-06-02,2023-06-03,2023-06-04,2023-06-05', 'Lothlórien, Middle-earth', 'Entire cottage', 2, 'N', 'Y', 'Y', 'Forest view, Hot tub, BBQ grill', 0002);

insert into quest (guest_id, first_name, last_name, e_mail,phone_number, guest_quantity, children_quantity, pets_quantity, account_balance, bonus_balance, room_id)
VALUES 
    (0004, 'Aragorn', 'Son of Arathorn', 'aragorn@example.com', '380671234567', 2, 0, 0, 1000, 50, 0002),
    (0005, 'Gandalf', 'the Grey', 'gandalf@example.com', '380675678910', 1, 0, 1, 1500, 100, 0003),
    (0006, 'Legolas', 'Greenleaf', 'legolas@example.com', '380679111213', 2, 1, 0, 800, 20, 0001);
    
INSERT INTO review (review_num, guest_id, room_id, review_date, room_rating, reviewer_comments, host_answer) 
VALUES 
    (1, 4, 0001, '2023-05-06', 4.5, 'I had a wonderful stay at Bilbo cozy hobbit-hole. The room was clean and comfortable, and the complimentary breakfast was delicious!', 'Thank you for your kind words, I am so glad you enjoyed your stay!'),
    (2, 6, 0003, '2023-05-07', 5.0, 'Elronds Rivendell retreat was absolutely breathtaking. The room was spacious and beautifully decorated, and the views from the balcony were stunning.', 'Thank you for your positive review! It was a pleasure hosting you.'),
    (3, 5, 0001, '2023-05-08', 3.0, 'Unfortunately, my stay at Bilbo hobbit-hole was not as enjoyable as I had hoped. The room was quite small and there was a musty smell throughout the house.', 'I apologize for any inconvenience caused during your stay. I will make sure to address the issues you mentioned to ensure a better experience for future guests.');
   
INSERT INTO reservation (reservation_id, start_date, end_date, high_season, price, pre_payment_need, guest_id, payment_due_date, room_id)
VALUES
    (1, '2023-06-01', '2023-06-05', 'N', 1000, 'Y', 6, '2023-05-01', 0001),
    (2, '2023-07-10', '2023-07-15', 'Y', 1500, 'Y', 5, '2023-06-10', 0002),
    (3, '2023-08-20', '2023-08-25', 'N', 1200, 'N', 4, '2023-08-01', 0003);
   
INSERT INTO reservation (reservation_id, start_date, end_date, high_season, price, pre_payment_need, guest_id, payment_due_date, room_id)
values (4, '2023-06-01', '2023-07-06', 'N', 8000, 'Y', 6, '2023-06-01', 0003)

INSERT INTO payment (receit_num, reservation_id, total_sum, pre_payment_sum, payment_date, payment_option, transaction_fee, refusal_reason)
VALUES 
    (1001, 2, 150.00, 50.00, '2023-04-10', 'Credit card', 2.50, NULL),
    (1002, 3, 300.00, 100.00, '2023-05-01', 'PayPal', 5.00, NULL),
    (1003, 1, 450.00, 150.00, '2023-06-15', 'Bank transfer', 7.50, NULL);
    
select *
from reservation
where guest_id in (
	select guest_id
	from quest
	where first_name='Legolas'
	);
	
SELECT q.first_name, q.last_name, ro.room_title
FROM quest q
JOIN reservation r ON q.guest_id = r.guest_id
JOIN room ro ON r.room_id = ro.room_id

SELECT q.first_name, q.last_name, COUNT(*) AS num_rooms_reserved
FROM quest q
JOIN reservation r ON q.guest_id = r.guest_id
JOIN room ro ON r.room_id = ro.room_id
GROUP BY q.guest_id
ORDER BY num_rooms_reserved desc
limit 1;

SELECT q.first_name, q.last_name
FROM quest q
JOIN reservation r ON q.guest_id = r.guest_id
JOIN room ro ON r.room_id = ro.room_id
JOIN host h ON ro.host_id = h.host_id
WHERE h.host_id = '0002' AND r.start_date = '2023-07-10'
