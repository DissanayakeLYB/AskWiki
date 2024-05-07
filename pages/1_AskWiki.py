import os
from dotenv import load_dotenv

#load_dotenv()

import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.utilities import WikipediaAPIWrapper
from langchain_groq import ChatGroq
from groq import Groq


st.set_page_config(
    page_title = "AskWiki",
    page_icon = "💬",
    initial_sidebar_state = 'auto',
    menu_items = {
        "Report a Bug" : "mailto:lasithdissanayake.official@gmail.com",
        "About" : "https://dissanayakelyb.github.io/LasithDissanayake.github.io/"
    }
)

groq_api_key = st.sidebar.text_input("Enter the GROQ API :")

# app framework
st.title("AskWiki")
prompt = st.chat_input("Mention 'ONLY' the topic you need in Wikipedia...")

with st.sidebar:

    model = st.selectbox(
        'Choose a model',
        ['llama3-8b-8192', 'mixtral-8x7b-32768', 'gemma-7b-it', 'llama3-70b-8192']
    )

    reset = st.button(
         label = "Reset",
         type="primary"
        )
    
# prompt templates
respond_template = PromptTemplate(
    input_variables = ['topic', 'wikipedia_research'],
    template = "Write a well organized description about the {topic} using {wikipedia_research}. If you do not have any information on {wikipedia_research} about {topic}, then reply with 'Sorry, I couldn't find any details in Wikipedia under {topic}."
)

reference_template = PromptTemplate(
    input_variables = ['topic'],
    template = "Write 20 suitable website links that explains or are under the topic,  {topic}."
)

if groq_api_key:
    # llms
    llm = ChatGroq(
        api_key=groq_api_key,
        model_name=model,
        temperature=0
    )
    respond_chain = LLMChain(llm=llm, prompt=respond_template, verbose=True)
    reference_chain = LLMChain(llm=llm, prompt=reference_template, verbose=True)

    wiki = WikipediaAPIWrapper()

    # response
    if prompt:
        wiki_research = wiki.run(prompt)
        response = respond_chain.run(topic=prompt, wikipedia_research = wiki_research)
        references = reference_chain.run(topic=prompt)

        st.write("From Wikipedia")
        st.write(response)

        with st.expander('For more information') :
            st.write(references)   

            



st.write("&copy; Lasith Dissanayake | 2024")