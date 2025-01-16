import json
import requests
import streamlit as st

from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain.agents import ConversationalChatAgent, AgentExecutor  
from langchain_community.chat_message_histories import StreamlitChatMessageHistory 

import warnings
warnings.filterwarnings('ignore')  # Suppresses warnings to keep the output clean

st.set_page_config(page_title = "HOME")  # Sets the page title in the web interface

col1, col4 = st.columns([4, 1])  # Defines a 2-column layout, with col1 taking more space

with col1:
    st.title('GPTInterface - Interface Web with LangChain and GPT')  # Title for the page

openai_api_key = st.sidebar.text_input('OpenAI API Key', type = 'password')  # Sidebar input for API key

msgs = StreamlitChatMessageHistory()  # Initializes chat history to store messages

# Set up memory to track conversation context
memory = ConversationBufferMemory(chat_memory = msgs,
                                  return_messages = True,
                                  memory_key = 'chat_history',
                                  output_key = 'output')

# Reset chat if it's empty or the user clicks 'Reset'
if len(msgs.messages) == 0 or st.sidebar.button('Reset'):
    msgs.clear()
    msgs.add_ai_message('How can I help you?')
    st.session_state.steps = {}

avatars = {'human': 'user', 'ai': 'assistant'}  # Defines avatars for user and assistant

# Loop through all stored messages and display them with associated steps
for idx, msg in enumerate(msgs.messages):
    with st.chat_message(avatars[msg.type]):
        # Display any additional steps associated with the message (e.g., tool usage)
        for step in st.session_state.steps.get(str(idx), []):
            if step[0].tool == '_Exception':  # Skip steps that are errors or exceptions
                continue

            with st.expander(f"✅ **{step[0].tool}**: {step[0].tool_input}"): 
                st.write(step[0].log)  # Display log related to the tool usage
                st.write(f'**{step[1]}**')  # Display the result of the tool

        st.write(msg.content)  # Display the actual message content

# Waits for user input in the chat interface
if prompt := st.chat_input(placeholder = 'Send a message to GPT'):
    st.chat_message('user').write(prompt)  # Display user's message in the chat interface

    if not openai_api_key:  # Check if OpenAI API key is provided
        st.info('Add your OpenAI Key to Continue.')
        st.stop()

    # Initialize OpenAI model with the provided API key and enable streaming
    llm = ChatOpenAI(openai_api_key = openai_api_key, streaming = True)

    # Set up external search tool (DuckDuckGo)
    search_mechanism = [DuckDuckGoSearchRun(name = 'Search')]

    # Create a conversational agent that combines LLM and external tools
    chat_agent = ConversationalChatAgent.from_llm_and_tools(llm = llm, tools = search_mechanism)

    # Executor to handle agent execution and memory management
    executor = AgentExecutor.from_agent_and_tools(agent = chat_agent,
                                                  tools = search_mechanism,
                                                  memory = memory,
                                                  return_intermediate_steps = False,
                                                  handle_parsing_errors = True)  # Handles errors during execution
    
    # Display the AI's response in the chat interface
    with st.chat_message('assistant'):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts = False)  # Manages real-time updates
        response = executor(prompt, callbacks = [st_cb])  # Execute the agent and get response
        st.write(response['output'])  # Display the AI response in the interface