import os
import sys
import argparse
from operator import itemgetter

# LangChain Imports
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
# Using standard community embeddings as per assignment constraints (NO API keys)
from langchain_community.embeddings import HuggingFaceEmbeddings 
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

# --- Configuration ---
# The assignment specifically asks for Mistral 7B [cite: 18]
# You can change this to "llama3" if you prefer, as used in your notebook.
OLLAMA_MODEL = "mistral" 
SOURCE_FILE = "speech.txt"
VECTOR_STORE_DIR = "./chroma_db"

def check_requirements():
    """Checks if source file exists."""
    if not os.path.exists(SOURCE_FILE):
        print(f"❌ Error: '{SOURCE_FILE}' not found.")
        print("Please create the file and paste the text from the assignment instructions.")
        sys.exit(1)

def load_and_split_data():
    """
    1. Load the provided text file.
    2. Split the text into manageable chunks.
    [cite: 8, 9]
    """
    print(f"Loading {SOURCE_FILE}...")
    loader = TextLoader(SOURCE_FILE)
    documents = loader.load()
    
    print("Splitting text into chunks...")
    # Using specific chunk settings suitable for short speeches
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    print(f"✅ Created {len(chunks)} text chunks.")
    return chunks

def setup_vectorstore(chunks):
    """
    3. Create Embeddings and store them in a local vector store (ChromaDB).
    Using 'sentence-transformers/all-MiniLM-L6-v2' as requested.
    [cite: 10, 16, 17]
    """
    print("Initializing Embeddings (HuggingFace)...")
    # Suppressing the specific huggingface token warning for local use
    os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print("Creating/Updating Vector Store...")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_STORE_DIR
    )
    print(f"✅ Vector store ready at {VECTOR_STORE_DIR}")
    return vectorstore

def setup_rag_chain(vectorstore):
    """
    4. Retrieve relevant chunks.
    5. Generate answer using Ollama (Mistral).
    [cite: 11, 12, 15]
    """
    print(f"Initializing LLM ({OLLAMA_MODEL})...")
    llm = Ollama(model=OLLAMA_MODEL)

    # Retrieve top 3 most similar chunks
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    template = """You are a helpful AI assistant trained on the speeches of Dr. B.R. Ambedkar.
    Answer the question based ONLY on the following context. 
    If the answer is not in the context, say "I cannot find the answer in the provided text."

    CONTEXT:
    {context}

    QUESTION: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    # LangChain Expression Language (LCEL) Chain
    chain = (
        {
            "context": itemgetter("question") | retriever | RunnableLambda(lambda x: "\n".join(doc.page_content for doc in x)),
            "question": itemgetter("question")
        }
        | prompt
        | llm
    )
    
    return chain

def main():
    print("--- AmbedkarGPT Intern Assignment ---")
    check_requirements()

    # Setup Phase
    chunks = load_and_split_data()
    vectorstore = setup_vectorstore(chunks)
    rag_chain = setup_rag_chain(vectorstore)

    print("\n✅ System Ready! (Type 'exit' or 'quit' to stop)")
    print("-" * 50)

    # Interactive Q&A Loop 
    while True:
        try:
            user_input = input("\nMake a query: ").strip()
            
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting...")
                break
            
            if not user_input:
                continue

            print("Thinking...")
            response = rag_chain.invoke({"question": user_input})
            
            print("\nAnswer:")
            print(response)
            print("-" * 50)

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"❌ Error occurred: {e}")
            print("Make sure Ollama is running: `ollama serve`")

if __name__ == "__main__":
    main()
