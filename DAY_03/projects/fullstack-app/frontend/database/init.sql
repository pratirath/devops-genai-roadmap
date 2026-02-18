-- Create messages table
CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO messages (content) VALUES 
    ('Welcome to the Full-Stack Docker App! 🚀'),
    ('This app uses Docker Compose to orchestrate multiple containers'),
    ('Frontend (Nginx) + Backend (Flask) + Database (PostgreSQL)');