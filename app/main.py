from fastapi import FastAPI
from app.api.routes import user

app = FastAPI()

# Include route modules
app.include_router(user.router, prefix="/users", tags=["Users"])
# Health Check
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "OK"}
