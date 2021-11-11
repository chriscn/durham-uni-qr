import qrcode
import random
import datetime

def generate_qr(data: str):
    qr = qrcode.QRCode(
        mask_pattern=7,
        error_correction=qrcode.ERROR_CORRECT_M
    )

    qr.add_data(data)

    qr.make(fit=True)
    img = qr.make_image()
    img.show()


def main():
    print("Durham Test and Trace: Fake QR Code")
    name = input("What is their name? ").upper()
    username = input("What is their username? ").upper()

    date = datetime.date.today().strftime('%d %b %Y')

    data = f"""Name: {name}
Username: {username}
{date}: NEGATIVE
Test ref. {random.randint(100000,250000)}"""

    print("Using data: ")
    print(data)
    generate_qr(data)

main()
