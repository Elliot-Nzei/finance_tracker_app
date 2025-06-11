from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse

from app.services.finance_service import analyze_statement, save_budget, load_budget

router = APIRouter()


@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        return JSONResponse(status_code=400, content={"error": "Only CSV files are supported."})
    
    content = await file.read()
    analysis = analyze_statement(content.decode("utf-8"))
    return JSONResponse(content={"summary": analysis})


@router.post("/budget")
async def set_budget(amount: float = Form(...)):
    save_budget(amount)
    return JSONResponse(content={"message": "Budget saved."})


@router.get("/budget")
async def get_budget():
    budget = load_budget()
    return JSONResponse(content={"budget": budget})
