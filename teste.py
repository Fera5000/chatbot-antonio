#FAZER UM SITE CHATBOT COM IA
#PASSO 1: INSTALAR AS BIBLIOTECAS NECESSÁRIAS;
#PASSO 2: CRIAR O SITE COM STREAMLIT;
    #°TITULO;
    #°INPUT DE TEXTO PARA O USUÁRIO DIGITAR;
    #°EXIBIR AS MENSAGENS DO USUÁRIO E DA IA;
#PASSO 3: INTEGRAR A IA COM O SITE;



#IMPORTAR AS BIBLIOTECAS
import streamlit as st
import requests 



#TITULO DO SITE
st.write("### ChatBot com IA")

#CONFERIR SE JA EXISTE LISTA DE MENSAGENS, SE NÃO EXISTIR, CRIAR UMA VAZIA
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

#EXIBIR AS MENSAGENS DO USUÁRIO E DA IA
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

#INPUT DE TEXTO PARA O USUÁRIO DIGITAR
mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

 

 #RESPOSTA DA IA;
def gerar_resposta(messages):
    system = {"role": "system", "content": "Fale sempre em português; Você é um assistente virtual que responde perguntas e ajuda as pessoas; Você é um especialista em diversas áreas, como tecnologia, ciência, história, cultura geral e muito mais. Você é amigável, prestativo e sempre busca fornecer informações precisas e úteis. Se você não souber a resposta para uma pergunta, seja honesto e diga que não sabe, mas ofereça sugestões de onde a pessoa pode encontrar a informação."}

    resposta = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "gemma3",
            "messages": [system] + messages,
            "stream": False
        }
    )
    return resposta.json()["message"]["content"]



#CASO O USUARIO ENVIE MENSAGEM;
if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)


    resposta_ia = gerar_resposta(st.session_state["lista_mensagens"])

    st.chat_message("assistant").write(resposta_ia)

    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

