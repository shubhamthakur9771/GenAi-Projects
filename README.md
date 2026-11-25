<div align="center">

# Generative AI Projects

### A hands-on collection of experiments and applications built while learning Generative AI, LLMs, embeddings, chat interfaces, and document processing.

<p>
  <a href="https://github.com/shubhamthakur9771/GenAi-Projects">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub repository">
  </a>
  <img src="https://img.shields.io/badge/Python-Projects-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/LangChain-LLM%20Workflows-1C3C3C?style=for-the-badge" alt="LangChain">
  <img src="https://img.shields.io/badge/Ollama-Local%20Models-black?style=for-the-badge" alt="Ollama">
  <img src="https://img.shields.io/badge/Streamlit-Interactive%20Apps-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
</p>

<p>
  <a href="#overview">Overview</a> ·
  <a href="#projects-and-experiments">Projects</a> ·
  <a href="#technology-stack">Tech Stack</a> ·
  <a href="#setup-and-installation">Setup</a> ·
  <a href="#configuration">Configuration</a>
</p>

</div>

---

## Overview

This repository contains my practical work and experiments with Generative AI using Python. It brings together small applications, model integrations, prompt-based workflows, embedding experiments, and document-processing examples.

The code explores working with hosted model providers as well as locally running models. It also includes Streamlit interfaces for interactive chatbot experiences and utilities.

## Projects and Experiments

### 1. Chatbots and AI-powered applications

Located in [`Chatbots/`](https://github.com/shubhamthakur9771/GenAi-Projects/tree/main/Chatbots).

| File | What it demonstrates |
|---|---|
| [`AssistantBot.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/Chatbots/AssistantBot.py) | Streamlit assistant combining text chat, speech input, text-to-speech responses, conversation history, feedback actions, and PDF summarization. |
| [`voiceAssistant.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/Chatbots/voiceAssistant.py) | Voice-enabled assistant with speech recognition, spoken responses, a stop-speaking control, and Groq-powered chat. |
| [`pdf_app.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/Chatbots/pdf_app.py) | Upload a PDF, extract its text, summarize it with a Groq chat model, and download the generated summary as a PDF. |
| [`groqChatbot.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/Chatbots/groqChatbot.py) | Terminal chatbot using the Groq API with a message history that retains the conversation context. |
| [`geminiChatbot.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/Chatbots/geminiChatbot.py) | Streamlit image-generation interface that sends a text prompt to the Stability AI image-generation API and provides a generated-image download. |
| [`image_gen.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/Chatbots/image_gen.py) | Local Stable Diffusion pipeline experiment using Hugging Face Diffusers and PyTorch. |

### 2. Chat models and LLM integrations

Located in [`chatmodels/`](https://github.com/shubhamthakur9771/GenAi-Projects/tree/main/chatmodels).

| File | What it demonstrates |
|---|---|
| [`openAi_ChatOpenAi.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/chatmodels/openAi_ChatOpenAi.py) | Calling an OpenAI chat model through LangChain's `ChatOpenAI` integration. |
| [`openAi_Chat_Model.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/chatmodels/openAi_Chat_Model.py) | Initializing a chat model through LangChain's model initialization interface. |
| [`geminiChat_Model.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/chatmodels/geminiChat_Model.py) | Connecting to a Gemini model through LangChain. |
| [`chat.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/chatmodels/chat.py) | Mistral chat-model experiment with configurable generation parameters. |
| [`chatbot.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/chatmodels/chatbot.py) | Simple terminal-based conversational loop using Mistral. |
| [`ollama_local_model.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/chatmodels/ollama_local_model.py) | Running a local Qwen model through Ollama and LangChain. |
| [`ollama_chatbot.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/chatmodels/ollama_chatbot.py) | Terminal chatbot using Ollama chat models and message objects for conversational context. |
| [`localmodel.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/chatmodels/localmodel.py) | Local Hugging Face text-generation pipeline experiment using TinyLlama. |
| [`huggingface.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/chatmodels/huggingface.py) | Hugging Face hosted inference experiment through LangChain. |
| [`UIChatbot.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/chatmodels/UIChatbot.py) | Streamlit chatbot with selectable response moods and conversation state. |
| [`core.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/chatmodels/core.py) | Prompt-template experiment for extracting structured, useful information from a paragraph. |
| [`Structured_Output.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/chatmodels/Structured_Output.py) | Extracting movie details into a Pydantic schema using an Ollama model and LangChain output parser. |

### 3. Embedding models

Located in [`embeddingmodels/`](https://github.com/shubhamthakur9771/GenAi-Projects/tree/main/embeddingmodels).

- [`embeddings.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/embeddingmodels/embeddings.py) demonstrates generating document embeddings with the `nomic-embed-text` model through Ollama's LangChain integration.
- The example embeds a small collection of text strings and prints a portion of the resulting vector.

### 4. RAG and document-processing experiments

Located in [`RAG%20Project/`](https://github.com/shubhamthakur9771/GenAi-Projects/tree/main/RAG%20Project).

- [`main.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/RAG%20Project/main.py) loads a PDF with LangChain's `PyPDFLoader`, formats its extracted text into a prompt, and requests a concise summary from a Mistral chat model.
- [`document loaders/`](https://github.com/shubhamthakur9771/GenAi-Projects/tree/main/RAG%20Project/document%20loaders) contains focused examples of text splitting:
  - [`text_split.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/RAG%20Project/document%20loaders/text_split.py)
  - [`Recursive_character_text_splitter.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/RAG%20Project/document%20loaders/Recursive_character_text_splitter.py)
  - [`token_based_splitting.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/RAG%20Project/document%20loaders/token_based_splitting.py)
  - [`test.py`](https://github.com/shubhamthakur9771/GenAi-Projects/blob/main/RAG%20Project/document%20loaders/test.py)

These examples cover loading document content and preparing text chunks for downstream language-model workflows. The repository currently contains document-loading and splitting experiments; it should not be interpreted as a complete production RAG pipeline.

## Technology Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square" alt="LangChain">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Ollama-black?style=flat-square" alt="Ollama">
  <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="Hugging Face">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI">
  <img src="https://img.shields.io/badge/Google_Gemini-8E75B2?style=flat-square" alt="Google Gemini">
  <img src="https://img.shields.io/badge/Groq-F55036?style=flat-square" alt="Groq">
  <img src="https://img.shields.io/badge/Mistral-000000?style=flat-square" alt="Mistral">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch">
</p>

- **Language:** Python
- **LLM orchestration:** LangChain
- **Model providers and runtimes:** OpenAI, Google Gemini, Groq, Mistral, Ollama, Hugging Face
- **Local model experiments:** Qwen 2.5, TinyLlama, Stable Diffusion
- **User interfaces:** Streamlit and command-line applications
- **Embeddings:** Ollama embeddings with `nomic-embed-text`
- **Document processing:** LangChain document loaders, PDF extraction, and text splitters
- **Validation and output parsing:** Pydantic and LangChain output parsers
- **Other libraries:** PyPDF2, ReportLab, SpeechRecognition, pyttsx3, Diffusers, and PyTorch

## Repository Structure

```text
GenAi-Projects/
├── Chatbots/
│   ├── AssistantBot.py
│   ├── geminiChatbot.py
│   ├── groqChatbot.py
│   ├── image_gen.py
│   ├── pdf_app.py
│   └── voiceAssistant.py
│
├── RAG Project/
│   ├── document loaders/
│   │   ├── Recursive_character_text_splitter.py
│   │   ├── test.py
│   │   ├── text_split.py
│   │   └── token_based_splitting.py
│   ├── main.py
│   └── requirements.txt
│
├── chatmodels/
│   ├── Structured_Output.py
│   ├── UIChatbot.py
│   ├── core.py
│   ├── chatbot.py
│   ├── chat.py
│   ├── geminiChat_Model.py
│   ├── huggingface.py
│   ├── localmodel.py
│   ├── ollama_chatbot.py
│   ├── ollama_local_model.py
│   ├── openAi_Chat_Model.py
│   └── openAi_ChatOpenAi.py
│
├── embeddingmodels/
│   └── embeddings.py
│
└── .gitignore
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/shubhamthakur9771/GenAi-Projects.git
cd GenAi-Projects
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

The repository's dependency file is inside `RAG Project/`.

```bash
python -m pip install --upgrade pip
pip install -r "RAG Project/requirements.txt"
```

The requirements file is a broad dependency list, but it does not currently declare every package imported by every script (for example, some chatbot, Ollama, speech, and image-generation integrations). Install the relevant provider and application packages in the active virtual environment when running those examples.

### 4. Run an application

Examples:

```bash
# Streamlit mood-based chatbot
streamlit run chatmodels/UIChatbot.py

# Streamlit structured-output example
streamlit run chatmodels/Structured_Output.py

# Streamlit voice assistant
streamlit run Chatbots/voiceAssistant.py

# Terminal-based Ollama chatbot
python chatmodels/ollama_chatbot.py

# PDF summarization experiment
cd "RAG Project" && python main.py
```

Run the examples from the repository root, except for the RAG summary script: it uses a path relative to the `RAG Project/` directory, so the command above changes into that folder first.

## Configuration

### API-based model providers

Create a `.env` file in the repository root and add only the credentials for the provider-backed examples you intend to run:

```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
MISTRAL_API_KEY=your_mistral_api_key
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token
STABILITY_API_KEY=your_stability_api_key
```

The variable names above are configuration examples; use the exact variable expected by the relevant provider integration or script. In particular, the Stability AI image-generation script reads `STABILITY_API_KEY`, while the Groq chatbot examples read `GROQ_API_KEY`.

Keep `.env` out of version control. The repository's `.gitignore` already ignores `.env` and `*.env`.

### Local models with Ollama

Install and run [Ollama](https://ollama.com/), then pull the model used by the examples:

```bash
ollama pull qwen2.5:3b
ollama pull nomic-embed-text
```

For the TinyLlama example, the Hugging Face model is loaded by the Transformers integration.

## Notes

- This repository is a learning and experimentation collection. Individual scripts may have different dependency requirements and may need provider credentials or local model runtimes.
- The examples use different model providers and model names; availability and API pricing are controlled by those providers.
- The `RAG Project/main.py` example currently summarizes the first loaded PDF page's extracted content (`docs[0].page_content`), rather than implementing retrieval over a vector database.
- Some scripts expect files or services to be available locally. Review the paths and runtime requirements before executing them.

## Useful Links

- **Repository:** [GenAi-Projects on GitHub](https://github.com/shubhamthakur9771/GenAi-Projects)
- **Python:** [python.org](https://www.python.org/)
- **LangChain:** [Documentation](https://python.langchain.com/docs/introduction/)
- **Ollama:** [ollama.com](https://ollama.com/)
- **Streamlit:** [Documentation](https://docs.streamlit.io/)
- **Hugging Face:** [huggingface.co](https://huggingface.co/)
- **OpenAI API:** [Platform documentation](https://platform.openai.com/docs/)
- **Google Gemini:** [Gemini API documentation](https://ai.google.dev/gemini-api/docs)
- **Groq:** [Documentation](https://console.groq.com/docs)
- **Mistral AI:** [Documentation](https://docs.mistral.ai/)
- **Stability AI:** [API documentation](https://platform.stability.ai/docs)

---

<div align="center">

**Built with Python while exploring Generative AI and LLM application development.**

[Back to top](#generative-ai-projects)

</div>
