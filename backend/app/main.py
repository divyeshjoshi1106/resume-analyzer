from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    print("health endpoint")
    return {"status": "ok"}
