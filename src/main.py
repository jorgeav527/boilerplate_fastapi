from fastapi import FastAPI
from sqlmodel import SQLModel

from api.infrastructure.db.sql.session_sqlite import engine
from api.presentation.api.user_routes import router as user_router

# from api.presentation.api.post_routes import router as post_router


def create_app() -> FastAPI:
    app = FastAPI(title="Clean Architecture FastAPI")

    SQLModel.metadata.create_all(engine)

    app.include_router(user_router)
    #     app.include_router(post_router)

    return app


app = create_app()
