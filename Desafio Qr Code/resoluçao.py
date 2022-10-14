from PIL import Image

img = Image.open("qrcodes.png").convert("RGB")

larg, alt = img.size

#Gera uma imagem vazia
newImg = Image.new("RGB", (27,27))

#Percorre toda a imagem dos qrcodes
for x in range(0,larg,27):
    for y in range(0,alt,27):
        #Armazena os qrcodes consecutivamente
        qrcode = img.crop((x,y,x+27,y+27))
        #Armazena os pixels do qrcode
        pixels = qrcode.load()

        #Percorre cada qrcode individualmente
        for i in range(27):
            for j in range(27):
                #Pega as cores rgb de cada pixel (tudo preto ou tudo branco)
                r,g,b = pixels[i,j]
                #Faz o xor de cada valor do pixel com os pixels da imagem gerada
                r ^= newImg.getpixel((i,j))[0]
                g ^= newImg.getpixel((i,j))[1]
                b ^= newImg.getpixel((i,j))[2]

                #Armazena os novos valores RGB
                pixels[i,j] = (r,g,b)

        newImg.paste(qrcode, (0,0))

#Gera a imagem do resultado final, que é o qrcode sem par
newImg.save("finalqrcode.png")