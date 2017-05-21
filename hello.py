from flask import Flask
from flask import send_file
from flask import request
from flask import redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = "/home/pi/Documents/WebServer/dropbox/"
#from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#CORS(app)
import os

@app.route("/retrieve/<documentName>", methods=['GET'])
def retrieve(documentName):
    filename = "/home/pi/Documents/WebServer/dropbox/" + documentName
    b = os.path.exists(filename)
    if b:
        try:
	    return send_file(filename, attachment_filename=documentName)
	except Exception as e:
            return str(e)
    else:
        return "File doesn't exist, sorry"
    #code for showing text
    #b = os.path.exists(filename)
    # 
    #if b:
    #    with open(filename, 'r') as myfile:
    #        data=myfile.read().replace('\n', '')
    #    return data
    #else:
    #    return "File doesn't exist!"
    
    

@app.route("/upload", methods=['POST'])
def upload():
    #if 'file' not in request.files:
    #    print('No request part')
    #file = request.files['file']
    #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    f = request.files['file']
    filename1 = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
    return 'file uploaded successfully'

    
    #data = request.files[file]
    #error with this ^
    #return data
    #path = "/home/pi/Documents/WebServer/dropbox/" + documentName
    #if not os.path.exists(path):
    #    open(path, "wb")
        
            
        #with open(os.path.join("/home/pi/Documents/WebServer/dropbox/", documentName), 'wb') as temp_file:
            #temp_file.write()
    
    
#comment the previous lines back in
    #return documentName

if __name__ == "__main__":
    app.run()
#

