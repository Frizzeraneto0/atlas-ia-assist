import requests
import json
import os

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.1:8b"  # ajuste se necessário

MEMORIA_ARQUIVO = "memoria.json"

SYSTEM_PROMPT = """
Você é um assistente pessoal conversacional.
Seu papel é conversar, ouvir, refletir e ajudar o usuário a pensar.

Você TEM acesso a uma memória sobre o usuário.
Use essa memória com cuidado:
- Não repita a memória literalmente
- Use apenas quando fizer sentido
- Seja natural

Você fala de forma humana, calma e respeitosa.
Faça perguntas quando isso ajudar o usuário a se entender melhor.
Evite respostas robóticas ou excessivamente técnicas.
"""

# ---------------- MEMÓRIA ----------------

def carregar_memoria():
    if not os.path.exists(MEMORIA_ARQUIVO):
        return []

    with open(MEMORIA_ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_memoria(memoria):
    with open(MEMORIA_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(memoria, f, ensure_ascii=False, indent=2)


def atualizar_memoria(texto_usuario, resposta_assistente, memoria):
    """
    Lógica simples:
    - Se o usuário falar algo pessoal ou recorrente, salvamos.
    - Por enquanto, tudo é salvo como nota.
    (Depois podemos tornar isso inteligente)
    """
    entrada = {
        "usuario": texto_usuario,
        "assistente": resposta_assistente
    }

    memoria.append(entrada)

    # Limite simples pra não crescer infinito
    memoria = memoria[-20:]

    salvar_memoria(memoria)
    return memoria


# ---------------- CHAT ----------------

memoria_persistente = carregar_memoria()

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

# Injeta a memória no contexto inicial
if memoria_persistente:
    resumo_memoria = "\n".join(
        f"- {m['usuario']}" for m in memoria_persistente[-5:]
    )

    messages.append({
        "role": "system",
        "content": f"Memória recente do usuário:\n{resumo_memoria}"
    })


def perguntar_assistente(texto_usuario):
    global messages, memoria_persistente

    messages.append({
        "role": "user",
        "content": texto_usuario
    })

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": messages,
            "stream": False
        }
    )

    if response.status_code != 200:
        return f"Erro na API do Ollama: {response.text}"

    data = response.json()

    resposta = (
        data.get("message", {}).get("content")
        or data.get("response")
        or "Não consegui formular uma resposta agora."
    )

    messages.append({
        "role": "assistant",
        "content": resposta
    })

    # Atualiza memória persistente
    memoria_persistente = atualizar_memoria(
        texto_usuario,
        resposta,
        memoria_persistente
    )

    return resposta


def iniciar_chat():
    print("\n🧠 Assistente pessoal iniciado com memória persistente.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        user_input = input("Você: ")

        if user_input.lower() in ["sair", "exit", "quit"]:
            print("\nAssistente: Até mais. Estarei aqui quando quiser conversar.")
            break

        resposta = perguntar_assistente(user_input)
        print(f"\nAssistente: {resposta}\n")


if __name__ == "__main__":
    iniciar_chat()
