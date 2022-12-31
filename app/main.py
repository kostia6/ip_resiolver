import uvicorn as uvicorn
from fastapi import FastAPI

from MyManager import MyManager

app = FastAPI()
manager = MyManager()


@app.get("/ip-service/{ip_addr}")
async def root(ip_addr):
    res = manager.query_ip(ip_addr)
    return res


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
