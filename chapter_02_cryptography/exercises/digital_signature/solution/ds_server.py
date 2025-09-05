from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
import base64

app = FastAPI()

class MessageRequestBody(BaseModel):
    message: str
    signature: str

@app.post("/message")
def message(request: MessageRequestBody):
    try:
        message = request.message
        signature = base64.b64decode(request.signature)

        public_key = ECC.import_key(open('public_key.pem', "rb").read())
        message_hash = SHA256.new(message.encode())
        verifier = DSS.new(public_key, 'fips-186-3')
        
        try:
            verifier.verify(message_hash, signature)
        except ValueError:
            return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"success": False, "message": "The message is not authentic!"}
            )
        
        return JSONResponse(
            status_code=status.HTTP_200_OK, 
            content={"success": True, "message": "The message is authentic!"}
        )
    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            content={"success": False, "message": "Internal Server Error."}
        )
