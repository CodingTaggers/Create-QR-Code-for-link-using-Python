import pyqrcode as qr

link = "https://codingtaggers.blogspot.com/"

url = qr.create(link)

url.svg("myBlog.svg", scale=8)
