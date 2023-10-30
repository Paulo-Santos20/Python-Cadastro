from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

#Criando o formulario principal

root = Tk()

#Criando o titulo do sistema
root.title("CADASTRO DE CURRÍCULOS")
lbl_result = None
home = None


#Configurando o tamhanho do formulário principal
width=800
height = 500
screen_width = root.winfo_screenmmwidth()
screen_height = root.winfo_screenmmheight()
x=(screen_width/1) - (width/6)
y=(screen_height/1) - (height/6)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.configure(bg="lightSteelBlue3")

#Criando as variaveis do sistema de cadastro de produtos
USERNAME = StringVar()
PASSWORD = StringVar()
PRODUTO_NOME = StringVar()
PRODUTO_PRECO = IntVar()
PRODUTO_QTD = IntVar()
PESQUISA = StringVar()

#criando conexao com o BD Sqlite3
def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("create table if not exists admin (admin_id integer primary key, username varchar, password varchar)")
    cursor.execute("create table if not exists produto (produto_id integer primary key, produto_nome varchar, produto_qtd varchar, produto_preco varchar)")
    cursor.execute("select * from admin where username = 'admin' and password='admin'")
    if cursor.fetchone() is None:
        cursor.execute("insert into admin (username, password) values('admin','admin')")
        conn.commit()

#Criando metodo dos botões sair
def EXIT():
    result=tkMessageBox.askquestion('CADASTRO DE CURRÍCULOS', 'TEM CERTEZA? ', icon="warning")
    if result == "yes":
        root.destroy()
        exit()
def EXIT2():
    result=tkMessageBox.askquestion('CADASTRO DE CURRÍCULOS', 'TEM CERTEZA? ', icon="warning")
    if result == "yes":
        root.destroy()
        exit()

#Criando o formulário login
def ShowLoginForm():
    global loginform, lbl_result
    loginform = Toplevel()
    loginform.title("SISTEMA DE LOGIN")
    width = 700
    height = 370

    screen_width = root.winfo_screenmmwidth()
    screen_height = root.winfo_screenmmheight()
    x = (screen_width / 1) - (width / 400)
    y = (screen_height / 1) - (height / 400)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()

#Criando campos do formulário login
def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=50, height=50, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=2)
    lbl_text = Label(TopLoginForm, text="SEJA BEM VINDO AO SISTEMA DE CADASTRO DE CURRÍCULOS", fg="blue", font=('Arial', 10, 'bold'), width=100)
    lbl_text.pack(fill=X)
    MidLoginForm=Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    ldl_username = Label(MidLoginForm, text="USUARIO", font=('Arial', 15, 'bold'), fg='blue', bd=18)
    ldl_username.grid(row=0)
    ldl_password = Label(MidLoginForm, text="SENHA", font=('Arial', 15, 'bold'), fg='blue', bd=18)
    ldl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('Arial', 18))
    lbl_result.grid(row=3, columnspan=2)

    userNAME= Entry(MidLoginForm, textvariable=USERNAME, font=('Arial', 15),width=30)
    userNAME.grid(row=0, column=1)
    passWORD= Entry(MidLoginForm, textvariable=PASSWORD, font=('Arial', 15), width=30, show="*")
    passWORD.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="LOGIN", font=('Arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)

#Criando o formulário de produtos principal
def home():
    global home
    home = Tk()  # Crie uma instância da janela principal
    home.title("CADASTRO DE CURRÍCULOS")
    width = 1024
    height = 500
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    x = (screen_width / 1) - (width / 400)
    y = (screen_height / 1) - (height / 400)
    home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    home.resizable(0, 0)
    title = Frame(home, bd=1, relief=SOLID)
    title.pack(pady=10)
    lbl_display = Label(title, text="CADASTRO DE CURRÍCULOS", bg="orange", font=("Arial", 45))
    lbl_display.pack()
    menubor = Menu(home) 
    filemenu = Menu(menubor, tearoff=0)
    filemenu2 = Menu(menubor, tearoff=0)
    filemenu.add_command(label="LOGOUT", command=Logout)
    filemenu.add_command(Label="SAIR", command=EXIT2)
    filemenu2.add_command(Label="NOVO CADASTRO", command=ShowAddNew)
    filemenu2.add_command(Label="VISUALIZAR", command=ShoView)
    menubor.add_cascade(Label="CONTA",  menu=filemenu)
    menubor.add_cascade(Label="CADASTRO", menu=filemenu2)
    home.configure(menu =menubor)
    home.configure(bg="orange")
    return home
#Criando o metodo adicionar novo cadastro de produtos
def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("ADICIONANDO NOVOS PRODUTOS")
    width = 600
    height = 400
    screen_width =home.winfo_screenmmwidth()
    screen_height = home.winfo_screenmmheight()
    x = (screen_width / 1) - (width / 400)
    y = (screen_height / 1) - (height / 400)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()

#Criando os campos do formulario novo cadastro de produtos
def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="CADASTRAR NOVO PRODUTO", font=('Arial', 18), width=600)
    lbl_text.pack(fill=x)
    TopAddNew=Frame(addnewform, width=600)
    TopAddNew.pack(side=TOP,pady=50)
    ldl_prodname = Label(MidAddNew, text="PRODUTO", font=('Arial', 15), bd=10)
    ldl_prodname.grid(row=0, sticky=W)
    ldl_qty = Label(MidAddNew, text="QUANTIDADE", font=('Arial', 15), bd=10)
    ldl_qty.grid(row=1, sticky=W)
    ldl_preco = Label(MidAddNew, text="PREÇO", font=('Arial', 15), bd=10)
    ldl_preco.grid(row=2, sticky=W)
    prodname= Entry(MidAddNew, textvariable=PRODUTO_NOME, font=('Arial', 25),width=15)
    prodname.grid(row=0, column=1)
    prodqty= Entry(MidAddNew, textvariable=PRODUTO_QTD, font=('Arial', 25), width=15)
    prodqty.grid(row=1, column=1)
    prodpreco = Entry(MidAddNew, textvariable=PRODUTO_PRECO, font=('Arial', 25), width=15)
    prodpreco.grid(row=2, column=1)
    btn_add = Button(MidAddNew, text="SALVAR", font=('Arial', 18), width=30, bg="gray63", command=AddNew)
    btn_add.grid(row=3, columnspan=2, pady=50)

#criando a conexao do novo cadastro ao banco de dados
def AddNew():
    Database()
    cursor.execute("insert into produto (produto_nome, produto_qtd, produto_preco) values (?, ?, ?)",
               (str(PRODUTO_NOME.get()), int(PRODUTO_QTD.get()), int(PRODUTO_PRECO.get())))

    conn.commit()
    PRODUTO_NOME.set("")
    PRODUTO_QTD.set("")
    PRODUTO_PRECO.set("")
    cursor.close()
    conn.close()

#Criando os campos do formulario de cadastro de produtos
def ViewForm():
    global tree
    TopViewFrom = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewFrom.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    ldl_text = Label(TopViewFrom, text="PRODUTOS", font=('Arial', 18), width=600)
    ldl_text.pack(fill=X)
    ldl_textsearch = Label(LeftViewForm, text="PESQUISAR", font=('Arial', 15))
    ldl_textsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=PESQUISA, font=('Arial', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="PESQUISAR", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="ATUALIAZAR", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="DELETAR", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=(" ID", "NOME", "QUANTIDADE", "PRECO"), selectmode="extended", height=100, yacrollcommand=scrollbary.set, xscrollcomnand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading("ID", text="ID", anchor=W)
    tree.heading("NOME", text="NOME", anchor=W)
    tree.heading("QUANTIDADE", text="QUANTIDADE", anchor=W)
    tree.heading("PRECO", text="PRECO", anchor=W)
    tree.column("#0", stretch=NO, minwidth=0, width=0)
    tree.column("#1", stretch=NO, minwidth=0, width=0)
    tree.column("#2", stretch=NO, minwidth=0, width=200)
    tree.column("#3", stretch=NO, minwidth=0, width=120)
    tree.column("#4", stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()


def DisplayData():
    Database()
    cursor.execute("Select * from produto")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'and', values=(data))
    cursor.close()
    conn.close()

#Criando Metodo de atualizar cadastro de produtos
def Search():
    if PESQUISA.get() !="":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("select * from produto where produto_nome like ?", ('%'+str(PESQUISA.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'and', values=(data))
        cursor.close()
        conn.close()

#Criando metodo para atualizar cadastros
def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    PESQUISA.set("")

#Criando metodo para deletar
def Delete():
    if not tree.selection():
        print("ERROR!!!")
    else:
        result = tkMessageBox.askquestion('CADASTRO DE CURRÍCULOS','TEM CERTEZA? DELETANDO CADASTRO', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents('values')
            tree.delete(curItem)
            Database()
            cursor.execute("delete from produto where produto_id = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

#Definindo o tamamnho do formulario cadastro novo produto
def ShoView():
    global viewform
    viewform = Toplevel()
    viewform.title("CADASTRO DE CURRÍCULOS/VISUALIZAR CURRÍCULOS")
    width = 600
    height = 400
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenwidth()
    x = (screen_width / 1) - (width / 400)
    y = (screen_height / 1) - (height / 400)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm()  # Corrigir esta linha para ShowView()

def ShowResumeForm():
    global resumepage
    resumepage = Toplevel()
    resumepage.title("CADASTRO DE CURRÍCULOS")
    width = 800
    height = 500
    screen_width = root.winfo_screenmmwidth()
    screen_height = root.winfo_screenmmheight()
    x = (screen_width / 1) - (width / 6)
    y = (screen_height / 1) - (height / 6)
    resumepage.geometry("%dx%d+%d+%d" % (width, height, x, y))
    ResumeForm()

    def ResumeForm():
        TopResumeForm = Frame(resumepage, width=600, height=100, bd=1, relief=SOLID)
        TopResumeForm.pack(side=TOP, pady=20)
        lbl_text = Label(TopResumeForm, text="CADASTRAR CURRÍCULO", font=('Arial', 18), width=600)
        lbl_text.pack(fill=X)

        MidResumeForm = Frame(resumepage, width=600)
        MidResumeForm.pack(side=TOP, pady=50)

        lbl_name = Label(MidResumeForm, text="Nome", font=('Arial', 15), bd=10)
        lbl_name.grid(row=0, sticky=W)

        lbl_age = Label(MidResumeForm, text="Idade", font=('Arial', 15), bd=10)
        lbl_age.grid(row=1, sticky=W)

        lbl_address = Label(MidResumeForm, text="Endereço", font=('Arial', 15), bd=10)
        lbl_address.grid(row=2, sticky=W)

        lbl_phone = Label(MidResumeForm, text="Telefone", font=('Arial', 15), bd=10)
        lbl_phone.grid(row=3, sticky=W)

        entry_name = Entry(MidResumeForm, font=('Arial', 15), width=30)
        entry_name.grid(row=0, column=1)

        entry_age = Entry(MidResumeForm, font=('Arial', 15), width=30)
        entry_age.grid(row=1, column=1)

        entry_address = Entry(MidResumeForm, font=('Arial', 15), width=30)
        entry_address.grid(row=2, column=1)

        entry_phone = Entry(MidResumeForm, font=('Arial', 15), width=30)
        entry_phone.grid(row=3, column=1)

        btn_save_resume = Button(MidResumeForm, text="Salvar Currículo", font=('Arial', 18), width=30, bg="gray63", command=SaveResume)
        btn_save_resume.grid(row=4, columnspan=2, pady=50)

def SaveResume():
    name = entry_name.get()
    age = entry_age.get()
    address = entry_address.get()
    phone = entry_phone.get()

    if name == "" or age == "" or address == "" or phone == "":
        tkMessageBox.showerror("Erro", "Preencha todos os campos!")
    else:
        # Conecte-se ao banco de dados (substitua com suas configurações)
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()

        # Insira os dados do currículo na tabela de currículos (substitua com sua tabela)
        cursor.execute("INSERT INTO curriculum (name, age, address, phone) VALUES (?, ?, ?, ?)",
                       (name, age, address, phone))

        conn.commit()
        conn.close()

        # Limpe os campos após salvar
        entry_name.delete(0, 'end')
        entry_age.delete(0, 'end')
        entry_address.delete(0, 'end')
        entry_phone.delete(0, 'end')

        tkMessageBox.showinfo("Sucesso", "Currículo salvo com sucesso!")

        # Certifique-se de fechar a janela atual (se necessário)
        resumepage.destroy()



def SwitchToResume():
    home.withdraw()
    ShowResumeForm()

def SwitchToHome():
    resumepage.withdraw()
    home.deiconify()
#Metodo do formulario sair
def Logout():
    result = tkMessageBox.askquestion('CADASTRO DE CURRÍCULOS', 'TEM CERTEZA? LOGOUT', icon="warning")
    if result == 'yes':
        admin = ""
        root.deiconify()
        home.destroy()

#Metodo de Formulario de login
def Login():
    global admin_id, lbl_result
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="FAVOR ENTRAR COM OS CAMPOS VALIDOS, TENTE NOVAMENTE!", fg="red", font=('Arial', 10))
    else:
        cursor.execute("select * from admin where username = ? and password = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("select * from admin where username = ? and password = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("admin")
            PASSWORD.set("admin")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="USUÁRIO OU SENHA INVÁLIDAS", fg="red")
        USERNAME.set("admin")
        PASSWORD.set("admin")
    cursor.close()
    conn.close()

def ShowHome():
    global home
    root.withdraw()  # Esconde a janela principal (root)
    home.deiconify()


#Criando o metodo sair do botao
def Exit():
    result = tkMessageBox.askquestion('CADASTRO DE CURRÍCULOS', 'TEM CERTEZA? SAINDO DO SISTEMA', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

#Criando o menu para login
menubor =Menu(root)
filemenu =Menu(menubor, tearoff=0)
filemenu.add_command(label="ENTRAR", command=ShowLoginForm)
filemenu.add_command(label="SAIR", command=EXIT)
menubor.add_cascade(label="ARQUIVOS", menu=filemenu)
root.configure(menu=menubor)

productmenu = Menu(menubor, tearoff=0)
productmenu.add_command(label="Novo Cadastro", command=ShowAddNew)
productmenu.add_command(label="Visualizar", command=ShoView)
menubor.add_cascade(label="Cadastro", menu=productmenu)

# Adicione um novo item de menu para a aba de currículos
resumemenu = Menu(menubor, tearoff=0)
resumemenu.add_command(label="Cadastrar Currículo", command=SwitchToResume)
menubor.add_cascade(label="Currículos", menu=resumemenu)

root.configure(menu=menubor)
#Criando o Frame seja bem vindo ao sistema cadastro de produtos
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

#Criando label cadastro de produtos
lbl_display = Label(Title, text="CADASTRO DE CURRÍCULOS", bg="SlateGray1", font=('Arial', 45))
lbl_display.pack()

home = home()
#Criando MainLoop
if __name__ == '__main__':
    root.mainloop()
      
