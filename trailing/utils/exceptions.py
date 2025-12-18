from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from .response import ResponseModel


# 自定义业务异常
class BusinessException(Exception):
    def __init__(self, message: str, code: int = 400):
        self.message = message
        self.code = code


# 全局异常处理器
async def custom_exception_handler(request: Request, exc: Exception):
    # 1. 参数校验错误（FastAPI 内置）
    if isinstance(exc, RequestValidationError):
        error_msg = f"参数校验失败：{exc.errors()[0]['msg']}（字段：{exc.errors()[0]['loc'][-1]}）"
        return ResponseModel.fail(message=error_msg, code=400)

    # 2. HTTP 异常（如 404/403）
    elif isinstance(exc, (HTTPException, StarletteHTTPException)):
        return ResponseModel.fail(
            message=exc.detail,
            code=exc.status_code,
            http_status=exc.status_code
        )

    # 3. 自定义业务异常
    elif isinstance(exc, BusinessException):
        return ResponseModel.fail(message=exc.message, code=exc.code)

    # 4. 其他未知异常（服务器内部错误）
    else:
        import traceback
        traceback.print_exc()  # 打印错误栈，方便排查
        return ResponseModel.fail(
            message="服务器内部错误，请稍后重试",
            code=500,
            http_status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )