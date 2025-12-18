# atlas-ia-assist

# 🧠 Atlas IA Assist

**Atlas IA Assist** é um assistente pessoal conversacional construído com modelos LLaMA rodando localmente via Ollama. O foco do projeto é **conversa, escuta, reflexão e acompanhamento do usuário**, sem automações de trabalho ou foco em dados corporativos.

Atlas não é um bot de tarefas. Ele é um **companheiro de diálogo**, projetado para ajudar o usuário a pensar, organizar ideias e lidar com decisões do dia a dia.

---

## ✨ Filosofia do Projeto

Atlas foi pensado com alguns princípios claros:

- 🤝 **Presença antes de produtividade**
- 🧠 **Memória com cuidado e contexto**
- 🗣️ **Linguagem humana, calma e respeitosa**
- ❌ Nada de respostas robóticas ou técnicas sem necessidade
- 🔒 Execução local, respeitando privacidade

Atlas não substitui decisões. Ele **caminha junto** enquanto você as constrói.

---

## 🚀 Funcionalidades Atuais

- ✅ Chat conversacional via terminal
- ✅ Integração com **Ollama** (LLaMA local)
- ✅ **Memória persistente** em arquivo JSON
- ✅ Contexto inicial com histórico recente
- ✅ Prompt de sistema com identidade do assistente

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Ollama** (execução local de LLMs)
- **Modelo LLaMA** (ex: `llama3`, `llama3.1` – conforme memória disponível)
- **Requests** (comunicação HTTP)
- **JSON** (persistência de memória)

---

## 📁 Estrutura do Projeto

```text
atlas_ia_assist/
│
├── llamaIA.py           # Script principal do assistente
├── memoria.json         # Memória persistente do usuário
├── README.md            # Documentação do projeto
└── requirements.txt     # Dependências (opcional)
```

---

## ⚙️ Pré-requisitos

1. **Python instalado** (recomendado 3.10+)
2. **Ollama instalado e rodando**
3. Modelo LLaMA baixado

Exemplo:

```bash
ollama pull llama3
ollama run llama3
```

⚠️ Importante: o Ollama **precisa estar aberto** para o Atlas funcionar.

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/atlas_ia_assist.git
cd atlas_ia_assist
```

2. (Opcional) Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Instale as dependências

```bash
pip install requests
```

4. Execute o assistente

```bash
python llamaIA.py
```

---

## 🧠 Como Funciona a Memória

A memória do Atlas:

- É armazenada em `memoria.json`
- Guarda interações recentes
- É reinjetada no contexto inicial do modelo
- Tem limite para evitar crescimento infinito

⚠️ Atualmente a memória é **simples e literal**. Evoluções futuras tornarão isso mais inteligente.

---

## 🗺️ Roadmap (Próximos Passos)

### Curto Prazo

- [ ] Separação de memória (fatos, preferências, emoções)
- [ ] Resumo automático da memória
- [ ] Arquivo de persona (`atlas_persona.txt`)

### Médio Prazo

- [ ] Entrada por voz (speech-to-text)
- [ ] Resposta falada (text-to-speech)
- [ ] Detecção de temas recorrentes

### Longo Prazo

- [ ] Memória semântica (embeddings)
- [ ] Interface gráfica simples
- [ ] Modo diário / reflexivo

---

## 🧩 Exemplo de Uso

```text
Você: estou meio confuso com algumas decisões

Atlas: Quer me contar o que está pesando mais agora? Às vezes organizar em palavras já ajuda a clarear.
```

---

## 🔒 Privacidade

- Atlas roda **100% local**
- Nenhuma conversa é enviada para serviços externos
- Toda a memória fica no seu computador

---

## 🤝 Contribuições

Este projeto nasceu como um assistente pessoal, mas contribuições são bem-vindas:

- Ideias
- Melhorias na memória
- Ajustes de prompt
- Evoluções de UX

---

## 📜 Licença

Defina a licença conforme sua preferência (MIT, Apache, GPL, etc).

---

## 🌍 Nome do Projeto

**Atlas IA Assist**

> Um assistente que ajuda a sustentar pensamentos, não a substituí-los.
