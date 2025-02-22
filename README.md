# LAWLOOM🎯


## Basic Details
### Team name: [Nova spec]


### Team Members
- Member 1: [Archana J] - [Ahalia school of engineering and technology]
- Member 2: [Nazna N] - [Ahalia school of engineering and technology]
- Member 3: [Riya Marjum M R] - [Ahalia school of engineering and technology]

### Hosted Project Link
https://github.com/lvxvlmidhu/tink-her-hack-3-temp
### Project Description

 LegalBot is a chatbot designed to assist legal professionals, researchers, and individuals seeking legal advice by delivering accurate and contextual responses to complex legal queries. The chatbot leverages Retrieval-Augmented Generation (RAG) to enhance the quality of its responses, ensuring they are both relevant and well-informed.
With its ability to perform semantic searches and generate responses using Google Generative AI, LegalBot aims to simplify legal research, streamline document analysis, and provide quick access to legal insights
### The Problem statement

The problem being addressed by this project is the lack of accessible and efficient legal assistance for individuals who may not have the resources to consult a lawyer or navigate complex legal systems. Legal research and advice can be time-consuming and expensive, and this bot aims to democratize access to legal information by:
Providing quick and accurate responses to legal queries.
Reducing the dependency on human lawyers for preliminary legal advice.
Making legal information more accessible to the general public.
### The Solution
[The primary objective of the RAG_LegalBot is to provide automated legal assistance by answering user queries related to legal matters. The bot aims to:
Retrieve relevant legal information or case laws from a database.
Generate accurate, concise, and contextually appropriate responses to user queries.
Assist users in understanding legal concepts, finding relevant case laws, or getting guidance on legal procedures.]

## Technical Details
### Technologies/Components Used
For Software:
-NLP Techniques Utilized:
       Semantic Embeddings: Vectorization of text using Hugging Face embeddings.
       Vector Search: Efficient document retrieval using Pinecone.
* Generative AI Integration:
      Uses Google Generative AI (Gemini) for natural language response generation.
             Custom prompt templates for coherent and context-aware outputs.
* Web Framework and Interactive UI:
Built using Flask for backend services.
User-friendly chat interface for smooth interactions

### Implementation
For Software:
1. Storing Legal Documents as Embeddings
Legal documents such as case laws and legal texts are processed into numerical representations (embeddings) using an AI model. These embeddings capture the semantic meaning of the content rather than just keywords. The processed data is then stored in Pinecone, a specialized database optimized for fast similarity searches.

2. Searching and Retrieving Relevant Documents
When a user submits a legal query, it is also converted into an embedding. Pinecone then compares this query embedding with stored document embeddings to find the most relevant matches. The system retrieves the top results, ensuring the response is based on meaning rather than just word occurrence.

3. Generating Contextual Answers
The retrieved documents are used as context for Google Generative AI, which synthesizes a coherent and contextually accurate response to the user’s query. This ensures that the legal response is well-informed and directly relevant to the provided question.

4. Efficiency and Scalability
Pinecone allows the system to handle large volumes of legal documents while maintaining fast search times. The database is continuously updated to ensure the latest legal precedents and texts are available for retrieval. Optimization techniques, such as indexing and efficient query handling, further enhance performance.


# Installation
 
pip install -r requirements.txt
pip install langchain_community
pip install langchain-huggingface
pip install langchain-google-genai
pip install pinecone-client
Pip install flask 


# Run
python app.py

# Screenshots (Add at least 3)
These are demo of our legal chatbot user interface:

https://1drv.ms/i/c/5ffd074a1f11b5b9/EQuytTxn_A9PjW7UO-h0rA0BikU06FbXlho-uQ0n4ceSvQ?e=hoVySR

https://1drv.ms/i/c/5ffd074a1f11b5b9/EZIUdq5q3XZBpaC_qqTzzywBB1naxhV_YvCMVpKHIN5hFQ?e=1AzdML

https://1drv.ms/i/c/5ffd074a1f11b5b9/EeKjAEqPkuhHs9SUCXs5bJ8Bnkqi6f1C5DYIEp1JyhmYKA?e=6yU5BT


### Project Demo
# Video
https://1drv.ms/v/c/5ffd074a1f11b5b9/EVRMzHZehfxIpv-szN8cYggB_h6mcYaTvzH-Wfh4LGA5cw?e=ljLfhm



---
Made with ❤️ at TinkerHub
