import logging

from fastapi import FastAPI

from api.routers.journal_router import router as journal_router

app = FastAPI(
    title="Journal API",
    description="A simple journal API for tracking daily work, struggles, and intentions",
)
app.include_router(journal_router)

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
logging.getLogger(__name__).info("Journal API starting up")
