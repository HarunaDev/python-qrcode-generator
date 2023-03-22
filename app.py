# install librarires needed
import qrcode

# create function that receives text and converts it to qr-code
def qr_generator(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )
# save qr-code as image

# run function