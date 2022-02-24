from PIL import Image, ImageDraw
from easyinput import read
f = read(str)
t = read(str)
n = read(int)
m = read(int)
if m>(n+1)/2:    
    img = Image.new('RGB', (n,m), f)
    dib = ImageDraw.Draw(img)
    dib.polygon([(0, 0), (n/2, (n1)), (n, 0)], t)
else:
    print("Introdueix una amplada i altura correcta")
#img.save('output.png')
img.show()