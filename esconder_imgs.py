from PIL import Image, ImageColor
from random import random
from sympy import nextprime
from math import *

def obter_mono(nome):
    img1 = Image.open(nome)
    img1 = img1.convert("L")
    return img1.load(), img1.size

def main1(mmg_1, mmg_2, mmg_3):
    """
    Coloca 3 imagens jutas
    """

    p1, size = obter_mono(mmg_1)
    p2, _ = obter_mono(mmg_2)
    p3, _ = obter_mono(mmg_3)
    
    ing = Image.new("RGB",(size))

    for i in range(size[0]):
        for j in range(size[1]):
            ing.putpixel((i,j), (p1[i,j], p2[i,j], p3[i,j]))
        
    #ing.show()
    
    return ing

def obter_16(nome, b):
    img1 = Image.open(nome)
    k = img1.load()
    p = []

    for i in range(img1.size[0]):
        n = []
        for j in range(img1.size[1]):
            n.append(list(k[i,j]))
        p.append(list(n))

    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            p[i][j][0] = int(p[i][j][0]/b)
            p[i][j][1] = int(p[i][j][1]/b)
            p[i][j][2] = int(p[i][j][2]/b)

    return p, img1.size

def main2(mmg_1, mmg_2, bits = 16):
    """
    Coloca uma imagem dentro da outra
    """

    p1, size = obter_16(mmg_1, int(256/bits))
    p2, size2 = obter_16(mmg_2, bits)

    if size[0] < size2[0] or size[1] < size2[1]:
        print("Imagem escondida maior que imagem que esconde!")
        
    ing = Image.new("RGB",(size))

    b = int(256/bits)

    for i in range(size[0]):
        for j in range(size[1]):
            try:
                ing.putpixel((i,j), (p1[i][j][0]*b + p2[i][j][0],
                                     p1[i][j][1]*b + p2[i][j][1],
                                     p1[i][j][2]*b + p2[i][j][2]))
            except IndexError:
                ing.putpixel((i,j), (p1[i][j][0]*b,
                                     p1[i][j][1]*b,
                                     p1[i][j][2]*b))
        
    #ing.show()
    
    return ing

def obter(nome):
    img1 = Image.open(nome)
    return img1.load(), img1.size

def converter(img, bits = 16):
    p, size = obter(img)
        
    ing = Image.new("RGB",(size))

    b = int(256/bits)

    for i in range(size[0]):
        for j in range(size[1]):
            ing.putpixel((i,j), ((p[i,j][0] - b*int(p[i,j][0]/b))*bits,
                                 (p[i,j][1] - b*int(p[i,j][1]/b))*bits,
                                 (p[i,j][2] - b*int(p[i,j][2]/b))*bits))

    #ing.show()
    
    return ing
        
    
def main3(mmg, texto):
    """
    Coloca um texto dentro de uma imagem
    """
    p, size = obter_16(mmg, 4)
    p_, size = obter(mmg)

    ing = Image.new("RGB",(size))

    k = 0
    for i in range(size[0]):
        for j in range(size[1]):
            try:
                num = converter_para_rgb(texto[k].lower().replace("á","a").replace("é","e"))
                ing.putpixel((i,j), (p[i][j][0]*4 + num[0],
                                         p[i][j][1]*4 + num[1],
                                         p[i][j][2]*4 + num[2]))
                k += 1
            except:
                ing.putpixel((i,j), (p_[i,j][0], p_[i,j][1], p_[i,j][2]))
                             
    #ing.show()
    
    return ing 


def converter_para_rgb(a):
    if not "dic" in globals():
        globals()["l"] = []

        l.extend([" ","\n",",",".","_","`","\"","\'"])

        for i in range(97, 123):
            l.append(chr(i))

        l.extend(["1","2","3","4","5","6","7","8","9","0"])
        l.extend(["(",")","[","]","{","}","<",">"])
        l.extend([":",";"])
        l.extend(["+","-","*","/","%","\\","#","@","!","?"])

        globals()["dic"]= {}

        for i in range(len(l)):
            dic[l[i]] = (int(i/16),
                         int(i/4)%4,
                         i%4)

    try:
        return dic[a]
    except:
        return dic[" "]

def ler(img):
    p, size = obter(img)

    converter_para_rgb(" ")

    global dic, l

    texto = ""
    for i in range(size[0]):
        for j in range(size[1]):#size[1]):
            n = (p[i,j][0] - int(p[i,j][0]/4)*4,
                 p[i,j][1] - int(p[i,j][1]/4)*4,
                 p[i,j][2] - int(p[i,j][2]/4)*4)

            texto += l[n[0]*16 + n[1]*4 + n[2]]

    return texto.replace("  ","")
