import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from cv2 import cv2
from flask_ngrok import run_with_ngrok

from predict import CovidCXR



UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'rajnikant'
run_with_ngrok(app)



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return render_template("error.html", err="No File Found")
        
        file = request.files['file']

        if not allowed_file(file.filename):
            return render_template("error.html", err="Invalid File Format")
        
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return render_template("error.html", err="No Image Selected")
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            base = "C:/Users/dell/3D Objects/Coronavirus X-ray project - Major/source code/"
            # print(os.environ.get('IMG_HEIGHT'), os.environ.get('IMG_WIDTH'))
            model = CovidCXR(base + "models/densenet-best.hdf5", 299, 299)
            result = model.predict(filename)
            filename = request.base_url + '/uploads/' +  filename
            return render_template('result.html', result1=result, user_image = filename)
    
    return render_template('index.html', my_name="nishant")




# python index.py
'''
When you start your app by running flask run the if __name__ == '__main__': 
block gets skipped. If you don't want to skip it, run with python index.py.
'''
if __name__ == "__main__":
    app.run()