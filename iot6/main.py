import serial
import time
from banco import Banco

PORTA = "COM3"
ARDUINO = serial.Serial(PORTA, 9600, timeout=1)
time.sleep(2)

ALUNO = "dasilva"
LED = 1
banco = Banco()
banco.criar_tabela()

while True:
    estado = banco.ler_estado(ALUNO)
    print(f"esse eh o estado do meu led: {estado}")
    comando = input("Digite 1 para Ligar o Led e 0 para desligar ou Sair para encerrar o programa: ").upper()
    match comando:
        case "1":
            #ARDUINO.write(b'1')
            estado = "Ligado"
            banco.inserir_ou_atualizar_estado(ALUNO,LED,estado)
            print("LED ligado!")
        case "0":
            #ARDUINO.write(b'0')
            estado = "Desligado"
            banco.inserir_ou_atualizar_estado(ALUNO,LED,estado)
            print("LED Desligado!")
        case "2":
            banco.listar_dados()
        case "SAIR":
            print("Encerrando o Programa...")
            break