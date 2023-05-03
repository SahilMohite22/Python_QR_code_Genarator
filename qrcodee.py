import qrcode
url=input("Enter the url of which you need to generate the QR code \n")
thing=input("What is this url of --- Example : URL OF YOUTUBE then enter YOUTUBE \n")
img=qrcode.make(url)
img.save("scanner.jpg")


