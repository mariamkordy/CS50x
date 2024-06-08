CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL
);
INSERT INTO users(id, username, email)
VALUES (0, "koko", "mariamkordyy@gmail.com");

SELECT * FROM users;
ALTER TABLE users
ADD COLUMN hash TEXT NOT NULL DEFAULT "hashed_password";




CREATE TABLE flashcards (
    id INTEGER PRIMARY KEY,
    question TEXT NOT NULL DEFAULT "front side",
    answer TEXT NOT NULL DEFAULT "back side"
    );

INSERT INTO flashcards(id, question, answer)
VALUES (0, "What's the capital of France?", "Paris");

SELECT * FROM flashcards;

