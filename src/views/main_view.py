import tkinter as tk
from tkinter import ttk, messagebox

from PIL import ImageTk, Image

from src.translation.translation import _
from src import consts, models


class MainView(object):
    def __init__(
            self,
            close_click_callback: callable = None
    ):
        # instance attributes
        self.close_click_callback: callable = close_click_callback
        # view attributes
        self.window: tk.Tk = self._init_window()
        self.window.protocol("WM_DELETE_WINDOW", self.on_close_click)
        # view initialization
        self._init_window_widgets(window=self.window)

    @staticmethod
    def _init_window() -> tk.Tk:
        window: tk.Tk = tk.Tk()
        window.title("Qualidade dos Nutrientes da Hidroponia de alface")
        window.iconphoto(False, tk.PhotoImage(file="assets/alface-icon.png"))
        pad = 15
        widthMaxPx = window.winfo_screenwidth()
        heightMaxPx = window.winfo_screenheight()
        window.geometry("{0}x{1}+0+-3".format(widthMaxPx - pad, heightMaxPx - pad))
        window["bg"] = consts.cc_green
        return window

    @staticmethod
    def _init_window_widgets(window: tk.Tk):
        ctHeader = tk.Frame(window, bg=consts.cc_green)
        lbH1 = tk.Label(
            ctHeader,
            text="Hidroponia de Alfaces",
            bg=consts.cc_green,
            font=("Roboto", 32, "bold")
        )
        lbH2 = tk.Label(
            ctHeader,
            text="Olá, Agricultor",
            bg="green",
            padx=200,
            font=("Arial", 16),
            fg="white"
        )
        ctHeader.pack(side=tk.TOP, fill='x')
        lbH1.pack(side=tk.LEFT, expand=1)
        lbH2.pack(side=tk.RIGHT, fill='y')

        tabControl = ttk.Notebook(window)
        win1 = ttk.Frame(tabControl)
        win2 = ttk.Frame(tabControl)
        tabControl.pack(expand=1, fill='both')
        tabControl.add(win1, text="Dashboard")
        tabControl.add(win2, text="Configurações")
        # background
        img1 = ImageTk.PhotoImage(Image.open("assets/bg.jpg"))
        background1 = tk.Label(win1, image=img1)
        background1.place(x=150, y=50, relwidth=1)
        # Conteiner do cabeçalho do tab 1
        ctPag1Header = tk.Frame(win1)
        HeaderPag1 = tk.Label(
            ctPag1Header,
            text="Dados de Qualidade do Nutriente",
            font=("Arial", 24, "bold"),
            bg="#44aa44"
        )
        ctPag1Header.pack(fill="x")
        HeaderPag1.pack(fill="x")

        # Conteiner do grupo de cards do tab 1
        ctPag1CardGroup = tk.Frame(win1, bg="#aaffaa")

        # conteiner do card 0
        ctPag1Card0 = tk.Frame(
            ctPag1CardGroup,
            bd=consts.cs_cardGroupBD
        )
        card0_lbH2 = tk.Label(
            ctPag1Card0,
            text="Condutividade:",
            font=("Roboto", 18, "bold"),
            cursor=tk.DOTBOX
        )
        card0_lbP = tk.Label(
            ctPag1Card0,
            text="0000",
            font=("Times", 14),
            padx=20,
            pady=20
        )
        img0Pag1 = Image.open("assets/alface.png")
        img0Pag1 = img0Pag1.resize(
            (consts.cs_cardImgH, consts.cs_cardImgW), Image.ANTIALIAS)  # The (250, 250) is (height, width)
        img0Pag1 = ImageTk.PhotoImage(img0Pag1)
        card0_lbImg0 = tk.Label(ctPag1Card0, image=img0Pag1)

        # conteiner do card 1
        ctPag1Card1 = tk.Frame(ctPag1CardGroup, bd=consts.cs_cardGroupBD)
        card1_lbH2 = tk.Label(ctPag1Card1, text="Nivel de Acidez:", font=("Roboto", 18, "bold"))
        card1_lbP = tk.Label(ctPag1Card1, text="0000", font=("Times", 14), padx=20, pady=20)
        img1Pag1 = Image.open("assets/fast.png")
        img1Pag1 = img1Pag1.resize((consts.cs_cardImgH, consts.cs_cardImgW), Image.ANTIALIAS)
        img1Pag1 = ImageTk.PhotoImage(img1Pag1)
        card1_lbImg0 = tk.Label(ctPag1Card1, image=img1Pag1)

        # conteiner do card 2
        ctPag1Card2 = tk.Frame(ctPag1CardGroup, bd=consts.cs_cardGroupBD)
        card2_lbH2 = tk.Label(ctPag1Card2, text="Temperatura da água:", font=("Roboto", 18, "bold"))
        card2_lbP = tk.Label(ctPag1Card2, text="0000", font=("Times", 14), padx=20, pady=20)
        img2Pag1 = Image.open("assets/thermometer.png")
        img2Pag1 = img2Pag1.resize((consts.cs_cardImgH, consts.cs_cardImgW), Image.ANTIALIAS)
        img2Pag1 = ImageTk.PhotoImage(img2Pag1)
        card2_lbImg0 = tk.Label(ctPag1Card2, image=img2Pag1)

        # conteiner do card 3
        ctPag1Card3 = tk.Frame(ctPag1CardGroup, bd=consts.cs_cardGroupBD)
        card3_lbH2 = tk.Label(ctPag1Card3, text="Temperatura Ambiente:", font=("Roboto", 18, "bold"))
        card3_lbP = tk.Label(ctPag1Card3, text="0000", font=("Times", 14), padx=20, pady=20)
        img3Pag1 = Image.open("assets/hot.png")
        img3Pag1 = img3Pag1.resize((consts.cs_cardImgH, consts.cs_cardImgW), Image.ANTIALIAS)
        img3Pag1 = ImageTk.PhotoImage(img3Pag1)
        card3_lbImg0 = tk.Label(ctPag1Card3, image=img3Pag1)

        # conteiner do card 4
        ctPag1Card4 = tk.Frame(ctPag1CardGroup, bd=consts.cs_cardGroupBD)
        card4_lbH2 = tk.Label(ctPag1Card4, text="Estado Motor:", font=("Roboto", 18, "bold"))
        card4_lbP = tk.Label(ctPag1Card4, text="0000", font=("Times", 14), padx=20, pady=20)
        img4Pag1 = Image.open("assets/motor.png")
        img4Pag1 = img4Pag1.resize((consts.cs_cardImgH, consts.cs_cardImgW), Image.ANTIALIAS)
        img4Pag1 = ImageTk.PhotoImage(img4Pag1)
        card4_lbImg0 = tk.Label(ctPag1Card4, image=img4Pag1)

        # Arrumar grupo de cards dentro da tela
        ctPag1CardGroup.pack(side=tk.BOTTOM, fill="x")

        ctPag1Card0.grid(row=0, column=0)
        card0_lbH2.pack()
        card0_lbP.pack()
        card0_lbImg0.pack()

        ctPag1Card1.grid(row=0, column=1)
        card1_lbH2.pack()
        card1_lbP.pack()
        card1_lbImg0.pack()

        ctPag1Card2.grid(row=0, column=2)
        card2_lbH2.pack()
        card2_lbP.pack()
        card2_lbImg0.pack()

        ctPag1Card3.grid(row=0, column=3)
        card3_lbH2.pack()
        card3_lbP.pack()
        card3_lbImg0.pack()

        ctPag1Card4.grid(row=0, column=4)
        card4_lbH2.pack()
        card4_lbP.pack()
        card4_lbImg0.pack()

        # #  List box para mostrar os dados recebidos
        # liPag1 = tk.Listbox(win1, bg="green", bd=5, width=20, font=("Roboto", 14), fg="white")

        # liPag1.insert(1, "Opcao 01")
        # liPag1.insert(2, "Opcao 02")
        # liPag1.insert(3, "Opcao 03")
        # liPag1.pack(side=tk.LEFT,anchor=tk.NW,fill='y', expand=1)

        # Text box para mostrar os dados recebidos
        txtPag1 = tk.Text(win1, bg="#12bb23", cursor=tk.DOTBOX, font=('Roboto', 14), width=300)

        db_lista = [
            ["id2", "INTEGER PRIMARY KEY AUTOINCREMENT"],
            ["data", "DATE NOT NULL"],
            ["tempo", "TIME NOT NULL"],
            ["condutividade", "INTEGER"],
            ["nivel_ph", "DOUBLE"],
            ["temperatura_ambiente", "INTEGER"],
            ["temperatura_agua", "INTEGER"],
            ["umidade_ambiente", "INTEGER"]
        ]

        cabecalhoDatabase = ""
        for item in db_lista:
            cabecalhoDatabase += item[0]
            cabecalhoDatabase += "\t"

        txtPag1.insert(tk.INSERT, cabecalhoDatabase)
        txtPag1.insert(tk.INSERT, "\n")

        txtPag1.pack(side=tk.RIGHT, anchor=tk.NE)

        # Implementação de dados para janela 2
        img2 = ImageTk.PhotoImage(Image.open("assets/bg-config.png"))
        background2 = tk.Label(win2, image=img2)
        background2.place(x=0, y=0, relwidth=1, relheight=1)

        bt2 = tk.Button(win2, text="CLIQUE2")
        bt2.pack()

    def on_close_click(self):
        if messagebox.askokcancel(_('confirmation'), _('finish_application')+'?') \
                and self.close_click_callback:
            self.close_click_callback()

    def update_nutrients_data(self, nutrients: [models.Nutrient]):
        pass

    def update_customers_data(self, customers: [models.Customer]):
        pass

    def show(self):
        self.window.mainloop()

    def close(self):
        self.window.destroy()
