# Your Honor, I Object (to Jury Duty)

## 🧩 Problem Statement

Jurors often have questions about their eligibility, the excusal process, and legal obligations that are difficult to answer without calling the jury office or reading complex legal code. This creates workload strain on staff, delays for jurors, and inconsistent access to accurate information. The goal of this prototype is to build a low-cost, legally cautious AI chatbot that can provide neutral, citation-backed answers using content from California Code of Civil Procedure §§190–242 and California Rule of Court 2.1008 This tool is designed to support, not replace, staff by answering common questions and guiding users toward the correct next steps.

⚠️ **Demo Only – Not for Public Use**

🔗 Demo (Loom): [Watch the demo](https://www.loom.com/share/189bf95c6e8643da9188f85413daf56f?sid=634f2e81-8ac8-4328-8a54-9524c1a4231a)  

This AI chatbot prototype answers jury-related questions using:
- California Code of Civil Procedure §§190–242
- California Rule of Court 2.1008

It uses Retrieval-Augmented Generation (RAG) with AWS Bedrock (Claude model), FAISS indexing, and Streamlit.

### 🚀 What This Project Demonstrates

This chatbot is a proof-of-concept built to simulate safe, real-world AI use in government. It demonstrates:

- How public legal codes (CCP §§190–242 and CRC Rule 2.1008) can be embedded and queried using vector search.
- How Retrieval-Augmented Generation (RAG) enables accurate, citation-backed answers.
- That AWS Bedrock can be used to safely invoke Claude for legal-adjacent use cases.
- That Streamlit enables low-code prototyping with a clean, usable front-end.
- A workflow that’s replicable, explainable, and appropriate for internal government demos.
- A model for how AI can support jury staff, improve public understanding, and reduce inbound phone calls all without giving legal advice.

### 🧰 Tools Used and Why

- **Claude via AWS Bedrock**  
I used Claude because it’s a powerful language model that’s strong with legal and structured text, and Bedrock gave me secure access without managing my own AI infrastructure.
- **LangChain + langchain_community**  
These libraries helped me connect my legal documents to Claude in a way that lets the model “look up” the right answers instead of making them up.
- **FAISS for vector search**  
FAISS let me turn the legal code into a searchable format so that relevant sections could be quickly matched to juror questions.
- **RAG (Retrieval-Augmented Generation)**  
This technique let the AI find and use real legal content instead of relying on its training data. I retrieved the most relevant section of law and passed it into Claude with the user’s question, making the answers accurate and source-cited.
- **Streamlit**  
I used Streamlit to build a clean, simple web interface for demo purposes without needing to code a full front-end website.
- **Python**  
Python made all of this possible with readable code, great support for AI tools, and compatibility with everything from AWS to Streamlit.

## 🔄 Future Development (v10+)

This chatbot is an iterative public service prototype. While version 9 demonstrates successful legal information retrieval, future versions may include:

- ⚖️ Plain-language summaries for each legal response
- 🧠 Multi-turn memory for natural back-and-forth conversation
- 🔍 Semantic search for better matching across phrasing
- 💥 Exception handling for unclear, incomplete, or vague queries
- 🔗 Live deployment to secure internal or public-facing sites
- 🧾 Integration with court FAQs or local rules
- 📞 Inclusion of Jury Office contact details in fallback messages
- 📣 Automatic prompts for unique cases: “Call the Jury Office”
- ✅ Clear pathways for actionable next steps: deferral, excuse, or disqualification
- 🛡️ Additional safety guardrails, like better refusal responses when content is missing
- ⚙️ Refinement of inference parameters (temperature, top_p, etc.) to ensure neutral, cautious tone in public-facing tools

## 🧠 Vector Index Notes (`kb_index/`)

This folder contains the pre-built vector index of your legal knowledge base, created using FAISS during the `load_documents.py` step. It allows the chatbot to match juror questions with relevant code sections.

## 🧠 Environment Notes (for Developers)

This repo does **not** include the following folders, which are auto-generated when running the chatbot locally:

- `_pycache_/` – stores temporary compiled versions of Python files.
- `.venv/` – your local Python virtual environment.

To recreate your environment:
1. Set up a virtual environment (see `vscode_chatbot_instructions_corrected.txt`)
2. Install dependencies with:  
   ```bash
   pip install -r requirements.txt

## 📘 Legal Disclaimer
This app is **not legal advice**. 

## 🙌 Inspiration
Based on [Ryan Gertz’s Bedrock chatbot repo](https://github.com/RyanGertz/aws-bedrock-streamlit-chat)

Created by **L. Cordero** for **CCC AI Summer Camp 2025**.

---

### 🤖 AI Acknowledgment

This project was heavily assisted by **ChatGPT**, which served as my technical coach, writing editor, and troubleshooting partner throughout the build process.

🧠 Credit: "6th Person Off the Bench" — providing assistive insight, not doing the work.

All development decisions, legal content curation, and prompt testing were guided and implemented by **L Cordero**, with ChatGPT providing structure, feedback, and suggestions during the iterative build.

---

