import requests
import os

# Load secrets from GitHub environment variables
jwt_token = os.getenv("JWT_TOKEN")
workflow_id = os.getenv("XCODE_CLOUD_WORKFLOW_ID")

# Xcode Cloud API URL
api_url = f"https://api.appstoreconnect.apple.com/v1/workflows/{workflow_id}/start"

# Headers
headers = {
    "Authorization": f"Bearer {jwt_token}",
    "Content-Type": "application/json"
}

# Send API Request
response = requests.post(api_url, headers=headers)

# Print response
print(f"Response Status Code: {response.status_code}")
print(f"Response Text: {response.text}")

# Check if request was successful
if response.status_code == 200:
    print("✅ Xcode Cloud Workflow triggered successfully!")
else:
    print("❌ Failed to trigger Xcode Cloud Workflow.")
    exit(1)
