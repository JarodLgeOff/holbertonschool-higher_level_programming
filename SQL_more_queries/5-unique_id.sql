-- Create a table named force_name with the following columns
CREATE TABLE IF NOT EXISTS force_name (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(255) NOT NULL
);