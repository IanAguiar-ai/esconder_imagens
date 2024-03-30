#Minhas:
import esconder_imgs
#main2 -> colocar imagem em imagem
#converter -> converter imagem escondida
#main3 -> colocar imagem em texto
#ler -> ler imagem

import os
from time import sleep

from threading import Thread, active_count

#Grafico:
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image

try:
    from platform import system
    print(f"Rodando em {system()}")
except:
    def system():
        return "NONE"

#Classe para paralelizar a tarefa:
class paralelo:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        pr = Thread(target = self.func, args = [*args])
        pr.start()

        if self.func.__name__ != "esconder_texto" or self.func.__name__ != "quantidade_rgb":
            texto.insert("1.0", "")

    def __repr__(self):
        return str(self.memoria)


#Funções:
def escolher_dir():
    global caminho

    if system() == "Linux":
        x_ = 240
    else:
        x_ = 210 
    y_ = 545

    Tk().withdraw()
    caminho = filedialog.askdirectory()

        
    if caminho == "":
        Label(grafico, text = 50 * " ",
              font = "Times 14", bg = cor_4, fg = 'White').place(x = x_, y = y_)
        Label(grafico, text = "Será salvo na pasta atual do programa",
              font = "Times 13", bg = cor_4, fg = 'White',
              borderwidth = 0, relief = "sunken").place(x = x_, y = y_)
        messagebox.showinfo(title = "information", message = "Você não selecionou nenhum diretório!")
        caminho = os.getcwd()
        
    else:
        Label(grafico, text = 50 * " ",
              font = "Times 14", bg = cor_4, fg = 'White').place(x = x_, y = y_)
        Label(grafico, text = str(caminho[:12] + "..." + caminho[-18:]),
              font = "Times 14", bg = cor_4, fg = 'White').place(x = x_, y = y_)
        

    pass

def deletar_1():
    global caminho_1
    del caminho_1

def deletar_2():
    global caminho_2
    del caminho_2

def limpar():
    texto.delete("1.0", "100000.100000")


#Imagem:
def deletar_img_1():
    deletar_1()
    plot_img()
    pass

def deletar_img_2():
    deletar_2()
    plot_img()
    pass
    
def ver_img_1():
    global img_1_original
    img_1_original.show()

def ver_img_2():
    global img_2_original
    img_2_original.show()
    
def plot_img():    
    if not "caminho_1" in globals() and not "caminho_2" in globals():
        Label(grafico, text = " "*10,
              font = "Times 350", bg = cor_4, fg = 'White').place(x = 10, y = 580)
        globals()["proporcao_tela"] = "500x588"
        grafico.geometry(globals()["proporcao_tela"])
        return

    if not "caminho_1" in globals():
        Label(grafico, text = " "*2,
              font = "Times 350", bg = cor_4, fg = 'White').place(x = 10, y = 605)
        Label(grafico, text = " "*7,
              font = "Times 15", bg = cor_4, fg = 'White').place(x = 155, y = 582)

    if not "caminho_2" in globals():
        Label(grafico, text = " "*2,
              font = "Times 350", bg = cor_4, fg = 'White').place(x = 260, y = 605)
        Label(grafico, text = " "*7,
              font = "Times 15", bg = cor_4, fg = 'White').place(x = 260 + 160, y = 582)
        
    if "caminho_1" in globals():
        
        Label(grafico, text = "Imagem principal:",
              font = "Times 14", bg = cor_4, fg = 'White').place(x = 10, y = 582)

        Label(grafico, text = " "*2,
              font = "Times 350", bg = cor_4, fg = 'White').place(x = 10, y = 605)

        globals()["proporcao_tela"] = "500x730"
        grafico.geometry(globals()["proporcao_tela"])
        img1 = Image.open(caminho_1)
        
        globals()["img_1_original"] = img1

        Button(grafico, text = "Ver",
           bg = '#d9d948', borderwidth = 1, font = "Arial 12", activebackground = '#b3b337',
           activeforeground = 'Black', fg = 'Black',
           command = ver_img_1).place(x = 155, y = 582)
        
        a, b = img1.size
        x = (100/b)
        if a*x < 225:
            img1 = img1.resize((int(a*x), int(b*x)), Image.ANTIALIAS)
        else:
            x = (225/a)
            img1 = img1.resize((int(a*x), int(b*x)), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(img1)
        globals()["plot_1"] = Label(grafico, image = img1)
        global plot_1
        plot_1.pack()
        plot_1 = plot_1.place(x = 10, y = 620)

        Button(grafico, text = "X",
           bg = cor_6, borderwidth = 1, font = "Times 10", activebackground = cor_7,
           activeforeground = 'Black', fg = 'Black',
           command = deletar_img_1).place(x = 10, y = 620)


    if "caminho_2" in globals():
        Label(grafico, text = "Imagem a esconder:",
              font = "Times 14", bg = cor_4, fg = 'White').place(x = 260, y = 582)

        Label(grafico, text = " "*2,
              font = "Times 350", bg = cor_4, fg = 'White').place(x = 260, y = 605)

        globals()["proporcao_tela"] = "500x730"
        grafico.geometry(globals()["proporcao_tela"])
        img2 = Image.open(caminho_2)

        globals()["img_2_original"] = img2

        Button(grafico, text = "Ver",
           bg = '#d9d948', borderwidth = 1, font = "Arial 12", activebackground = '#b3b337',
           activeforeground = 'Black', fg = 'Black',
           command = ver_img_2).place(x = 260 + 160, y = 582)
        
        a, b = img2.size
        x = (100/b)
        if a*x < 225:
            img2 = img2.resize((int(a*x), int(b*x)), Image.ANTIALIAS)
        else:
            x = (225/a)
            img2 = img2.resize((int(a*x), int(b*x)), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img2)
        globals()["plot_2"] = Label(grafico, image = img2)
        global plot_2
        plot_2.pack()
        plot_2  = plot_2.place(x = 260, y = 620)

        Button(grafico, text = "X",
           bg = cor_6, borderwidth = 1, font = "Times 10", activebackground = cor_7,
           activeforeground = 'Black', fg = 'Black',
           command = deletar_img_2).place(x = 260, y = 620)
        

    grafico.mainloop()

###Chamada principal:
def imagem_principal():
    globals()["caminho_1"] = askopenfilename(filetypes = [("Image files", "*.png"),
                                                          ("Image files","*.jpeg"),
                                                          ("Image files","*.jpg")])
    if caminho_1 != "":
        texto.insert("1.0", "Você escolheu a imagem principal:\n" + caminho_1 + "\n\n")
        img__ = ImageTk.PhotoImage(Image.open(caminho_1))
        
    else:
        texto.insert("1.0", "Você não escolheu nenhuma imagem, escolha uma imagem principal!\n\n")
        deletar_1()

    plot_img()
        
def imagem_escondida():
    globals()["caminho_2"] = askopenfilename(filetypes = [("Image files", "*.png"),
                                                          ("Image files","*.jpeg"),
                                                          ("Image files","*.jpg")])

    if caminho_2 != "":
        texto.insert("1.0", "Você escolheu a imagem que vai esconder:\n" + caminho_2 + "\n\n")
    else:
        texto.insert("1.0", "Você não escolheu nenhuma imagem para esconder!\n\n")
        deletar_2()

    plot_img()

#Salvar arquivos:

def carregando():
    texto.insert("1.0", "#")

@paralelo
def esconder_texto():
    if "caminho_1" in globals().keys():
        global texto
        texto_ = texto.get("1.0","1000.1000")
            
        img = esconder_imgs.main3(caminho_1, texto_)
        print(caminho)
        if system() == "Linux":
            salv = caminho + "/" + arquivo_nome.get() + ".png"
        else:
            salv = caminho + "\\" + arquivo_nome.get() + ".png"
        img.save(salv)
            
        messagebox.showinfo(title = "Informação", message = "Salvo em " + salv + ".")

        texto.insert("1.0", "Você salvou uma imagem com texto escondido em:\n" + salv + "\n\n")
    else:
        messagebox.showinfo(title = "Informação", message = "Você não escolheu a imagem principal!")


@paralelo
def ler_texto():
    if "caminho_1" in globals().keys():
        global texto
            
        texto_lido = esconder_imgs.ler(caminho_1)

        limpar()
        texto.insert("1.0", "O texto escondido é:\n" + texto_lido.replace("carregando...","") + "\n\n")
    else:
        messagebox.showinfo(title = "Informação", message = "Você não escolheu a imagem que você quer ler!")

@paralelo
def esconder_imagem(): 
    if "caminho_1" in globals().keys() and "caminho_2" in globals().keys():
            
        img = esconder_imgs.main2(caminho_1, caminho_2, qualidade.get())

        salv = caminho + "\\" + arquivo_nome.get() + ".png"
        img.save(salv)

        messagebox.showinfo(title = "Informação", message = "Salvo em " + salv + ".")

        texto.insert("1.0", "Imagem escondida em:\n" + salv + "\n\n")
    else:
        messagebox.showinfo(title = "Informação", message = "Você não escolheu duas imagens!")

@paralelo
def obter_imagem():
    if "caminho_1" in globals().keys():
            
        img = esconder_imgs.converter(caminho_1, qualidade.get())

        salv = caminho + "\\" + arquivo_nome.get() + ".png"
        img.save(salv)

        messagebox.showinfo(title = "Informação", message = "Salvo em " + salv + ".")

        texto.insert("1.0", "Imagem obtida está em:\n" + salv + "\n\n")
    else:
        messagebox.showinfo(title = "Informação", message = "Você não escolheu a imagem que você quer ler!")
    
@paralelo
def quantos_threads():
    """
    Corrige a proporção da tela
    """
    while True:
        try:
            grafico.geometry(proporcao_tela)
            hm = active_count()
            if hm < 10:
                hm = "0"+str(hm)
            Label(grafico, text = f"Threads ativos: {str(hm)}",
                          font = "Times 10", bg = cor_4, fg = 'White',
                          borderwidth = 0, relief = "sunken").place(x = 20, y = 340)
        except RuntimeError:
            break
        except _tkinter.TclError:
            break
        sleep(3)


#Caixas de ajuda:
def ajuda_escolha_img():
    messagebox.showinfo(title = "Informação", message = "Você pode escolher imagens com extensão png, jpeg e jpg.")

def ajuda_esconder_texto():
    messagebox.showinfo(title = "Informação", message = "Depois de ter escolhido uma imagem e ter escrito algo você pode esconder um texto na imagem. Este texto não aceita maiusculas, acentos, caracteres especiais ou 'ç'.")

def ajuda_ler_texto():
    messagebox.showinfo(title = "Informação", message = "Escolha um arquivo que você quer ler o texto, aperte o botão 'Ler texto escondido'.")

def ajuda_esconder_imagem():
    messagebox.showinfo(title = "Informação", message = "Depois de ter escolhido duas imagens você pode esconder uma imagem em outra.")

def ajuda_ler_imagem():
    messagebox.showinfo(title = "Informação", message = "Escolha um arquivo que você quer ler a imagem escondida.")

def ajuda_qualidade():
    messagebox.showinfo(title = "Informação", message = "É a qualidade da imagem principal, quanto maior a qualidade da imagem principal menor a qualidade da imagem escondida.")

def ajuda_nome_arquivo():
    messagebox.showinfo(title = "Informação", message = "Escolha o nome do seu arquivo, ele não pode ter pontos nem o tipo da extensão.")

def ajuda_local_salvar():
    messagebox.showinfo(title = "Informação", message = "É o local em que as imagens geradas serão salvas.")


#Textos dinamicos:
@paralelo
def quantidade_rgb():
    #Qualidade:
    ant = ""

    if system() == "Linux":
        y_ = 465
    else:
        y_ = 460
    
    while True:
        try:
            novo = str(qualidade.get()**3) + " cores possíveis"

            if novo != ant:
                Label(grafico, text = " " * 50,
                        font = "Times 14", bg = cor_4, fg = 'White').place(x = 280, y = y_)
                Label(grafico, text = novo,
                        font = "Times 14", bg = cor_4, fg = 'White').place(x = 280, y = y_)
                ant = str(qualidade.get()**3) + " cores possíveis"

        except RuntimeError:
            break

        sleep(0.2)

### Parte gráfica:
if __name__ == "__main__":

    caminho = os.getcwd()
    
    grafico = Tk()

    proporcao_tela = "500x588"
    grafico.geometry(proporcao_tela)
    grafico.resizable(width = True, height = True)
    grafico.title("Escondendo em imagens")

    try:
        grafico.iconphoto(False, ImageTk.PhotoImage(Image.open("icone.png")))
    except:
        pass

    cor_1 = '#4a698c'
    cor_4 = '#3a597a'
    cor_3 = '#3c79a0'
    cor_2 = '#596f71'
    cor_5 = '#13868f'
    cor_6 = '#cd3131'
    cor_7 = '#ad2929'
    
    grafico.configure(bg = cor_4)

    #Variáveis:
    qualidade = IntVar(grafico, 64)
    arquivo_nome = StringVar(grafico, "arquivo_teste")
    

    #Texto principal:
    Label(grafico, text = "Escolha uma imagem e coloque um texto secreto\nou\nescolha duas e esconda a segunda imagem dentro da primeira.",
          font = "Times 14", bg = cor_1, fg = 'White',
          borderwidth = 4, relief = "sunken").place(x = 15, y = 70)


    if system() == "Linux":
        #Botões:
        loc_1 = (18, 20)
        
        Button(grafico, text = "Escolher imagem principal",
               bg = cor_3, borderwidth = 1, font = "Arial 11", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = imagem_principal).place(x = loc_1[0], y = loc_1[1])

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 7", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_escolha_img).place(x = loc_1[0] + 197, y = loc_1[1])

        Button(grafico, text = "Escolher imagem escondida",
               bg = cor_3, borderwidth = 1, font = "Arial 11", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = imagem_escondida).place(x = loc_1[0] + 235, y = loc_1[1])

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 7", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_escolha_img).place(x = loc_1[0] + 235 + 209, y = loc_1[1])


        #Caixa de texto:
        texto = Text(grafico, width = 59, height = 10,
                     font = "Times 12", borderwidth = 2,
                     relief = "sunken")

        texto.place(x = 13, y = 155)

        Button(grafico, text = "X",
               bg = cor_6, borderwidth = 1, font = "Arial 12", activebackground = cor_7,
               activeforeground = 'White', fg = 'White',
               command = limpar).place(x = 454, y = 155)

        #Botões finais:
        #Esconder e ler texto:
        loc_1 = (18, 380)
        Button(grafico, text = "Esconder texto",
               bg = cor_3, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = esconder_texto).place(x = loc_1[0], y = loc_1[1])

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 10", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_esconder_texto).place(x = loc_1[0] + 135, y = loc_1[1])

        Button(grafico, text = "Ler texto escondido",
               bg = cor_3, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ler_texto).place(x = loc_1[0] + 235, y = loc_1[1])

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 10", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_ler_texto).place(x = loc_1[0] + 235 + 168, y = loc_1[1])

        #Esconder e ler imagem:
        loc_1 = (18, 420)
        Button(grafico, text = "Esconder imagem",
               bg = cor_3, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = esconder_imagem).place(x = loc_1[0], y = loc_1[1])

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 10", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_esconder_imagem).place(x = loc_1[0] + 158, y = loc_1[1])

        Button(grafico, text = "Pegar imagem escondida",
               bg = cor_3, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = obter_imagem).place(x = loc_1[0] + 235, y = loc_1[1])

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 10", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_ler_imagem).place(x = loc_1[0] + 235 + 211, y = loc_1[1])


        #Qualidade:
        Label(grafico, text = "Qualidade da imagem:",
              font = "Times 14", bg = cor_4, fg = 'White').place(x = loc_1[0], y = loc_1[1] + 40)
        
        ttk.Combobox(grafico, textvariable = qualidade,
                     values = [128, 64, 32, 16],
                     width = 3, font = "Times 14").place(x = loc_1[0] + 175, y = loc_1[1] + 40)

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 10", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_qualidade).place(x = loc_1[0] + 222, y = loc_1[1] + 40)

        quantidade_rgb()
        

        #Nome do arquivo:
        Label(grafico, text = "Salvar arquivo com o nome:",
              font = "Times 14", bg = cor_4, fg = 'White').place(x = loc_1[0], y = loc_1[1] + 80)
        

        Entry(grafico, textvariable = arquivo_nome,
              font = "Times 14", width = 23).place(x = loc_1[0] + 220, y = loc_1[1] + 80)

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 10", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_nome_arquivo).place(x = loc_1[0] + 436 , y = loc_1[1] + 80)

        loc_1 = (loc_1[0], loc_1[1] + 120)
        
        #Salvar em:
        Button(grafico, text = "Local de salvamento",
               bg = '#34a1d9', borderwidth = 1, font = "Arial 12", activebackground = '#0d858e',
               activeforeground = 'White', fg = 'White',
               command = escolher_dir).place(x = loc_1[0], y = loc_1[1])
        
        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_local_salvar).place(x = loc_1[0] + 176, y = loc_1[1])

    else:
        #Botões:
        loc_1 = (18, 20)
        
        Button(grafico, text = "Escolher imagem principal",
               bg = cor_3, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = imagem_principal).place(x = loc_1[0], y = loc_1[1])

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_escolha_img).place(x = loc_1[0] + 200, y = loc_1[1])

        Button(grafico, text = "Escolher imagem escondida",
               bg = cor_3, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = imagem_escondida).place(x = loc_1[0] + 235, y = loc_1[1])

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_escolha_img).place(x = loc_1[0] + 235 + 214, y = loc_1[1])


        #Caixa de texto:
        texto = Text(grafico, width = 59, height = 10,
                     font = "Times 12", borderwidth = 2,
                     relief = "sunken")

        texto.place(x = 13, y = 155)

        Button(grafico, text = chr(128465),
               bg = cor_6, borderwidth = 1, font = "Arial 12", activebackground = cor_7,
               activeforeground = 'White', fg = 'White',
               command = limpar).place(x = 457, y = 155)

        #Botões finais:
        #Esconder e ler texto:
        loc_1 = (18, 380)
        Button(grafico, text = "Esconder texto",
               bg = cor_3, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = esconder_texto).place(x = loc_1[0], y = loc_1[1])

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_esconder_texto).place(x = loc_1[0] + 120, y = loc_1[1])

        Button(grafico, text = "Ler texto escondido",
               bg = cor_3, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ler_texto).place(x = loc_1[0] + 235, y = loc_1[1])

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_ler_texto).place(x = loc_1[0] + 235 + 153, y = loc_1[1])

        #Esconder e ler imagem:
        loc_1 = (18, 420)
        Button(grafico, text = "Esconder imagem",
               bg = cor_3, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = esconder_imagem).place(x = loc_1[0], y = loc_1[1])

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_esconder_imagem).place(x = loc_1[0] + 145, y = loc_1[1])

        Button(grafico, text = "Pegar imagem escondida",
               bg = cor_3, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = obter_imagem).place(x = loc_1[0] + 235, y = loc_1[1])

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_ler_imagem).place(x = loc_1[0] + 235 + 197, y = loc_1[1])


        #Qualidade:
        Label(grafico, text = "Qualidade da imagem:",
              font = "Times 14", bg = cor_4, fg = 'White').place(x = loc_1[0], y = loc_1[1] + 40)
        
        ttk.Combobox(grafico, textvariable = qualidade,
                     values = [128, 64, 32, 16],
                     width = 3, font = "Times 14").place(x = loc_1[0] + 175, y = loc_1[1] + 40)

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_qualidade).place(x = loc_1[0] + 230, y = loc_1[1] + 40)

        quantidade_rgb()
        

        #Nome do arquivo:
        Label(grafico, text = "Salvar arquivo com o nome:",
              font = "Times 14", bg = cor_4, fg = 'White').place(x = loc_1[0], y = loc_1[1] + 80)
        

        Entry(grafico, textvariable = arquivo_nome,
              font = "Times 14", width = 23).place(x = loc_1[0] + 220, y = loc_1[1] + 80)

        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_nome_arquivo).place(x = loc_1[0] + 436 , y = loc_1[1] + 80)

        loc_1 = (loc_1[0], loc_1[1] + 120)
        
        #Salvar em:
        Button(grafico, text = "Local de salvamento",
               bg = '#34a1d9', borderwidth = 1, font = "Arial 12", activebackground = '#0d858e',
               activeforeground = 'White', fg = 'White',
               command = escolher_dir).place(x = loc_1[0], y = loc_1[1])
        
        Button(grafico, text = "?",
               bg = cor_5, borderwidth = 1, font = "Arial 12", activebackground = cor_5,
               activeforeground = 'White', fg = 'White',
               command = ajuda_local_salvar).place(x = loc_1[0] + 160, y = loc_1[1])

    quantos_threads()

    grafico.mainloop()

