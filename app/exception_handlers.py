from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from app.exceptions import PartNotFoundError


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(PartNotFoundError)
    async def handle_part_not_found(request: Request, exc: PartNotFoundError):
        return JSONResponse(
            status_code=404,
            content={"detail": str(exc)},
        )
