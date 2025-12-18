from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request

from utils.response import resp_success,resp_fail,resp_page
from utils.exceptions import BusinessException, custom_exception_handler
from starlette.exceptions import HTTPException as StarletteHTTPException
import random

# 创建 FastAPI 实例
app = FastAPI(title="FastAPI 接口规范示例", version="1.0")

# 跨域配置
origins = [
    "http://localhost:5173",  # Vite 开发服务器默认端口
    "http://127.0.0.1:5173",
    # 生产环境添加实际前端域名，如 "https://your-frontend-domain.com"
    "*",  # 开发环境临时允许所有域名（生产环境务必删除！）
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许的源（前端域名）
    allow_credentials=True,  # 允许携带 Cookie/Token（关键！前端请求带认证信息时必须开启）
    allow_methods=["*"],  # 允许所有 HTTP 方法（GET/POST/PUT/DELETE 等）
    allow_headers=["*"],  # 允许所有请求头（如 Authorization/Content-Type 等）
)

# 注册全局异常处理器
app.add_exception_handler(StarletteHTTPException, custom_exception_handler)
app.add_exception_handler(Exception, custom_exception_handler)













