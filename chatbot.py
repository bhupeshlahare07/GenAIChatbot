import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS



#upload pdf files
st.header("My first chatbot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")

#Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for pages in pdf_reader.pages:
        text+= pages.extract_text()
        #st.write(text)

#Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    st.write(chunks)

    # generating embedding
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    # creating vector store - FAISS
    vector_store = FAISS.from_texts(chunks, embeddings)