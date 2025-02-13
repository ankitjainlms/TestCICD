import jwt
import time
import os

# Read secrets from environment variables
key_path = "AuthKey.p8"
key_id = os.getenv("APPSTORE_KEY_ID", "").strip()
issuer_id = os.getenv("APPSTORE_ISSUER_ID", "").strip()

if not key_id:
    raise ValueError("❌ ERROR: APPSTORE_KEY_ID is missing or empty!")
if not issuer_id:
    raise ValueError("❌ ERROR: APPSTORE_ISSUER_ID is missing or empty!")

print("✅ Reading private key in binary mode to prevent UnicodeDecodeError")
with open(key_path, "rb") as key_file:  # Read in binary mode
    private_key = key_file.read()

# Generate JWT token
current_time = int(time.time())
payload = {
    "iss": issuer_id,
    "iat": current_time,
    "exp": current_time + 1200,  # Token expires in 20 minutes
    "aud": "appstoreconnect-v1"
}

headers = {"alg": "ES256", "kid": key_id}
token = jwt.encode(payload, private_key, algorithm="ES256", headers=headers)

print(f"✅ JWT Token Generated: {token[:20]}... (truncated)")

# Save JWT Token to GitHub Environment
with open(os.getenv("GITHUB_ENV"), "a") as env_file:
    env_file.write(f"JWT_TOKEN={token}\n")
