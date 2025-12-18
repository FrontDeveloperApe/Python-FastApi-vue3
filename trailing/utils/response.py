from datetime import datetime
from typing import Any, Optional, Dict
import uuid
from fastapi import status
from fastapi.responses import JSONResponse

# 基础响应模型
class ResponseModel:
    @staticmethod
    def success(
        data: Any = None,
        message: str = "success",
        code: int = 200
    ) -> JSONResponse:
        """成功响应"""
        response_data = {
            "code": code,
            "message": message,
            "data": data,
            # "requestId": str(uuid.uuid4()),
            # "timestamp": int(datetime.now().timestamp() * 1000)
        }
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=response_data
        )

    @staticmethod
    def fail(
        message: str,
        code: int = 400,
        data: Any = None,
        http_status: int = status.HTTP_200_OK
    ) -> JSONResponse:
        """失败响应（业务错误，HTTP状态码默认200，避免浏览器拦截）"""
        response_data = {
            "code": code,
            "message": message,
            "data": data,
            # "requestId": str(uuid.uuid4()),
            # "timestamp": int(datetime.now().timestamp() * 1000)
        }
        return JSONResponse(
            status_code=http_status,
            content=response_data
        )

# 快捷响应函数（简化调用）
def resp_success(data: Any = None, message: str = "success"):
    return ResponseModel.success(data=data, message=message)

def resp_fail(message: str, code: int = 400, data: Any = None):
    return ResponseModel.fail(message=message, code=code, data=data)

# 分页响应封装（通用分页场景）
def resp_page(data: list, total: int, page: int, size: int, message: str = "success"):
    page_data = {
        "list": data,
        "total": total,
        "page": page,
        "size": size,
        "pages": (total + size - 1) // size  # 总页数
    }
    return ResponseModel.success(data=page_data, message=message)