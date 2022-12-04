CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE user_files (
    id SERIAL PRIMARY KEY,
    username TEXT,
    filename TEXT
);