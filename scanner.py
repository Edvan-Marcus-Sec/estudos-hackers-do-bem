import socket

# Alvo que vamos testar (pode ser um IP da sua rede ou site)
alvo = input("Digite o endereço (URL ou IP) para escanear: ") 
# Lista de portas que queremos checar
portas = [21, 22, 23, 80, 443, 8080]

print(f"\033[1;32m[+]\033[0m Testando porta {portas}...")

for porta in portas:
    # AF_INET = IPV4 | SOCK_STREAM = TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # Espera 1 segundo por resposta
    
    # Tenta a conexão
    resultado = s.connect_ex((alvo, porta))
    
    if resultado == 0:
        print(f"[+] Porta {porta}: ABERTA")
    else:
        print(f"[-] Porta {porta}: FECHADA")
        
    s.close()

print("--- Scan Finalizado ---\n")
