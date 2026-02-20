import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"  # ou "llama3:8b" se o outro não funcionar

def chat(prompt):
    data = {
        "model": MODEL,
        "prompt": prompt
    }
    try:
        response = requests.post(OLLAMA_URL, json=data)
        if response.status_code == 200:
            result = response.json()
            # A resposta de texto normalmente está aqui:
            return result.get("completion", "[Sem resposta]")
        else:
            return f"Erro {response.status_code}: {response.text}"
    except Exception as e:
        return f"Erro de conexão: {e}"

def main():
    print("Mini Ollama Chat (digite 'sair' para encerrar)")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            break
        reply = chat(user_input)
        print("IA:", reply)

if __name__ == "__main__":
    main()