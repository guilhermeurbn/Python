#import requests
import random

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"  # ou "llama3:8b"

historico = []
def ia_jogar():
    if len(historico) < 3:
        return random.choice(["pedra", "papel", "tesoura"])

    pedra = historico.count("pedra")
    papel = historico.count("papel")
    tesoura = historico.count("tesoura")

    if pedra >= papel and pedra >= tesoura:
        return "papel"
    elif papel >= pedra and papel >= tesoura:
        return "tesoura"
    else:
        return "pedra"
    
def decidir_ganhador(usuario, ia):
    if usuario == ia:
        return "Empate!"
    elif (usuario == "pedra" and ia == "tesoura") or \
         (usuario == "papel" and ia == "pedra") or \
         (usuario == "tesoura" and ia == "papel"):
        return "Você ganhou!"
    else:
        return "A IA ganhou!"

def main():
    print("Vamos jogar Pedra, Papel ou Tesoura contra a IA!")
    while True:
        usuario = input("Escolha [pedra, papel, tesoura] ou 'sair' para encerrar: ").lower()
        historico.append(usuario)
        if usuario == "sair":
            break
        if usuario not in ["pedra", "papel", "tesoura"]:
            print("Escolha inválida!")
            continue
        ia = ia_jogar()
        print(f"IA jogou: {ia}")
        print(decidir_ganhador(usuario, ia))
        print("-" * 30)

if __name__ == "__main__":
    main()