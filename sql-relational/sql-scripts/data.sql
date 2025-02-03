INSERT INTO users (name, email) VALUES 
('John Doe', 'john@example.com'),
('Jane Smith', 'jane@example.com');

INSERT INTO products (name, price) VALUES 
('Laptop', 1000.00),
('Mouse', 20.00);

INSERT INTO orders (user_id) VALUES (1);

INSERT INTO order_items (order_id, product_id, quantity) VALUES 
(1, 1, 1),
(1, 2, 2);