from fastapi import FastAPI, Depends, Request, Response
from fastapi.responses import RedirectResponse, JSONResponse
from gateway.api_router import call_api_gateway, RedirectStudentPortalException, RedirectFacultyPortalException, \
    RedirectLibraryPortalException
from controller import university

from loguru import logger
from uuid import uuid4

app = FastAPI()
app.include_router(university.router,
                   dependencies=[Depends(call_api_gateway)])
logger.add("info.log", format="Log: [{extra[log_id]}: {time} - {level} - {message} ", level="INFO", enqueue=True)


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    log_id = str(uuid4())
    with logger.contextualize(log_id=log_id):
        logger.info('Request to access ' + request.url.path)
        try:
            response = await call_next(request)
        except Exception as ex:
            logger.error(f"Request to " + request.url.path + " failed: {ex}")
            response = JSONResponse(content={"success": False}, status_code=500)
        finally:
            logger.info('Successfully accessed ' + request.url.path)
            return response


@app.exception_handler(RedirectStudentPortalException)
def exception_handler_student(request: Request, exc: RedirectStudentPortalException) -> Response:
    return RedirectResponse(url='http://localhost:8003/docs')


@app.exception_handler(RedirectFacultyPortalException)
def exception_handler_faculty(request: Request, exc: RedirectFacultyPortalException) -> Response:
    return RedirectResponse(url='http://localhost:8002/docs')


@app.exception_handler(RedirectLibraryPortalException)
def exception_handler_library(request: Request, exc: RedirectLibraryPortalException) -> Response:
    return RedirectResponse(url='http://localhost:8001/docs')
