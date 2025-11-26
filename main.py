from fastapi import FastAPI,File, UploadFile

import csv
from logic import *
app = FastAPI()
 

@app.post("/assignWithCsv")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        file_r=loadCSV('Hayal_No_Status.csv')
        return {"filename": file_r}
        
        
