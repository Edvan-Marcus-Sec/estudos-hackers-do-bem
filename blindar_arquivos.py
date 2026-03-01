import os
import stat

# Lista de extensões que queremos proteger
extensoes_criticas = ['.txt', '.json', '.py']

print("--- 🛡️ Iniciando Blindagem de Arquivos ---")

# Lista todos os arquivos na pasta atual
for nome_arquivo in os.listdir('.'):
    if any(nome_arquivo.endswith(ext) for ext in extensoes_criticas):
        # Define a permissão: Somente leitura e escrita para o dono (600)
        # S_IRUSR (Read User) + S_IWUSR (Write User)
        os.chmod(nome_arquivo, stat.S_IRUSR | stat.S_IWUSR)
        print(f"✅ Arquivo [{nome_arquivo}] agora é PRIVADO (chmod 600)")

print("--- 🛡️ Blindagem Concluída ---")
