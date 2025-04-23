from fastapi import FastAPI

    app = FastAPI()

    @app.get("/test_import")
    async def test_import():
        try:
            import wntr
            return {"message": "WNTR imported successfully"}
        except ImportError as e:
            return {"error": str(e)}, 500
   

   
