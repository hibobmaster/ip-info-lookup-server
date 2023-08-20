from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse
from mmdb_func import ip_validator
from results import struct_ip_info_str, struct_ip_info

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
def rootg(request: Request):
    return (
        struct_ip_info_str(request.client.host)
        + "\n"
        + request.headers.get("User-Agent")
    )


@app.post("/")
def rootp(request: Request):
    return JSONResponse(content=struct_ip_info(request.client.host), status_code=200)


@app.get("/ip/{ip}", response_class=PlainTextResponse)
def ipg(ip: str, request: Request):
    if ip_validator(ip):
        return struct_ip_info_str(ip) + "\n" + request.headers.get("User-Agent")
    else:
        return {"error": "invalid ip address"}


@app.post("/ip/{ip}")
def ipp(ip: str):
    if ip_validator(ip):
        return JSONResponse(content=struct_ip_info(ip), status_code=200)
    else:
        return JSONResponse(content={"error": "invalid ip address"}, status_code=400)
