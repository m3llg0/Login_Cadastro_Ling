import customtkinter

customtkinter.set_appearance_mode("dark")

def Login():
    TelaLogin = customtkinter.CTk()
    TelaLogin.geometry("500x300")

    def lembrar():
        print("Lembrar Login")

    def clique():
        print("Fazer Login")

    texto = customtkinter.CTkLabel(TelaLogin, text="Fazer Login")
    texto.pack(padx=10, pady=10)

    email = customtkinter.CTkEntry(TelaLogin, placeholder_text="Seu e-mail")  # placeholder_text é o texto de orientação do entry
    email.pack(padx=10, pady=10)

    senha = customtkinter.CTkEntry(TelaLogin, placeholder_text="Sua senha", show="*")  # o show é o que ele vai exibir no lugar do que o usuário vai escrever
    senha.pack(padx=10, pady=10)

    checkbox = customtkinter.CTkCheckBox(TelaLogin, text="Lembrar Login", command=lembrar)
    checkbox.pack(padx=10, pady=10)

    botao = customtkinter.CTkButton(TelaLogin, text="Login", command=clique, fg_color="#ff738c", hover_color="#fa4565")
    botao.pack(padx=10, pady=10)

    TelaLogin.mainloop()

def Cadastro():
    TelaCadastro = customtkinter.CTk()
    TelaCadastro.geometry("500x300")

    #adicionar textos, entry e botões

    TelaCadastro.mainloop()

TelaPrincipal = customtkinter.CTk()
TelaPrincipal.geometry("500x300")

texto = customtkinter.CTkLabel(TelaPrincipal, text="Bem vindo ao sistema X!")
texto.pack(padx=10, pady=10)

botao_login = customtkinter.CTkButton(TelaPrincipal, text="Login", command=Login)
botao_login.pack(padx=10, pady=10)

botao_cadastro = customtkinter.CTkButton(TelaPrincipal, text="Cadastro", command=Cadastro)
botao_cadastro.pack(padx=10, pady=10)

TelaPrincipal.mainloop()

