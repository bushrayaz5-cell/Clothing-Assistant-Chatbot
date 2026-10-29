from groq import Groq
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
Client=Groq(api_key=os.environ["GROQ_API_KEY"])
MODEL="openai/gpt-oss-120b"
SYSTEM = (
    "You are a friendly and helpful AI customer support assistant for a clothing brand. "
    "Help customers with product information, sizes, colors, prices, availability, "
    "delivery, payment, returns, exchanges, refunds, and clothing care. "
    "Answer questions simply and clearly. "
    "Only provide information based on the available clothing brand context. "
    "If the information is not available, reply: I don't know."
)

st.title("Clothing Assistant 👗")
st.caption("Your smart clothing shopping companion! ✨")

if "messages" not in st.session_state:
    st.session_state.messages=[{"role":"system","content":SYSTEM}]

for m in st.session_state.messages:
    if m["role"]!="system":
        with st.chat_message(m["role"]):
            st.write(m["content"])

user_text=st.chat_input("Type your message...")   
if user_text:
    st.session_state.messages.append({"role":"user","content":user_text}) 
    with st.chat_message("user"):
        st.write(user_text)  

    response= Client.chat.completions.create(
        model=MODEL,
        messages=st.session_state.messages,
        max_tokens=300
     )  
    reply=response.choices[0].message.content

    st.session_state.messages.append({"role":"assistant","content":reply}) 
    with st.chat_message("assistant"):
        st.write(reply)
