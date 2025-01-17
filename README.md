# GPTInterface

## Table of Contents

1. [Introduction](#1-introduction)  
2. [Files in the Repository](#2-files-in-the-repository)  
3. [Technologies and Techniques Used](#3-technologies-and-techniques-used)  
4. [Setup and Execution](#4-setup-and-execution)  
5. [Usage](#5-usage)  
6. [License](#6-license)  

---

## 1. Introduction

**GPTInterface** is a web-based interface for interacting with GPT models, designed using **Streamlit** for the front-end and **LangChain** for managing the conversational pipeline. The project also integrates web search capabilities using **DuckDuckGo**, allowing the chatbot to retrieve up-to-date information from the web before processing queries through GPT.  

The project is containerized using **Docker**, ensuring an isolated and portable environment for deployment.

---

## 2. Files in the Repository

- **`app.py`**: Contains the main implementation of the web interface and GPT integration.  
- **`Dockerfile`**: Defines the environment and dependencies for running the project in a Docker container.  
- **`requirements.txt`**: Lists all the required Python libraries for the project.  

---

## 3. Technologies and Techniques Used

- **Streamlit**: Framework for building the web interface.  
- **LangChain**: Provides a conversational structure and memory for managing interactions with GPT.  
- **Docker**: Containerizes the project for easy deployment and consistency.  
- **DuckDuckGo Search**: Implements web search functionality to retrieve external information.  

### Key Features
1. **Web-Based Interface**:  
   - User-friendly interface for chatting with GPT.  
   - Sidebar for inputting the OpenAI API key and resetting the chat.

2. **External Search Integration**:  
   - Uses DuckDuckGo to fetch up-to-date information, expanding GPT's knowledge base.  

3. **Dockerized Deployment**:  
   - Ensures a consistent and reproducible environment.  

---

## 4. Setup and Execution

### Prerequisites
1. Install **Docker Desktop** on your machine.  

### Steps

2. Build the Docker image:
  ```bash
    docker build -t gpt-interface .
  ```
3. Run the Docker Container:
  ``` bash
    docker run --name chatgpt -d -p 8501:8501 gpt-interface
  ```
4. Open your browser and navigate to:
  `http://localhost:8501`

## 5. Usage
How to Use
1. Open the web interface at `http://localhost:8501`.
2. Enter your OpenAI API Key in the sidebar.
3. Ask questions in the chat input.
4. View responses generated by GPT, enhanced with web search results when applicable.

## 6. License
This project is licensed under the [MIT License](LICENSE).
