import qrcode
from PIL import Image

# Data to be encoded
data = "http://example.com"
# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save it somewhere, for example:
img.save("/home/samuel/Fall2024_IS601/user_management/qr_code.png")

# Or display it:
img.show()
