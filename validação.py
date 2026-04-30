import re
import getpass

# ─────────────────────────────────────────
#  Utilitários de validação
# ─────────────────────────────────────────

def validar_email(email: str) -> bool:
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return bool(re.match(padrao, email))

def validar_telefone(telefone: str) -> bool:
    # Aceita formato: (XX) XXXXX-XXXX  ou  (XX) XXXX-XXXX
    padrao = r'^\(\d{2}\)\s?\d{4,5}-\d{4}$'
    return bool(re.match(padrao, telefone))

def validar_senha(senha: str) -> bool:
    return len(senha) >= 6

# ─────────────────────────────────────────
#  Coleta de dados — Cadastro
# ─────────────────────────────────────────

TIPOS_USUARIO = {
    "1": "Aluno",
    "2": "Ex-Aluno",
    "3": "Funcionário",
}

def coletar_cadastro() -> dict:
    print("\n" + "="*45)
    print("   BIBLIOTECA EREM Dr. Jaime Monteiro")
    print("              CADASTRO")
    print("="*45 + "\n")

    # Nome de usuário
    while True:
        username = input("Nome de usuário: ").strip()
        if username:
            break
        print("  ⚠  Nome de usuário não pode ser vazio.\n")

    # Nome completo
    while True:
        nome_completo = input("Nome completo:   ").strip()
        if nome_completo:
            break
        print("  ⚠  Nome completo não pode ser vazio.\n")

    # E-mail
    while True:
        email = input("E-mail:          ").strip()
        if validar_email(email):
            break
        print("  ⚠  E-mail inválido. Tente novamente.\n")

    # Telefone
    while True:
        telefone = input("Telefone (ex: (81) 99999-9999): ").strip()
        if validar_telefone(telefone):
            break
        print("  ⚠  Formato inválido. Use (XX) XXXXX-XXXX.\n")

    # Senha
    while True:
        senha = getpass.getpass("Senha (mín. 6 caracteres): ")
        if validar_senha(senha):
            break
        print("  ⚠  Senha muito curta.\n")

    # Confirmação de senha
    while True:
        confirmacao = getpass.getpass("Confirme a senha:          ")
        if confirmacao == senha:
            break
        print("  ⚠  As senhas não coincidem.\n")

    # Tipo de usuário
    print("\nTipo de usuário:")
    for chave, valor in TIPOS_USUARIO.items():
        print(f"  [{chave}] {valor}")

    while True:
        escolha = input("Escolha (1/2/3): ").strip()
        if escolha in TIPOS_USUARIO:
            tipo_usuario = TIPOS_USUARIO[escolha]
            break
        print("  ⚠  Opção inválida.\n")

    return {
        "username":      username,
        "nome_completo": nome_completo,
        "email":         email,
        "telefone":      telefone,
        "tipo_usuario":  tipo_usuario,
        # A senha não é armazenada em texto puro em produção;
        # aqui guardamos apenas para confirmação na demo.
        "senha":         senha,
    }

# ─────────────────────────────────────────
#  Coleta de dados — Login
# ─────────────────────────────────────────

def coletar_login() -> dict:
    print("\n" + "="*45)
    print("   BIBLIOTECA EREM Dr. Jaime Monteiro")
    print("              LOGIN")
    print("="*45 + "\n")

    username = input("Nome de usuário: ").strip()
    senha    = getpass.getpass("Senha:           ")

    return {"username": username, "senha": senha}

# ─────────────────────────────────────────
#  Coleta de dados — Recuperação de senha
# ─────────────────────────────────────────

def coletar_recuperacao() -> dict:
    print("\n" + "="*45)
    print("   BIBLIOTECA EREM Dr. Jaime Monteiro")
    print("         RECUPERAR SENHA")
    print("="*45 + "\n")

    while True:
        email = input("E-mail cadastrado: ").strip()
        if validar_email(email):
            break
        print("  ⚠  E-mail inválido. Tente novamente.\n")

    return {"email": email}

# ─────────────────────────────────────────
#  Menu principal
# ─────────────────────────────────────────

def exibir_dados(dados: dict, titulo: str):
    print(f"\n{'─'*45}")
    print(f"  ✅  {titulo} — dados recebidos:")
    print(f"{'─'*45}")
    for campo, valor in dados.items():
        if campo == "senha":
            print(f"  {campo:<15}: {'*' * len(valor)}")
        else:
            print(f"  {campo:<15}: {valor}")
    print(f"{'─'*45}\n")

def menu():
    opcoes = {
        "1": ("Cadastrar-se",       coletar_cadastro,    "Cadastro concluído"),
        "2": ("Login",              coletar_login,       "Login realizado"),
        "3": ("Recuperar Senha",    coletar_recuperacao, "Link enviado para o e-mail"),
        "4": ("Sair",               None,                ""),
    }

    while True:
        print("\n" + "="*45)
        print("   BIBLIOTECA EREM Dr. Jaime Monteiro")
        print("="*45)
        for chave, (label, *_) in opcoes.items():
            print(f"  [{chave}] {label}")

        escolha = input("\nEscolha uma opção: ").strip()

        if escolha == "4":
            print("\n  Até logo! 👋\n")
            break
        elif escolha in opcoes:
            _, funcao, titulo = opcoes[escolha]
            dados = funcao()
            exibir_dados(dados, titulo)
        else:
            print("  ⚠  Opção inválida.\n")

# ─────────────────────────────────────────
#  Ponto de entrada
# ─────────────────────────────────────────

if __name__ == "__main__":
    menu()
