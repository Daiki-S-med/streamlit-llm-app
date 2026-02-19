from dotenv import load_dotenv
import os
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.5)
import streamlit as st

st.title('サンプルLLMアプリ')
st.write('##### 動作1: 脳神経外科領域に関する質問')
st.write('入力フォームに質問内容を入力し、「送信」ボタンを押すと、脳神経外科領域に関する質問ができます。')
st.write('#### 動作2: 生成AIに関する質問')
st.write('入力フォームに質問内容を入力し、「送信」ボタンを押すと、生成AIに関する質問ができます。')

selected_item = st.radio('どちらか選択してください。',
                         ['脳神経外科領域に関する質問',
                          '生成AIに関する質問'
                         ])

st.divider()

if selected_item == '脳神経外科領域に関する質問':
    input_message = st.text_input(label="脳神経外科領域に関する質問を入力してください。")
else:
    input_message = st.text_input(label="生成AIに関する質問を入力してください。")

if st.button('送信'):
    st.divider()
    
    if input_message:
        if selected_item == '脳神経外科領域に関する質問':
            messages = [
                SystemMessage(content="あなたは脳神経外科領域の専門家であり、質問に対して適切に答えることが求められます。"),
                HumanMessage(content=input_message)
            ]
        else:
            messages = [
                SystemMessage(content="あなたは生成AIの専門家であり、質問に対して適切に答えることが求められます。"),
                HumanMessage(content=input_message)
            ]
        
        
        answer = llm.invoke(messages)
        st.write(answer.content)
    else:
        st.write('質問内容を入力してから「送信」ボタンを押してください。')
