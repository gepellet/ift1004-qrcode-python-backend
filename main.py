from flask import Flask, render_template, request
from utils import find_student_by_registration_number, create_registration_numbers_qrcodes
import qrcode
from ulaval_data import STUDENTS

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/v1/students")
def find_student():
    student = find_student_by_registration_number(request.args.get('registration_number'))

    return student if student else "Student Not Found"

if __name__ == '__main__':
    # img = qrcode.make("J'aime le basket-ball")
    # img.save('favorite_sport.png', 'PNG')

    # create_registration_numbers_qrcodes()

    # print(find_student_by_registration_number("111111"))
    # print(find_student_by_registration_number("111118"))

    app.run(debug=True, host="0.0.0.0", port=3000)