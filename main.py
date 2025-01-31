from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from database.database import create_db_and_tables
from typing import Annotated
from routes.shell_routes import shell_router

app = FastAPI(
    title="Shell API",
    description="This API manages a collection of shells.",
    version="1.0.0",)
app.include_router(shell_router, prefix="/api/v1")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": "Check that all fields are correct"},
    )

