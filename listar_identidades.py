import subprocess

print("\n" + "="*50)
print("🛡️  RELATÓRIO DE IDENTIDADES E PRIVILÉGIOS (IAM)  🛡️")
print("="*50 + "\n")

def listar_usuarios_e_grupos():
    try:
        # Abre o arquivo de usuários do sistema Linux
        with open("/etc/passwd", "r") as f:
            for linha in f:
                partes = linha.split(":")
                usuario = partes[0]
                uid = int(partes[2])
                
                # Filtramos para mostrar o 'root' (UID 0) 
                # e usuários comuns (geralmente UID >= 1000)
                if uid == 0 or uid >= 1000:
                    # Executa o comando 'groups' para ver os privilégios
                    resultado = subprocess.check_output(["groups", usuario]).decode().strip()
                    
                    # Formata a saída
                    print(f"👤 USUÁRIO: {usuario.ljust(15)} | 👥 GRUPOS: {resultado}")
                    
    except Exception as e:
        print(f"❌ Erro ao processar identidades: {e}")

if __name__ == "__main__":
    listar_usuarios_e_grupos()
    print("\n" + "="*50)
    print("✅ Auditoria de Contas Finalizada")
    print("="*50 + "\n")
