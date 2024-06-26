from fastapi import FastAPI, Request
import uvicorn
import places_api
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://192.168.1.62:3000",
    "http://localhost:3000"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/places")
def tokenize(lon: float, lat: float, user_description: str):
    return places_api.get_places(lon, lat, user_description)


if __name__ == '__main__':
    uvicorn.run(app, port=3001, host='0.0.0.0')
