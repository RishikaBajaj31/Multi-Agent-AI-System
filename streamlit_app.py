# streamlit_app.py
import sys, os
import streamlit as st
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------
# Import Agents & Orchestrator
# ---------------------------
from backend.agents.data_agent import DataAgent
from backend.agents.research_agent import ResearchAgent
from backend.agents.orchestrator import Orchestrator

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("🤖 Multi-Agent AI System")

# File uploaders
data_file = st.file_uploader("Upload Data File (CSV/Excel)", type=["csv", "xlsx"], key="data")
research_file = st.file_uploader("Upload Research File (PDF)", type=["pdf"], key="research")

# Save uploaded files and persist in session state
if data_file:
    data_path = os.path.join(os.getcwd(), data_file.name)
    with open(data_path, "wb") as f:
        f.write(data_file.getbuffer())
    st.session_state["data_path"] = data_path

if research_file:
    research_path = os.path.join(os.getcwd(), research_file.name)
    with open(research_path, "wb") as f:
        f.write(research_file.getbuffer())
    st.session_state["research_path"] = research_path

# Get persisted paths
data_path = st.session_state.get("data_path", None)
research_path = st.session_state.get("research_path", None)

# Initialize or update orchestrator
st.session_state["orchestrator"] = Orchestrator(
    DataAgent(data_path) if data_path else None,
    ResearchAgent(research_path) if research_path else None
)
orchestrator = st.session_state["orchestrator"]

# Query input
if "query" not in st.session_state:
    st.session_state["query"] = ""

st.text_input("Enter your query:", key="query")
query = st.session_state["query"]

# Run Agents button
if st.button("Run Agents"):
    if query:
        with st.spinner("Running agents..."):
            response = orchestrator.route(query)
        st.success("Response:")
        st.write(response)
    else:
        st.warning("Please enter a query first!")

# Test with sample files button
if st.button("Test with Sample Files"):
    sample_query = "Summarize the dataset and research"
    response = orchestrator.route(sample_query)
    st.success("Response (sample files):")
    st.write(response)

