from flask import Flask, request, redirect, render_template, send_from_directory
from flask_sockets import Sockets
from werkzeug.utils import secure_filename

import requests
import os

app = Flask(__name__, static_url_path='')
sockets = Sockets(app)

app.config["IMAGE_UPLOADS"] = "res"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG"]


@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        image = request.files["image"]
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], 'image.jpg'))
        url = 'http://20.86.39.35:5000/find_film'
        files = {'image': open('res/image.jpg', 'rb')}
        r = requests.post(url, files=files)
        print(r.text)
        return render_template('upload_image.html', result=r.text)

    return send_from_directory('templates', 'upload_image.html')


# return app.send_static_file("/html/upload_image.html")
# return render_template("html/upload_image.html")


if __name__ == "__main__":
    app.run()
