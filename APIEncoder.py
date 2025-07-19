import base64

api_key = "AIzaSyBlvgUQh5YLz7B8mjuLqBer8-_B59F11cE"  # Replace with your actual API key
encoded_key = base64.b64encode(api_key.encode('utf-8')).decode('utf-8')
print("Encoded API Key:", encoded_key)