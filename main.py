import uvicorn
import requests
from lxml import etree
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/")
def rss(username: str, tag: str):

    url = f"https://medium.com/feed/@{username}"
    tag = tag.lower()

    res = requests.get(url)
    root = etree.XML(res.content, etree.XMLParser(strip_cdata=False))

    for item in root.iter("item"):
        categories = [category.text.lower() for category in item.iter("category")]
        if tag not in categories:
            item.getparent().remove(item)

    return Response(content=etree.tostring(root, encoding="UTF-8"), media_type="text/xml")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8108)
