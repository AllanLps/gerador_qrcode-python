import qrcode

def gerator():
    link = input("Digite o link que deseja conerter em QR Code: ")

    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")

    print("QR Code gerado com sucesso!")

gerator()