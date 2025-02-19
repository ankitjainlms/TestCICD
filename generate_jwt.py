import jwt
import time
import os

# Load environment variables
APPLE_KEY_ID = os.getenv("APPLE_KEY_ID")
APPLE_ISSUER_ID = os.getenv("APPLE_ISSUER_ID")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

if not APPLE_KEY_ID or not APPLE_ISSUER_ID or not PRIVATE_KEY:
    raise ValueError("❌ Missing one or more required secrets!")

# Format the private key correctly
PRIVATE_KEY = PRIVATE_KEY.replace("\\n", "\n")  

# Generate JWT
now = int(time.time())
payload = {
    "iss": APPLE_ISSUER_ID,
    "iat": now,
    "exp": now + 1200,  # Token valid for 20 minutes
    "aud": "appstoreconnect-v1"
}

headers = {
    "alg": "ES256",
    "kid": APPLE_KEY_ID,
    "typ": "JWT"
}

# Generate the signed token
try:
    jwt_token = jwt.encode(payload, PRIVATE_KEY, algorithm="ES256", headers=headers)
    print("✅ Successfully generated JWT Token:")
    print(jwt_token)
except Exception as e:
    print(f"❌ Error generating JWT Token: {e}")
    exit(1)
