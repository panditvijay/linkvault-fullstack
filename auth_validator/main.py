import jwt
import os
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

app = FastAPI()

# THIS MUST BE THE SAME SECRET KEY AS IN YOUR DJANGO USER_SERVICE!
# We'll load it from an environment variable.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

@app.get("/validate")
async def validate_token(request: Request):
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        return Response(status_code=401) # Unauthorized

    token = auth_header.split(' ')[1]

    try:
        # Decode the token. This will raise an exception if it's invalid.
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_token.get('user_id')

        if user_id is None:
            return Response(status_code=401)

        # If valid, return 200 OK and set the user ID in a response header
        headers = {'X-User-Id': str(user_id)}
        return Response(status_code=200, headers=headers)

    except jwt.ExpiredSignatureError:
        return JSONResponse(status_code=401, content={"detail": "Token has expired"})
    except jwt.InvalidTokenError:
        return JSONResponse(status_code=401, content={"detail": "Invalid token"})