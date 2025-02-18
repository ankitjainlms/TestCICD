import jwt
import time
import os

# Load secrets
private_key = os.getenv("PRIVATE_KEY")
key_id = os.getenv("APPLE_KEY_ID")
issuer_id = os.getenv("APPLE_ISSUER_ID")

# Check if secrets are missing
if not private_key or not key_id or not issuer_id:
    raise ValueError("❌ Missing one or more required secrets!")

# Fix private key format
private_key = private_key.replace("\\n", "\n")

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
