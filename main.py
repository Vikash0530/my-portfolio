from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.contact import router as contact_router
from routers.projects import router as projects_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contact_router, prefix="/api")
app.include_router(projects_router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "API Running"}