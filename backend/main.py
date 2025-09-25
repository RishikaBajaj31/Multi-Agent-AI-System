
from fastapi import FastAPI, UploadFile, Form
from backend.agents.data_agent import DataAgent
from backend.agents.research_agent import ResearchAgent
from backend.agents.orchestrator import Orchestrator

app = FastAPI()
orchestrator = None

@app.post("/upload-data/")
async def upload_data(file: UploadFile):
    global orchestrator
    with open(file.filename, "wb") as f:
        f.write(await file.read())
    data_agent = DataAgent(file.filename)
    orchestrator = Orchestrator(data_agent=data_agent)
    return {"message": "Data file uploaded and agent ready"}

@app.post("/upload-research/")
async def upload_research(file: UploadFile):
    global orchestrator
    with open(file.filename, "wb") as f:
        f.write(await file.read())
    research_agent = ResearchAgent(file.filename)
    orchestrator = Orchestrator(research_agent=research_agent)
    return {"message": "Research paper uploaded and agent ready"}

@app.post("/query/")
async def query_agent(query: str = Form(...)):
    global orchestrator
    if not orchestrator:
        return {"error": "No agent initialized yet"}
    return {"response": orchestrator.route(query)}

# ✅ Add this function for Streamlit
def run_agents(query: str, data_file=None, research_file=None):
    data_agent = DataAgent(data_file) if data_file else None
    research_agent = ResearchAgent(research_file) if research_file else None
    orch = Orchestrator(data_agent=data_agent, research_agent=research_agent)
    return orch.route(query)
