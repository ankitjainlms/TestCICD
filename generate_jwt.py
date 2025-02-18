import jwt
import time
import os

# Load secrets from GitHub environment variables
private_key = os.getenv("PRIVATE_KEY").replace("\\n", "\n")
key_id = os.getenv("APPLE_KEY_ID")
issuer_id = os.getenv("APPLE_ISSUER_ID")

# JWT Payload
payload = {
    "iss": issuer_id,
    "iat": int(time.time()),
    "exp": int(time.time()) + 600,
    "aud": "appstoreconnect-v1"
}

# Generate JWT Token
token = jwt.encode(payload, private_key, algorithm="ES256", headers={"kid": key_id})

# Print token for GitHub Actions
print(f"::set-output name=JWT_TOKEN::{token}")
