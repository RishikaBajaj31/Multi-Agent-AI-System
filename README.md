**Multi-Agent AI System**

A Streamlit-based multi-agent AI system capable of handling data queries from CSV/Excel files and research queries from PDFs. This project demonstrates an orchestrated AI agent setup where different agents specialize in different tasks, integrated via a central orchestrator.

**Features**

**Data Agent**: Processes uploaded CSV/Excel files and answers queries like:

Analyses and shows summary of columns in the dataset.
Query = Analyze

**Research Agent**: Processes uploaded PDFs and extracts meaningful information:

Summarize research papers

Extract keywords or topics

Answer PDF-related queries

**Orchestrator**: Routes user queries to the appropriate agent (Data Agent or Research Agent).

Streamlit Interface: Simple web interface to upload files, type queries, and get responses in real-time.

**Installation**

Clone the repository:

git clone https://github.com/yourusername/multi-agent-ai.git
cd multi-agent-ai

Install dependencies:

pip install -r requirements.txt


Dependencies include:

pandas

matplotlib

streamlit

PyMuPDF (fitz)

**Usage**

Run the Streamlit app:

streamlit run app.py


Upload your CSV/Excel file and/or PDF file using the interface.

Type your query in the text box and press Run Agents.

Example queries for CSV: "Analyze"

Example queries for PDF: "Summarize research", "Extract keywords"


Project Structure
ai-agent-system/
├── backend/
│   ├── agents/
│   │   ├── data_agent.py
│   │   ├── research_agent.py
│   │   └── orchestrator.py
│   └── main.py
├── app.py
├── sample_data.csv
├── sample_research.pdf
└── README.md


data_agent.py: Handles CSV/Excel file processing.

research_agent.py: Handles PDF research file processing.

orchestrator.py: Routes queries to the correct agent.

main.py: Contains FastAPI endpoints and helper functions for agents.

streamlit_app.py: Streamlit front-end for interacting with the agents.

Notes

Uploaded files are stored temporarily in /content (for Colab) or local working directory (for local runs).

Queries that do not match any specific agent keyword are routed to all available agents by default.

Make sure your CSV has numeric columns if you want visualizations like bar charts.

Screenshots
<img width="1236" height="690" alt="image" src="https://github.com/user-attachments/assets/4e31cc08-55a4-40dd-918a-42839e5eeff1" />
