from flask import Flask
from flask import request, flash, redirect, url_for, render_template
from flask import send_from_directory
from werkzeug.utils import secure_filename
import os

# where to store the uploaded files
UPLOAD_FOLDER = r'.\data\uploaded_files'
ALLOW_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allow_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOW_EXTENSIONS
        
@app.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        # check if the post request contain a file named 'file'
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        # if user does not select a file, the browser submit a empty file without a filename(no select file and submit)
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        
        if file and allow_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', filename=filename))
        
    return render_template('index.html')

@app.route('/uploads/<filename>', methods=['GET'])
def download_file(filename):
    # if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
    #     return f'{filename} Download successfully.'
    # else:
    #     return 'Download failed.'
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)