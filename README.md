🧠 Simple AI Agent with Ollama (Local LLM)

AI Agent sederhana menggunakan Ollama + Python yang bisa berjalan 100% offline di lokal tanpa API key.

Agent ini:

Menerima pertanyaan dari user

Melakukan reasoning sederhana (step-by-step thinking)

Menjawab seperti AI Agent (bukan sekadar chatbot)

Bisa ditambah memory percakapan

🚀 Teknologi yang Digunakan

Python

Ollama

Model: llama3 (bisa diganti model lain di Ollama)

📦 Instalasi
1. Install Ollama

Download & install dari:
https://ollama.com

Cek berhasil:

ollama --version

2. Download model LLM
ollama run llama3


Tunggu sampai selesai download, lalu keluar dengan Ctrl + C.

3. Install dependency Python
python -m pip install ollama

🗂️ Struktur Project
.
├── agent.py
└── README.md

▶️ Cara Menjalankan
python agent.py


Tampilan:

Simple Ollama AI Agent (type 'exit' to quit)

You:


Ketik pertanyaan, agent akan menjawab.

🧪 Contoh Penggunaan
You: Buatkan rencana belajar Python 30 hari
You: Jelaskan konsep OOP dengan sederhana
You: exit

🧩 Fitur Agent

System prompt khusus agar agent berpikir bertahap

Bisa ditambahkan memory percakapan

Bisa diganti model (mistral, gemma, dll)

Berjalan offline (tanpa internet setelah model terdownload)

🛠️ Kustomisasi Model

Ganti model di agent.py:

model="llama3"


Contoh:

model="mistral"
model="gemma:7b"

🧠 Menambahkan Memory Percakapan

Ubah fungsi agent agar menyimpan history chat sehingga agent “ingat” konteks sebelumnya.

✅ Kelebihan Project Ini

Sangat ringan & sederhana

Tidak perlu API key

Bisa dikembangkan jadi AI Assistant, AI Tool, atau AI Automation

Cocok untuk belajar konsep AI Agent dasar

📌 Catatan

Pastikan Ollama sedang berjalan saat menjalankan agent.py.

Cek dengan:

ollama list

📄 Lisensi

Bebas digunakan untuk pembelajaran dan pengembangan pribadi.
