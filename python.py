from flask import Flask, jsonify
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"
    username = os.getlogin()
    server_time = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # Get top output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    return f"""
    <html>
    <body>
        <h1>Today is {datetime.now().strftime('%A, %B %d, %Y')} and here are the results:</h1>
        <p>Name: {name}</p>
        <p>Username: {username}</p>
        <p>Server Time in IST: {server_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)