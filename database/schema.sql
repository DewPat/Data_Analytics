CREATE DATABASE IF NOT EXISTS flight_db;
USE flight_db;

CREATE TABLE IF NOT EXISTS flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    origin VARCHAR(10),
    destination VARCHAR(10),
    airline VARCHAR(50),
    platform VARCHAR(50),
    price INT,
    flight_date DATE,
    flight_time TIME
);

CREATE INDEX idx_route
ON flights(origin, destination, flight_date);