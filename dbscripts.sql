CREATE TABLE weather (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    temp DECIMAL(5, 2),
    humidity DECIMAL(5, 2),
    condition VARCHAR(50),
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO weather(city, temp, humidity, condition, recorded_at)
VALUES 
('New York', 22.5, 60.0, 'Sunny', '2025-05-06 08:00:00'),
('London', 18.3, 75.0, 'Cloudy', '2025-05-06 08:05:00'),
('Tokyo', 30.2, 80.5, 'Rainy', '2025-05-06 08:10:00'),
('Paris', 20.0, 65.0, 'Sunny', '2025-05-06 08:15:00'),
('Berlin', 15.6, 55.0, 'Foggy', '2025-05-06 08:20:00'),
('Sydney', 25.3, 70.0, 'Windy', '2025-05-06 08:25:00'),
('Moscow', 10.0, 50.0, 'Snowy', '2025-05-06 08:30:00'),
('Toronto', 16.5, 58.0, 'Rainy', '2025-05-06 08:35:00'),
('Mumbai', 33.0, 85.0, 'Humid', '2025-05-06 08:40:00'),
('Beijing', 28.7, 68.0, 'Cloudy', '2025-05-06 08:45:00'),
('Rio de Janeiro', 29.0, 75.0, 'Sunny', '2025-05-06 08:50:00'),
('Cape Town', 19.2, 55.0, 'Windy', '2025-05-06 08:55:00'),
('Seoul', 24.8, 60.0, 'Clear', '2025-05-06 09:00:00'),
('Rome', 21.0, 62.0, 'Sunny', '2025-05-06 09:05:00'),
('Madrid', 26.5, 50.0, 'Sunny', '2025-05-06 09:10:00'),
('Bangkok', 34.2, 90.0, 'Humid', '2025-05-06 09:15:00'),
('Istanbul', 17.5, 72.0, 'Rainy', '2025-05-06 09:20:00'),
('Dubai', 38.0, 40.0, 'Clear', '2025-05-06 09:25:00'),
('Singapore', 32.5, 85.0, 'Humid', '2025-05-06 09:30:00'),
('Los Angeles', 27.0, 65.0, 'Sunny', '2025-05-06 09:35:00');




CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    category VARCHAR(100),
    stock_quantity INT
);

CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(100),
    signup_date DATE
);


INSERT INTO customers (name, email, city, signup_date)
VALUES
('Alice Smith', 'alice@example.com', 'New York', '2023-05-10'),
('Bob Johnson', 'bob@example.com', 'Los Angeles', '2022-11-22'),
('Charlie Lee', 'charlie@example.com', 'Chicago', '2024-01-15'),
('Diana Prince', 'diana@example.com', 'Boston', '2023-09-05'),
('Evan Davis', 'evan@example.com', 'San Francisco', '2022-07-18');


INSERT INTO products (name, price, category, stock_quantity)
VALUES
('Laptop Pro 15"', 1500.00, 'Electronics', 20),
('Noise Cancelling Headphones', 200.00, 'Electronics', 50),
('Office Chair', 120.00, 'Furniture', 15),
('Coffee Maker', 80.00, 'Kitchen', 30),
('Yoga Mat', 25.00, 'Fitness', 100);
