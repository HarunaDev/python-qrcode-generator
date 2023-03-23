# install librarires needed
import qrcode

# get link or text from user
link = input("Enter link or text here: ")

# create function that receives text and converts it to qr-code
def qr_generator(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_clor="black", back_color="white")

    # save qr-code as image
    img.save("qrimg.png")

# run function
qr_generator(link)