# AmbedkarGPT-Intern-Assignment
required to build a simple command-line Q&amp;A system. The system will ingest the text from a provided short speech by Dr. B.R. Ambedkar and answer questions based solely on that content.
AmbedkarGPT-Intern-Task

AI Intern Hiring Assignment (Phase 1) Kalpit Pvt Ltd, UK

📋 Project Overview

AmbedkarGPT is a command-line Q&A system developed as part of the Core Skills Evaluation for the AI Intern position.

The system implements a Retrieval-Augmented Generation (RAG) pipeline to ingest a speech by Dr. B.R. Ambedkar ("Annihilation of Caste") and answers user questions based solely on that content, ensuring accurate and context-aware responses without hallucination.

🛠️ Technical Architecture

Per the assignment requirements, the solution is built using the following stack:

Language: Python 3.8+ (Developed & Tested on Python 3.11)

Framework: LangChain (for RAG orchestration)

Vector Store: ChromaDB (Local, open-source)

Embeddings: HuggingFaceEmbeddings (Model: sentence-transformers/all-MiniLM-L6-v2)

LLM: Ollama running mistral (7B parameter model)

Workflow

Load: Ingests text from speech.txt.

Split: Chunks text into 500-character segments using CharacterTextSplitter.

Embed: Generates vector embeddings using HuggingFace models.

Store: Persists vectors locally in chroma_db.

Retrieve: Queries the vector store for relevant context.

Answer: Passes context + question to Mistral 7B for the final answer.

📂 Repository Structure

AmbedkarGPT-Intern-Task/
│
├── main.py              # Core script containing the RAG pipeline
├── speech.txt           # The provided source text (Dr. Ambedkar's speech)
├── requirements.txt     # List of all dependencies
├── README.md            # Documentation (This file)
└── chroma_db/           # (Auto-generated) Local vector store directory


⚙️ Setup & Execution

1. Prerequisites

Python 3.8+ installed.

Ollama installed and running.

2. Model Setup

Open your terminal/command prompt and ensure the Mistral model is pulled:

ollama pull mistral


Ensure the Ollama server is running (ollama serve).

3. Installation

Clone this repository and install the required dependencies:

git clone [https://github.com/](https://github.com/)<your-username>/AmbedkarGPT-Intern-Task.git
cd AmbedkarGPT-Intern-Task

# Create virtual environment (Recommended)
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt


4. Running the Application

python main.py


🧪 Sample Interaction

--- AmbedkarGPT: RAG Prototype Initialization ---

[1/5] Loading speech.txt...
      ✅ File loaded successfully.
[2/5] Splitting text into chunks...
      ✅ Created 5 chunks.
[3/5] Creating embeddings and storing in ChromaDB...
      ✅ Vector store ready.
[4/5] Connecting to Ollama (mistral)...
[5/5] Building Retrieval Pipeline...

✅ SYSTEM READY! 

👉 Your Question: What is the real enemy?
   Thinking...

------------------------------------------------------------
🤖 Answer: According to the text, the real enemy is the belief in the shastras.
------------------------------------------------------------


📦 Deliverables Checklist

[x] main.py: Well-commented Python code implementing the RAG pipeline.

[x] requirements.txt: All dependencies listed.

[x] README.md: Detailed setup and execution instructions.

[x] speech.txt: The provided excerpt from "Annihilation of Caste".

👤 Author

Murahari Chavali AI Intern Applicant
