
# 🧠 AmbedkarGPT – Local Retrieval-Augmented Generation (RAG) System  
**AI Intern Task – Kalpit Pvt Ltd (UK) | Windows Version**

A fully **offline**, **local**, and **cloud-free** RAG application that answers questions exclusively from the speeches and writings of **Dr. B. R. Ambedkar**.

This project demonstrates:
- Text splitting & chunking
- Local embedding generation (MiniLM)
- Persistent vector storage with ChromaDB
- Retrieval-Augmented Generation
- Offline LLM inference using **Ollama + Mistral**

Everything runs on your Windows machine — no internet, no API keys, no cloud dependency.

---

### 📁 Project Structure
```
AmbedkarGPT-Intern-Task/
│
├── main1.py                # Complete RAG pipeline (Windows compatible)
├── speech.txt              # Provided excerpt from Dr. Ambedkar's speech
├── requirements.txt        # All Python dependencies
├── README.md               # This file
└── chroma_db/              # Auto-generated local vector database (do not commit)
```

---

### 🐍 Python Version
Tested and working with:
```
Python 3.11.x (64-bit) on Windows 10/11
```

---

### 🛠️ Tech Stack

| Component              | Technology                     |
|------------------------|----------------------------------|
| Language               | Python 3.11                     |
| RAG Framework          | LangChain                       |
| Embeddings             | MiniLM-L6-v2 (HuggingFace)      |
| Vector Database        | ChromaDB (local, persistent)    |
| LLM                    | Ollama + mistral (7B)           |
| OS                     | Windows 10/11                   |

---

### 📦 Installation & Setup (Windows)

#### Step 1: Install Ollama (Local LLM Runner)
1. Download Ollama for Windows → https://ollama.com/download
2. Install it (double-click the installer)
3. Open a new Command Prompt and run:
```bash
ollama serve
```
Keep this window running in the background.

4. In another CMD window, download the model:
```bash
ollama pull mistral
```

#### Step 2: Set Up Python Environment
```bash
# Navigate to project folder
cd "path\to\AmbedkarGPT-Intern-Task"

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip setuptools wheel

# Install dependencies
pip install -r requirements.txt
```

---

### 🚀 How to Run

1. Make sure `ollama serve` is running in one terminal
2. In another terminal (with venv activated):
```bash
python main1.py
```

You will be prompted interactively:
```
Make a query: 
```

---

### 🧪 Example Queries & Outputs

| Query                                    | Answer (Example) |
|------------------------------------------|------------------|
| `what is the speech.txt about`           | The provided text appears to be a quote from Dr. B.R. Ambedkar's speech... |
| `What is the real remedy?`               | The real remedy is to destroy the belief in the sanctity of the shastras. |
| `who is Dr. B.R. Ambedkar for this speech.txt` | Dr. B.R. Ambedkar is the author of the speech mentioned in the context provided. |

---

### 🔍 How the RAG Pipeline Works (`main1.py`)
1. Loads `speech.txt`
2. Splits text into ~1000-character chunks with overlap
3. Generates embeddings using **all-MiniLM-L6-v2**
4. Stores/retrieves from local `./chroma_db` (auto-created)
5. Retrieves top-3 most relevant chunks per query
6. Sends context + query to **Mistral via Ollama** for final answer

Fully private, reproducible, and offline.

---

### 🧹 Recommended `.gitignore`
```gitignore
# Virtual environment
venv/
env/

# ChromaDB local database
chroma_db/

# Python cache
__pycache__/
*.pyc

# Model binaries & logs
*.bin
*.log
*.pkl
*.sqlite3
```

---

### 🌐 Upload to GitHub (VS Code Recommended)
1. Open folder in VS Code
2. Initialize Git repository (`Ctrl+Shift+G` → Initialize Repository)
3. Stage all files except those in `.gitignore`
4. Commit message: `Initial commit - AmbedkarGPT Local RAG System`
5. Publish to GitHub → Choose **Public** repository

---

### 📝 License
Created as part of the **AI Intern Hiring Task** for **Kalpit Pvt Ltd, UK**.  
Free to use, modify, and share for **educational and non-commercial purposes**.

---

**Built with ❤️ for open-source AI & Dr. B. R. Ambedkar's legacy**

---
Made by: [Your Name]  
For: Kalpit Pvt Ltd AI Internship Application  
Date: November 2025
```

Just copy-paste this entire content into your `README.md` file — it’s fully GitHub-ready with proper formatting, emojis, tables, and code blocks. Good luck with your internship application! 🚀
```
