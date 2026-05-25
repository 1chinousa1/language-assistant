# Local LLM Language Study Assistant 🤖🇯🇵

A privacy-focused, zero-cost pipeline that leverages a local Large Language Model (LLM) to parse foreign-language strings, automatically extract foundational vocabulary data, and format structured components into production-grade outputs ready for bulk flashcard importation (e.g., Anki).

## 🚀 Architectural Paradigm
Unlike traditional implementations dependent on cloud API frameworks, this system handles token extraction locally by utilizing an onsite inference runtime to optimize data processing pipelines, prevent structural data mutations, and remove reliance on metered commercial APIs.

## 🛠️ Tech Stack & Dependencies
* **Inference Runtime Engine:** Ollama (Local Orchestration)
* **Underlying Model Matrix:** Llama 3.1 (8B Parameter Setup)
* **Application Framework:** Python 3.12+ 
* **Data Integration Pipeline:** LangChain Core & LangChain Ollama Driver

## 📦 Local Installation & Setup

1. **Initialize the Repository & Sandboxed Environment:**
   ```bash
   git clone [https://github.com/j-chan96/language-assistant.git](https://github.com/j-chan96/language-assistant.git)
   cd language-assistant
   python3 -m venv .venv
   source .venv/bin/activate
