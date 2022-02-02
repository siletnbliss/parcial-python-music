from sys import prefix
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router as music_store_router

def get_application():
    # set title to display on swagger documentation
    app= FastAPI(title="Music Store API", version="1.0.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    #  include router with all defined routes defined in /routes folder
    app.include_router(music_store_router, prefix="/music-store/api/v1")

    return app

app = get_application()
