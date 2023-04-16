from fastapi import FastAPI
from .main import ui

def mount_frontend(app: FastAPI) -> None:
    ui.run_with(app)
