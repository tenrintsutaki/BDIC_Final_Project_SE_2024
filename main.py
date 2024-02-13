from flask import *
import testOCR

app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def login_chat_room():
    return render_template("OCR_Front_Test.html")

@app.route('/ocr', methods=['GET'])
def get_ocr_result():
    text = testOCR.start_ocr()
    return text

if __name__ == "__main__":
    app.run()