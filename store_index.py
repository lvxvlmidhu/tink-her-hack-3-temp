from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from src.helper import text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_community.vectorstores.pinecone import Pinecone as Vec
from dotenv import load_dotenv
import os

load_dotenv()

# Load Pinecone API Key
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# Function to load PDF file(s)
def load_pdf_file(data_path):
    if os.path.isfile(data_path):
        # For a single PDF file
        print(f"Loading single PDF file: {data_path}")
        loader = PyPDFLoader(data_path)
        return loader.load()
    elif os.path.isdir(data_path):
        # For a directory of PDF files
        print(f"Loading all PDF files from directory: {data_path}")
        loader = DirectoryLoader(data_path, glob="*.pdf")
        return loader.load()
    else:
        raise ValueError(f"Invalid path provided: '{data_path}'. Must be a file or directory.")

# Specify file or directory path
data_path = "IPC.pdf"  # Update this path accordingly

# Load the PDF data
try:
    extracted_data = load_pdf_file(data_path)
    print(f"Extracted data length: {len(extracted_data)}")  # Debugging
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

# Split the text into chunks
text_chunks = text_split(extracted_data)
print(f"Number of text chunks: {len(text_chunks)}")  # Debugging
if len(text_chunks) == 0:
    print("No text chunks found. Check your data and text splitting logic.")
    exit()

# Download embeddings
embeddings = download_hugging_face_embeddings()
print(f"Embedding model: {embeddings}")  # Debugging

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Create Pinecone index
index_name = "ipc-guide"
try:
    print("Creating Pinecone index...")
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
    print(f"Index '{index_name}' created successfully.")
except Exception as e:
    print(f"Error creating index: {e}")
    exit()

# Upsert data into Pinecone
try:
    print("Upserting data to Pinecone...")
    docsearch = Vec.from_documents(
        documents=text_chunks,
        index_name=index_name,
        embedding=embeddings,
    )
    print("Data upsert complete.")
except Exception as e:
    print(f"Error during upsert: {e}")
