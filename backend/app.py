from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
import os
import pandas as pd

app = Flask(__name__)

# Enable CORS for ALL routes & origins
CORS(app, resources={r"/*": {"origins": "*"}})

# Upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    return '''
    <html>
      <head><title>CSV Uploader</title></head>
      <body>
        <h1>Upload a CSV File</h1>
        <form action="/upload" method="post" enctype="multipart/form-data">
          <input type="file" name="file" accept=".csv" required/>
          <button type="submit">Upload</button>
        </form>
      </body>
    </html>
    '''

@app.route('/upload', methods=['OPTIONS', 'GET', 'POST'])
def upload_file():
    # 1) CORS preflight
    if request.method == 'OPTIONS':
        return '', 200

    # 2) Browser GET → send them back to the form
    if request.method == 'GET':
        return redirect(url_for('index'))

    # 3) Actual CSV upload (POST)
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save & parse
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        return jsonify({"error": f"Failed to read CSV: {e}"}), 400

    return jsonify({
        "message": "File uploaded successfully",
        "rows":   len(df),
        "data":   df.to_dict(orient='records')
    })

if __name__ == '__main__':
    # If you still see watchdog errors, add use_reloader=False here
    app.run(host='0.0.0.0', port=5001, debug=True)
