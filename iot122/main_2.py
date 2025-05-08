import socket
import time

# Lista de IPs dos Arduinos
HOST = [
    "192.168.1.177",  # Exemplo adicional
    "192.168.1.10",   # Rafael
    "192.168.1.11",   # Dayane
    "192.168.1.157",  # Rafael
    "192.168.1.167",  # Rian
    "192.168.1.105",  # Kauan
    "192.168.1.174",  # Rodrigo
    "192.168.1.106",  # Diemerson
    "192.168.1.178",  # Davi
    "192.168.1.12"    # Erick
]

PORT = 5000
MAX_TENTATIVAS = 5
TIMEOUT = 5  # segundos

while True:
    try:
        ip = int(input("Escolha de 1 a 10 para Arduino: "))
        if ip < 1 or ip > len(HOST):
            print("Dispositivo inválido! Programa encerrado.")
            break

        # Novos comandos possíveis
        opcao = input("Escolha: 0 (desligar), 1 (ligar), ultra, lcd, temperatura: ").strip().lower()

        if opcao == "1":
            msg = b"ligar\n"
        elif opcao == "0":
            msg = b"desligar\n"
        elif opcao in ("ultra", "distancia"):
            msg = b"distancia\n"
        elif opcao == "lcd":
            msg = b"lcd_on\n"  # Envia o comando para ativar o LCD
        elif opcao == "temperatura":
            msg = b"temperatura\n"  # Envia o comando para ativar o LCD
        elif opcao == "sair":
            print("Encerrando programa.")
            break
        else:
            print("Opção inválida! Programa encerrado.")
            break

        s = None
        for tentativa in range(1, MAX_TENTATIVAS + 1):
            try:
                print(f"Tentando abrir conexão com IP: {HOST[ip - 1]} (tentativa {tentativa})")
                s = socket.create_connection((HOST[ip - 1], PORT), timeout=2)
                print("Conexão aberta.")
                s.settimeout(TIMEOUT)
                s.sendall(msg)
                resposta = s.recv(128).decode().strip()  # aumentamos o buffer
                print(f"Comando executado. Resposta: {resposta}")
                break

            except socket.timeout:
                print(f"Tempo esgotado (tentativa {tentativa}/{MAX_TENTATIVAS}).")
            except OSError as e:
                print(f"Erro de rede: {e} (tentativa {tentativa}/{MAX_TENTATIVAS}).")
            finally:
                if s:
                    s.close()
                    print("Conexão fechada.\n")

    except ValueError:
        print("Entrada inválida. Use apenas números para o IP.")
