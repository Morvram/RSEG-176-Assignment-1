import os
 
from flask import Flask, render_template, request, redirect, send_file
from werkzeug.utils import secure_filename
 
from s3demo import list_files, upload_file, download_file
 
app = Flask(__name__)
 
 
# pre-requisites -
# 1. in the project directory remember to create the "upload" and "download" folders
# 2. aws iam cli user is already created and have s3 full access policy attached
# 3. aws s3 bucket is already created
 
 
# creating the endpoints
 
# index
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', contents=list_files())
 
 
# uploading file to s3
@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    if f.filename:
        print('Uploading file = {}'.format(f.filename))
        # secure_filename function will replace any whitespace provided filename with an underscore
        # saving the file in the local folder
        f.save(os.path.join('upload', secure_filename(f.filename)))
        upload_file(f'upload/{secure_filename(f.filename)}')
    else:
        print('Skipping file upload op')
 
    return redirect('/')
 
 
# downloading file from s3
@app.route('/download/', methods=['GET'])
def download(filename):
    print('Downloading file = {}'.format(filename))
    output = download_file(filename)
 
    return send_file(output, as_attachment=True)
 
 
if __name__ == '__main__':
    app.run(debug=False)