from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.controllers.upload_controller import router as upload_router

app = FastAPI(
    title="CortexSearch API",
    description="Enterprise RAG System API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)

@app.get("/", tags=["Health Check"])
def health_status():
    return {"message": "CortexSearch Backend is running...."}