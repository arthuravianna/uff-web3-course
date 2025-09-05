from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from Crypto.Cipher import Salsa20
import base64

app = FastAPI()
KEY = b'0123456789012345'


class MessageRequestBody(BaseModel):
    message: str
    nonce: str

@app.post("/message")
def message(request: MessageRequestBody):
    try:
        # TODO: decrypt and print data here
        message = base64.b64decode(request.message)
        nonce = base64.b64decode(request.nonce)
        
        cipher = Salsa20.new(KEY, nonce)
        res = cipher.decrypt(message)
        
        print("Encrypted message:", request.message)
        print("Decrypted message:", res.decode())
        return JSONResponse(
            status_code=status.HTTP_200_OK, 
            content={"success": True, "message": "Message decrypted on server!"}
        )
    except:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            content={"success": False, "message": "Internal Server Error."}
        )
