import qrcode
from ulaval_data import STUDENTS


def find_student_by_registration_number(registration_number):
    return STUDENTS.get(registration_number)


def create_registration_numbers_qrcodes():
    print('QR Codes creation started...')
    for registration_number in STUDENTS.keys():
        img = qrcode.make(registration_number)
        img.save('qrcodes/{}.png'.format(registration_number), 'PNG')
    print('QR Codes creation finished...')