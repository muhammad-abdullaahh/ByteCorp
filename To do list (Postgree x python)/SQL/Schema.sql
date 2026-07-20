CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    due_date DATE,
    created_at TIMESTAMP DEFAULT NOW()
);
ALTER TABLE tasks
ADD CONSTRAINT check_status
CHECK (status IN ('pending', 'done'));

SELECT *
FROM tasks