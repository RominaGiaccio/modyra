from fastapi import FastAPI

app = FastAPI(
    title="Modyra API",
    description="API for Modyra, an AI-powered personal check-in app.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"message": "Welcome to Modyra API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}