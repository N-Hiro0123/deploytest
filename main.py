from fastapi import FastAPI

import os
from dotenv import load_dotenv

# 環境変数のロード
# load_dotenv()  # デプロイ時に残しておいても問題ないらしい（あやしければ無効にする）
TEST_SECRET = os.getenv("TEST_SECRET")

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": TEST_SECRET}
