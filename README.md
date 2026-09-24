# 🔬 ResearchFlow AI — Multi-Agent Deep Research System

> **Turn a research question into a structured, source-backed report using a team of specialized AI agents.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Agentic%20AI-green.svg)](https://www.langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/LLM-Groq-orange.svg)](https://groq.com/)
[![Tavily](https://img.shields.io/badge/Search-Tavily-purple.svg)](https://tavily.com/)

**ResearchFlow AI** is a multi-agent AI research application that autonomously researches a user-provided topic and generates a structured research report.

Instead of relying on a single LLM call, the system divides the research workflow across specialized agents responsible for **searching, reading, writing, and critically reviewing** the final report.

🌐 **Live Demo:**
https://deep-research-multi-agent-tool.streamlit.app/

💻 **GitHub:**
https://github.com/Manya-Rajput-2007/deep-research-multi-agent-tool

---

## ✨ Features

* 🤖 **Multi-Agent Architecture**

  * Search Agent
  * Reader Agent
  * Writer Agent
  * Critic Agent

* 🌐 **Real-Time Web Research**

  * Searches the web for recent information using Tavily.
  * Retrieves relevant URLs and search snippets.

* 📖 **Deep Web Reading**

  * Selects relevant sources from search results.
  * Scrapes webpage content for deeper context.

* 📝 **Automated Report Generation**

  * Generates a structured research report containing:

    * Introduction
    * Key Findings
    * Conclusion
    * Sources

* 🔍 **AI-Powered Critique**

  * Reviews the generated report.
  * Provides a score, strengths, areas for improvement, and a verdict.

* 🎨 **Streamlit Interface**

  * Clean research dashboard.
  * Pipeline status visualization.
  * Research topic input.
  * Generated report and critic feedback.

The application's UI presents the workflow as four specialized agents collaborating to search, read, write, and critique research.

---

# 🧠 How It Works

The system follows a sequential multi-agent research pipeline:

```text
                    ┌─────────────────────┐
                    │    Research Topic   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    🔎 Search Agent  │
                    │                     │
                    │ Tavily Web Search   │
                    └──────────┬──────────┘
                               │
                         Search Results
                               │
                               ▼
                    ┌─────────────────────┐
                    │    📖 Reader Agent  │
                    │                     │
                    │ URL Scraping +      │
                    │ Content Extraction  │
                    └──────────┬──────────┘
                               │
                         Research Content
                               │
                               ▼
                    ┌─────────────────────┐
                    │     ✍️ Writer       │
                    │                     │
                    │ Report Generation   │
                    └──────────┬──────────┘
                               │
                         Drafted Report
                               │
                               ▼
                    ┌─────────────────────┐
                    │    🧐 Critic Agent  │
                    │                     │
                    │ Quality Review      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Final Research   │
                    │       Report       │
                    └─────────────────────┘
```

---

# 🤖 Multi-Agent Workflow

### 1. 🔎 Search Agent

The Search Agent receives the research topic and searches the web for recent and relevant information.

It uses the **Tavily Search API** and returns:

* Source titles
* URLs
* Search snippets
* Relevant web information

The implementation limits the search to five results per query.

---

### 2. 📖 Reader Agent

The Reader Agent receives the search results and identifies a relevant URL for deeper research.

It then uses the `scrape_url` tool to:

* Request the webpage
* Parse HTML using BeautifulSoup
* Remove unnecessary elements such as scripts, navigation, and footers
* Extract readable text
* Return the relevant page content

The extracted content is capped before being passed further into the pipeline.

---

### 3. ✍️ Writer

The Writer combines:

```text
Search Results
      +
Scraped Web Content
      ↓
LLM Research Writer
      ↓
Structured Research Report
```

The generated report follows this structure:

```text
Introduction

Key Findings
- Finding 1
- Finding 2
- Finding 3

Conclusion

Sources
- URL 1
- URL 2
- ...
```

The writer is instructed to produce detailed, factual, and professional research reports.

---

### 4. 🧐 Critic Agent

The Critic reviews the generated report independently.

It evaluates:

* Overall quality
* Strengths
* Areas for improvement
* Final verdict

The current critic format produces a score out of 10 along with qualitative feedback.

---

# 🏗️ Architecture

```text
                    User
                     │
                     ▼
              Streamlit Interface
                     │
                     ▼
              Research Pipeline
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
     Search Agent          Reader Agent
          │                     │
          │ Tavily              │
          │ Search              │
          │                     │
          └──────────┬──────────┘
                     │
                     ▼
                 Research
                     │
                     ▼
                   Writer
                     │
                     ▼
                  Report
                     │
                     ▼
                  Critic
                     │
                     ▼
             Final Output + Feedback
```

The orchestration is implemented in `pipeline.py`, where the search, reader, writer, and critic stages are executed sequentially and their outputs are passed through a shared state dictionary.

---

# 🛠️ Tech Stack

| Technology        | Purpose                           |
| ----------------- | --------------------------------- |
| **Python**        | Core programming language         |
| **LangChain**     | Agent and LLM orchestration       |
| **Groq**          | LLM inference                     |
| **GPT-OSS-120B**  | Language model used by the agents |
| **Tavily**        | Web search                        |
| **BeautifulSoup** | Web content extraction            |
| **Requests**      | HTTP requests                     |
| **Streamlit**     | Interactive web application       |
| **python-dotenv** | Environment variable management   |
| **Rich**          | Terminal output formatting        |

The repository's dependency file includes LangChain, LangChain-Groq, Streamlit, Tavily, BeautifulSoup, Requests, dotenv, and related packages.

---

# 📂 Project Structure

```text
deep-research-multi-agent-tool/
│
├── agents.py
│   ├── Search Agent
│   ├── Reader Agent
│   ├── Writer Chain
│   └── Critic Chain
│
├── pipeline.py
│   └── Research workflow orchestration
│
├── tools.py
│   ├── web_search()
│   └── scrape_url()
│
├── app.py
│   └── Streamlit user interface
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Manya-Rajput-2007/deep-research-multi-agent-tool.git
```

```bash
cd deep-research-multi-agent-tool
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

> Never commit your `.env` file or API keys to GitHub.

---

# ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in your terminal.

---

# 🖥️ Using ResearchFlow AI

### Step 1 — Enter a topic

Example:

```text
Recent advancements in Generative AI
```

### Step 2 — Run the pipeline

Click:

```text
⚡ Run Research Pipeline
```

### Step 3 — Let the agents work

The system performs:

```text
Search
  ↓
Read
  ↓
Write
  ↓
Critique
```

### Step 4 — Review the result

The application provides:

* Research report
* Key findings
* Sources
* Critic feedback

---

# 💡 Example Research Topics

You can research topics such as:

```text
Recent advancements in Large Language Models

The future of autonomous AI agents

Quantum computing breakthroughs

CRISPR gene editing

Fusion energy progress

AI applications in healthcare

The impact of Generative AI on software development
```

---

# 🧩 Core Components

## `agents.py`

Contains the AI agent definitions and LLM chains.

```python
build_search_agent()
build_reader_agent()
writer_chain
critic_chain
```

The project currently initializes the LLM through LangChain using Groq and the `openai/gpt-oss-120b` model.

---

## `tools.py`

Contains the external research tools:

```python
web_search()
scrape_url()
```

`web_search()` uses Tavily, while `scrape_url()` uses Requests and BeautifulSoup for webpage extraction.

---

## `pipeline.py`

Responsible for orchestrating the complete research process:

```python
run_research_pipeline(topic)
```

The pipeline stores intermediate outputs such as:

```python
state["search_results"]
state["scraped_content"]
state["report"]
state["feedback"]
```

before returning the complete research state.

---

## `app.py`

Provides the Streamlit frontend and visualizes the research pipeline.

The interface includes:

* Research topic input
* Pipeline visualization
* Run Research Pipeline button
* Research results
* Critic feedback
* Downloadable output

---

# 🔄 Research Pipeline

```text
User Query
    │
    ▼
Search Agent
    │
    ├── Tavily Search
    │
    ▼
Relevant Sources
    │
    ▼
Reader Agent
    │
    ├── URL Selection
    ├── HTTP Request
    └── HTML Extraction
    │
    ▼
Research Context
    │
    ▼
Writer
    │
    ├── Introduction
    ├── Key Findings
    ├── Conclusion
    └── Sources
    │
    ▼
Generated Report
    │
    ▼
Critic
    │
    ├── Score
    ├── Strengths
    ├── Improvements
    └── Verdict
    │
    ▼
Final Research Output
```

---

# 🎯 Why This Project?

Traditional LLM applications often follow:

```text
User → LLM → Answer
```

ResearchFlow AI explores a more agentic architecture:

```text
User
 ↓
Search Agent
 ↓
Reader Agent
 ↓
Writer
 ↓
Critic
 ↓
Research Report
```

Each component has a specific responsibility, making the workflow easier to extend with additional agents, tools, verification steps, or research strategies.

---

# 🚀 Future Improvements

Potential improvements include:

* [ ] Multi-source webpage extraction instead of a single selected URL
* [ ] Citation verification
* [ ] Fact-checking agent
* [ ] Research planner agent
* [ ] Parallel research agents
* [ ] Report revision after critic feedback
* [ ] Source credibility scoring
* [ ] PDF report generation
* [ ] Persistent research history
* [ ] RAG-based research memory
* [ ] Research export to Markdown/PDF
* [ ] Better handling of inaccessible webpages
* [ ] Automated evaluation metrics
* [ ] Agent tracing and observability

---

# ⚠️ Limitations

ResearchFlow AI is an experimental research assistant.

Generated reports may contain:

* Incorrect information
* Incomplete source coverage
* Outdated information
* Errors caused by inaccessible or poorly structured webpages
* LLM-generated interpretations that require verification

Always verify important information against the original sources before relying on it.

---

# 🌐 Live Demo

Try ResearchFlow AI:

**https://deep-research-multi-agent-tool.streamlit.app/**

---

# 👩‍💻 Author

**Manya Rajput**

B.Tech — Computer Science & Engineering

GitHub:
https://github.com/Manya-Rajput-2007

LinkedIn:
https://linkedin.com/in/manya-rajput-2a281b33b

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is intended for educational and portfolio purposes.
