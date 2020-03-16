# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, request
from service import mypdf, test_logic
import os

# creating a Flask app
app = Flask(__name__)

global path


@app.route('/upload')
def uploader():
    path = str(request.args['x'])
    mypdf.f2i(path)


    res = []
    for i in os.listdir(os.path.join(os.getcwd(), 'images/')):
        # import pdb;pdb.set_trace()
        res.append(test_logic.blob(os.path.join(os.getcwd(),'images',i)))
    return 'The answer is {0}'.format(res)


# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
# @app.route('/test/predict')
# def home():
#     # import pdb; pdb.set_trace()
#     # if "document" in request:
#     uploaded_file = request.files["document"]
#     uploaded_file.save("test.jpg")
#     # print(uploaded_file.filename)
#     return uploaded_file.filename


# driver function
if __name__ == '__main__':
    app.run(debug=True, port=8000)
