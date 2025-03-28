# Import library yang dibutuhkan
import streamlit as st      # Streamlit untuk membuat UI chatbot
from langchain_ollama import ChatOllama     # Model AI dari Ollama untuk chatbot
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage      # Format pesan (manusia, sistem, AI)

st.title("Chatbot")     # Menampilkan judul aplikasi di Streamlit

# Inisialisasi riwayat percakapan jika belum ada
if "messages" not in st.session_state:
    st.session_state.messages = []      # Membuat list kosong untuk menyimpan riwayat pesan

    # Menambahkan pesan sistem sebagai instruksi awal
    st.session_state.messages.append(SystemMessage("You are a helpful AI assistant"))   

# Menampilkan riwayat chat saat aplikasi dijalankan ulang
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):       # Jika pesan berasal dari user
        with st.chat_message("user"):
            st.markdown(message.content)        # Tampilkan pesan user di layar
    elif isinstance(message, AIMessage):        # Jika pesan berasal dari AI
        with st.chat_message("assistant"):
            st.markdown(message.content)        # Tampilkan pesan AI di layar

# Membuat input chat untuk user
prompt = st.chat_input("Hi, how can I help you?")       # Kotak input bagi user untuk mengetik pesan

# Jika user memasukkan prompt
if prompt:

    # Menampilkan pesan user di UI Streamlit
    with st.chat_message("user"):
        st.markdown(prompt)     # Menampilkan teks user di layar

        # Menyimpan pesan user ke dalam riwayat percakapan
        st.session_state.messages.append(HumanMessage(prompt))

    # Membuat model chatbot dengan parameter tertentu
    llm = ChatOllama(
        model="llama3.2",       # Gunakan model Llama3.2 dari Ollama
        temperature=2       # Mengatur tingkat kreativitas model (semakin tinggi, semakin kreatif)
    )

    # AI menghasilkan respons berdasarkan percakapan sebelumnya
    result = llm.invoke(st.session_state.messages).content

    # Menampilkan respons AI di UI Streamlit
    with st.chat_message("assistant"):
        st.markdown(result)     # Menampilkan teks AI di layar

        # Menyimpan pesan AI ke dalam riwayat percakapan
        st.session_state.messages.append(AIMessage(result))