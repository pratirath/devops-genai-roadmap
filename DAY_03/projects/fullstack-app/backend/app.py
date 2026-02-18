from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        database=os.getenv('DB_NAME', 'myapp'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'postgres')
    )
    return conn

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': str(datetime.now()),
        'service': 'backend-api'
    })

@app.route('/api/messages', methods=['GET'])
def get_messages():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, content, created_at FROM messages ORDER BY created_at DESC;')
        messages = cur.fetchall()
        cur.close()
        conn.close()
        
        return jsonify({
            'messages': [
                {'id': m[0], 'content': m[1], 'created_at': str(m[2])}
                for m in messages
            ]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/messages', methods=['POST'])
def create_message():
    try:
        data = request.get_json()
        content = data.get('content')
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO messages (content) VALUES (%s) RETURNING id;', (content,))
        message_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({'id': message_id, 'content': content}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)