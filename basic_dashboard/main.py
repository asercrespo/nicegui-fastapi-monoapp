import uvicorn

from frontend import mount_frontend 
from api.app import app

def create_app():
    mount_frontend(app)
    return app

if __name__ == "__main__":
    uvicorn.run("main:create_app", factory=True,  host="127.0.0.1", port=8000, log_level="debug", reload=True)
