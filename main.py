from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routes.propsal as propsal
from log import setup_logging
import logging

setup_logging()

app = FastAPI(
    title="Proposal API",
    description="API for managing proposals. Use the /docs endpoint for interactive API documentation.",
    version="1.0.0"
)

# CORS middleware (optional if only using docs)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this if not using JS frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
logging.info("CORS middleware added successfully")

# Optional: Add a root endpoint for quick testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the Proposal API. Visit /docs for the API documentation."}

# Include user routes
app.include_router(propsal.router)

"""This is the main entry point for the FastAPI application.
It initializes the app and includes the proposal routes."""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)