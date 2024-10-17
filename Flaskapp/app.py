from flask import Flask, send_from_directory, jsonify
import subprocess
import os

app = Flask(__name__)

# Path to 'main.py' and the working directory
src_dir = r'D:\prac3\Flaskapp\src'
main_py_path = os.path.join(src_dir, 'main.py')

@app.route('/run-main', methods=['POST'])
def run_main():
    try:
        # Run 'main.py' without capturing output
        subprocess.run(['python', main_py_path], cwd=src_dir)  # No capture_output
        
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
# Path to the directory containing static files
frontend_path = r'D:\prac3\Batman2'

# Route to serve the main HTML page
@app.route('/')
def serve_frontend():
    return send_from_directory(frontend_path, 'Page3.html')

# Route to serve other static files like CSS, JS, or images
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(frontend_path, path)

# Start Flask on a custom port
if __name__ == '__main__':
    app.run(debug=True, port=5500)  # Set port to 5500
