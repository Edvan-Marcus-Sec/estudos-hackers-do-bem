import re

def verificar_senha(senha):
    if len(senha) < 8:
        return "❌ Fraca: Menos de 8 caracteres."
    if not re.search("[a-z]", senha):
        return "❌ Fraca: Precisa de letras minúsculas."
    if not re.search("[A-Z]", senha):
        return "❌ Fraca: Precisa de letras maiúsculas."
    if not re.search("[0-9]", senha):
        return "❌ Fraca: Precisa de números."
    
    return "✅ Forte: Senha aprovada pela política!"

senha_teste = input("Digite uma senha para testar a política: ")
print(verificar_senha(senha_teste))
