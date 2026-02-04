from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI()

DATA_FILE = Path("data/progress.json")

class ProgressEntry(BaseModel):
    date: str
    activity: str
    learning: str
    struggle: str
    pride: str
    improvement: str


def load_data():
    if not DATA_FILE.exists():
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


@app.post("/create", status_code=201)
async def create_progress(entry: ProgressEntry):
    data = load_data()

    data[entry.date] = {
        "activity": entry.activity,
        "learning": entry.learning,
        "struggle": entry.struggle,
        "pride": entry.pride,
        "improvement": entry.improvement,
    }

    save_data(data)

    return {"message": f"Progress for {entry.date} created successfully"}


# @app.delete('/delete/{date}')
# async def delete_progress(date: str = Path(..., description="The date of the progress entry to delete")):
#     data = load_data()
#     if date in data:
#         del data[date]
#         save_data(data)
#         return JSONResponse(content={"message": f"Progress for {date} deleted successfully"}, status_code=200)
#     else:
#         return JSONResponse(content={"error": "Date not found"}, status_code=404)