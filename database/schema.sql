CREATE DATABASE IF NOT EXISTS flight_db;
USE flight_db;

CREATE TABLE IF NOT EXISTS flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    source VARCHAR(50),
    origin VARCHAR(10),
    destination VARCHAR(10),
    airline VARCHAR(50),
    price INT,
    travel_date DATE,
    fetch_time DATETIME
);

CREATE INDEX idx_route
ON flights(origin, destination, travel_date);
