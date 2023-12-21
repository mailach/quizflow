CREATE STREAM questions_stream (
    id VARCHAR KEY,
    round INT,
    text VARCHAR,
    type VARCHAR,
    options ARRAY<VARCHAR>,
    correctAnswer INT,
    points INT,
    deleted INT
) WITH (
    KAFKA_TOPIC = 'create-questions',
    VALUE_FORMAT = 'JSON'
);


CREATE TABLE QUESTIONS_TABLE WITH (KAFKA_TOPIC='question-table', PARTITIONS=1, REPLICAS=1) AS 
SELECT
  QUESTIONS_STREAM.ID ID,
  LATEST_BY_OFFSET(QUESTIONS_STREAM.TEXT) AS TEXT,
  LATEST_BY_OFFSET(QUESTIONS_STREAM.OPTIONS) AS OPTIONS,
  LATEST_BY_OFFSET(QUESTIONS_STREAM.ROUND) AS ROUND,
  LATEST_BY_OFFSET(QUESTIONS_STREAM.CORRECTANSWER) AS CORRECTANSWER,
  LATEST_BY_OFFSET(QUESTIONS_STREAM.POINTS) AS POINTS,
  LATEST_BY_OFFSET(QUESTIONS_STREAM.DELETED) AS DELETED,
  LATEST_BY_OFFSET(QUESTIONS_STREAM.TYPE) AS TYPE
FROM QUESTIONS_STREAM QUESTIONS_STREAM
GROUP BY QUESTIONS_STREAM.ID
EMIT CHANGES;