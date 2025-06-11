from fastapi import APIRouter, UploadFile, File, Form
import pandas as pd

router = APIRouter()

@router.post("/upload")
def upload(user_id: str = Form(...), budget: float = Form(...), bank_statement: UploadFile = File(...)):
    df = pd.read_csv(bank_statement.file)
    total_spent = df["Amount"].sum()
    most_spent = df.sort_values(by="Amount", ascending=False).iloc[0]
    recurring = df["Description"].value_counts().idxmax()
    savings = budget - total_spent
    return {
        "total_spent": total_spent,
        "most_spent": most_spent.to_dict(),
        "most_recurring": recurring,
        "estimated_savings": savings
    }
