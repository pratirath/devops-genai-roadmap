-- Initialize database schema for fullstack-app
-- This file is automatically executed when PostgreSQL container starts

-- Create messages table
CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert some sample data
INSERT INTO messages (content) VALUES 
    ('Welcome to the Full-Stack Docker App! 🚀'),
    ('This message is coming from PostgreSQL database'),
    ('Backend built with Flask, Frontend with Nginx');

-- Create index for better query performance
CREATE INDEX IF NOT EXISTS idx_messages_created_at ON messages(created_at DESC);

-- Grant necessary permissions
GRANT ALL PRIVILEGES ON TABLE messages TO postgres;
GRANT USAGE, SELECT ON SEQUENCE messages_id_seq TO postgres;
