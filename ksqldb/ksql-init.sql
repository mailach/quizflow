CREATE STREAM questions_stream (
    id VARCHAR KEY,
    text VARCHAR,
    options ARRAY<VARCHAR>,
    correctAnswer INT,
    points INT
) WITH (
    KAFKA_TOPIC = 'create-questions',
    VALUE_FORMAT = 'JSON'
);


CREATE TABLE questions_table AS
SELECT 
    id, 
    text, 
    options, 
    correctAnswer, 
    points
FROM questions_stream
GROUP BY id;
