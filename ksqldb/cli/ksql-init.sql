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
    KAFKA_TOPIC = 'question',
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



CREATE STREAM ROUNDS_STREAM (
    id VARCHAR KEY,
    title VARCHAR,
    active VARCHAR
) WITH (
    KAFKA_TOPIC = 'create-round',
    VALUE_FORMAT = 'JSON'
);


CREATE TABLE ROUNDS_TABLE WITH (KAFKA_TOPIC='round-table', PARTITIONS=1, REPLICAS=1) AS 
SELECT
  ROUNDS_STREAM.ID ID,
  LATEST_BY_OFFSET(ROUNDS_STREAM.TITLE) AS TITLE,
  LATEST_BY_OFFSET(ROUNDS_STREAM.ACTIVE) AS ACTIVE
FROM ROUNDS_STREAM ROUNDS_STREAM
GROUP BY ROUNDS_STREAM.ID
EMIT CHANGES;




CREATE STREAM teams_stream (
    id VARCHAR KEY,
    points INT,
    activated INT,
    client_id VARCHAR
) WITH (
    KAFKA_TOPIC = 'teams',
    VALUE_FORMAT = 'JSON'
);


CREATE TABLE TEAMS_TABLE WITH (KAFKA_TOPIC='teams-table', PARTITIONS=1, REPLICAS=1) AS 
SELECT
  TEAMS_STREAM.ID ID,
  LATEST_BY_OFFSET(TEAMS_STREAM.POINTS) AS POINTS,
  LATEST_BY_OFFSET(TEAMS_STREAM.ACTIVATED) AS ACTIVATED,
  LATEST_BY_OFFSET(TEAMS_STREAM.CLIENT_ID) AS CLIENT_ID
FROM TEAMS_STREAM TEAMS_STREAM
GROUP BY TEAMS_STREAM.ID
EMIT CHANGES;