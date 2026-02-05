# Simple AI Agent with Ollama (Local LLM)

Project ini adalah AI Agent sederhana yang berjalan **100% lokal** menggunakan **Python** dan **Ollama** tanpa API key dan tanpa koneksi internet setelah model terunduh.

Agent ini bukan sekadar chatbot. Ia dirancang dengan **system prompt** sehingga mampu:
- Melakukan reasoning langkah demi langkah
- Menjawab dengan struktur yang jelas
- Menyimpan konteks percakapan (memory)
- Mudah dikembangkan menjadi AI Assistant atau AI Tool

---

## Fitur Utama

- Berjalan sepenuhnya offline
- Tanpa API key
- Memory percakapan
- Mudah ganti model (llama3, mistral, gemma, dll)
- Kode sangat sederhana dan mudah dipahami
- Cocok untuk belajar konsep AI Agent dasar

---

## Teknologi yang Digunakan

- Python 3.10+
- Ollama
- Model default: `llama3`

---

## Prasyarat

Pastikan sudah terinstall:

- Python
- Ollama

Cek dengan:
```bash```
python --version
ollama --version


*Instalasi
1. Install Ollama

Unduh dari:
https://ollama.com

2. Download Model LLM
ollama run llama3


Tunggu sampai selesai download, lalu keluar dengan Ctrl + C.

Cek model tersedia:

ollama list

3. Install Library Python

Masuk ke folder project:

python -m pip install ollama

Struktur Project
Simple-Ollama-Agent/
│
├── agent.py
└── README.md

Kode agent.py
import ollama

SYSTEM_PROMPT = """
You are an AI Agent.
Think step by step before answering.
Break down the problem, reason, then answer clearly.
"""

messages = [{"role": "system", "content": SYSTEM_PROMPT}]

def agent(question):
    messages.append({"role": "user", "content": question})

    response = ollama.chat(
        model="llama3",
        messages=messages
    )

    messages.append(response["message"])
    return response["message"]["content"]


if __name__ == "__main__":
    print("Simple Ollama AI Agent (type 'exit' to quit)\n")

    while True:
        q = input("You: ")
        if q.lower() == "exit":
            break

        answer = agent(q)
        print("\nAgent:\n", answer, "\n")

Menjalankan Program
python agent.py


Contoh:

You: Buatkan rencana belajar Python 30 hari
You: Jelaskan OOP dengan sederhana
You: exit

Mengganti Model

Ubah bagian ini di agent.py:

model="llama3"


Menjadi:

model="mistral"
model="gemma:7b"
model="phi"


Pastikan model sudah diunduh melalui Ollama.
