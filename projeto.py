import tkinter as tk
import sqlite3
from tkinter import filedialog, ttk, messagebox


# Função para salvar ou atualizar os dados no banco de dados
def salvar_atualizar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    cidade = entry_cidade.get()
    estado = entry_estado.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    experiencias = text_experiencias.get("1.0", tk.END)
    curriculo_path = entry_curriculo_path.get()

    situacao_empregaticia = situacao_empregaticia_var.get()  # Variável corrigida
    faixa_salarial = entry_faixa_salarial.get()  # Obter a faixa salarial

    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM cadastros WHERE nome = ?', (nome,))
    existing_user = cursor.fetchone()

    if existing_user:
        cursor.execute('''
            UPDATE cadastros
            SET idade=?, cidade=?, estado=?, telefone=?, email=?, experiencias=?, situacao_empregaticia=?, faixa_salarial=?, curriculo_path=?
            WHERE nome=?
        ''', (idade, cidade, estado, telefone, email, experiencias, situacao_empregaticia, faixa_salarial, curriculo_path, nome))
        conn.commit()
        conn.close()
        tk.messagebox.showinfo("Sucesso", "Cadastro atualizado com sucesso!")
    else:
        cursor.execute('''
            INSERT INTO cadastros VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nome, idade, cidade, estado, telefone, email, experiencias, situacao_empregaticia, faixa_salarial, curriculo_path))
        conn.commit()
        conn.close()
        tk.messagebox.showinfo("Sucesso", "Cadastro salvo com sucesso!")

    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_estado.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    text_experiencias.delete("1.0", tk.END)
    situacao_empregaticia_menu.set("Selecione uma opção")
    entry_faixa_salarial.delete(0, tk.END)
    entry_curriculo_path.delete(0, tk.END)
    entry_curriculo_path.insert(0, curriculo_path)

def baixar_curriculo():
    selected_index = listbox_nomes.curselection()
    
    if selected_index:
        nome_selecionado = listbox_nomes.get(selected_index[0])

        conn = sqlite3.connect('cadastro.db')
        cursor = conn.cursor()

        cursor.execute('SELECT curriculo_path, curriculo FROM cadastros WHERE nome = ?', (nome_selecionado,))
        curriculo_data = cursor.fetchone()

        if curriculo_data:
            curriculo_path = curriculo_data[0]
            curriculo_bytes = curriculo_data[1]

            with open(curriculo_path, 'wb') as file:
                file.write(curriculo_bytes)

            tk.messagebox.showinfo("Sucesso", "Currículo baixado com sucesso!")

        conn.close()


# Função para selecionar o arquivo do currículo
def selecionar_curriculo():
    curriculo_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf"), ("Word Files", "*.docx")])

    if curriculo_path:
        entry_curriculo_path.delete(0, tk.END)
        entry_curriculo_path.insert(0, curriculo_path)

    # Limpar o menu suspenso e exibir o caminho selecionado
    situacao_empregaticia_menu.set("Selecione uma opção")

    # Função para configurar o caminho do currículo quando uma seleção for feita
    def set_curriculo_path(event):
        selected_curriculo = curriculo_selecionado.get()
        entry_curriculo_path.delete(0, tk.END)
        entry_curriculo_path.insert(0, selected_curriculo)

  
    def confirmar_selecao():
        selecionado = curriculo_selecionado.get()
        if selecionado != "Selecione um currículo":
            entry_curriculo_path.delete(0, tk.END)
            entry_curriculo_path.insert(0, selecionado.split(": ")[1])
        
    

# Função para carregar os dados de um usuário existente
def carregar_dados(event):
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()

    selected_index = listbox_nomes.curselection()
    
    if selected_index:
        nome_selecionado = listbox_nomes.get(selected_index[0])
        
        cursor.execute('SELECT * FROM cadastros WHERE nome = ?', (nome_selecionado,))
        user_data = cursor.fetchone()

        if user_data:
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, nome_selecionado)
            entry_idade.delete(0, tk.END)
            entry_idade.insert(0, user_data[1])
            entry_cidade.delete(0, tk.END)
            entry_cidade.insert(0, user_data[2])
            entry_estado.delete(0, tk.END)
            entry_estado.insert(0, user_data[3])
            entry_telefone.delete(0, tk.END)
            entry_telefone.insert(0, user_data[4])
            entry_email.delete(0, tk.END)
            entry_email.insert(0, user_data[5])
            text_experiencias.delete("1.0", tk.END)
            text_experiencias.insert(tk.END, user_data[6])
            situacao_empregaticia_menu.set(user_data[7])  # Define a opção do menu suspenso
            entry_curriculo_path.delete(0, tk.END)
            entry_curriculo_path.insert(0, user_data[8])

    conn.close()

root = tk.Tk()
root.title("Cadastro de Usuários")
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

cadastro_frame = ttk.Frame(notebook)
notebook.add(cadastro_frame, text="Cadastro")

label_nome = tk.Label(cadastro_frame, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(cadastro_frame)
entry_nome.pack()

label_idade = tk.Label(cadastro_frame, text="Idade:")
label_idade.pack()
entry_idade = tk.Entry(cadastro_frame)
entry_idade.pack()

label_cidade = tk.Label(cadastro_frame, text="Cidade:")
label_cidade.pack()
entry_cidade = tk.Entry(cadastro_frame)
entry_cidade.pack()

label_estado = tk.Label(cadastro_frame, text="Estado:")
label_estado.pack()
entry_estado = tk.Entry(cadastro_frame)
entry_estado.pack()

label_telefone = tk.Label(cadastro_frame, text="Telefone:")
label_telefone.pack()
entry_telefone = tk.Entry(cadastro_frame)
entry_telefone.pack()

label_email = tk.Label(cadastro_frame, text="E-mail:")
label_email.pack()
entry_email = tk.Entry(cadastro_frame)
entry_email.pack()

label_experiencias = tk.Label(cadastro_frame, text="Experiências:")
label_experiencias.pack()
text_experiencias = tk.Text(cadastro_frame, height=5, width=30)
text_experiencias.pack()

label_situacao_empregaticia = tk.Label(cadastro_frame, text="Situação Empregatícia:")
label_situacao_empregaticia.pack()

# Crie um menu suspenso para a escolha da situação empregatícia
situacao_empregaticia_var = tk.StringVar()
situacao_empregaticia_menu = ttk.Combobox(cadastro_frame, textvariable=situacao_empregaticia_var)
situacao_empregaticia_menu['values'] = ("Empregado", "Desempregado")
situacao_empregaticia_menu.set("Selecione uma opção")
situacao_empregaticia_menu.pack()

label_faixa_salarial = tk.Label(cadastro_frame, text="Faixa Salarial:")
label_faixa_salarial.pack()
entry_faixa_salarial = tk.Entry(cadastro_frame)
entry_faixa_salarial.pack()


btn_selecionar_curriculo = tk.Button(cadastro_frame, text="Selecionar Currículo", command=selecionar_curriculo)
btn_selecionar_curriculo.pack()

entry_curriculo_path = tk.Entry(cadastro_frame)
entry_curriculo_path.pack()

btn_salvar_atualizar = tk.Button(cadastro_frame, text="Salvar/Atualizar Dados", command=salvar_atualizar_dados)
btn_salvar_atualizar.pack()

consulta_frame = ttk.Frame(notebook)
notebook.add(consulta_frame, text="Consulta")

listbox_nomes = tk.Listbox(consulta_frame)
listbox_nomes.pack(fill=tk.BOTH, expand=True)

conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()
cursor.execute('SELECT nome FROM cadastros')
nomes = cursor.fetchall()
for nome in nomes:
    listbox_nomes.insert(tk.END, nome[0])

listbox_nomes.bind("<<ListboxSelect>>", carregar_dados)

conn.close()

root.mainloop()