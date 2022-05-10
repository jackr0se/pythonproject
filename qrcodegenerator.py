import qrcode
import image

qr = qrcode.QRCode(
	version = 15, #15 means the version of the qrcode, high the number bigger the code image and complicated pictures
	box_size = 10, # size of the box where qrcode will be displayed
	border = 5 # it is the white part of image. border in all side with white color


)


data = "https://9gag.com/"

# link for content of the qrcode

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black",back_color = "white")
img.save("test.png")
