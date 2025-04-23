from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    try:
        import wntr
        return {"message": "WNTR imported successfully"}
    except ImportError as e:
        return {"error": str(e)}, 500 
   

   
