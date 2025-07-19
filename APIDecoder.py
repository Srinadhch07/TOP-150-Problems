import base64

# Obfuscated API key (encoded in Base64)
obfuscated_key = "QUl6YVN5Qmx2Z1VRaDVZTHo3QjhtanVMcUJlcjgtX0I1OUYxMWNF"  # Replace with your encoded key

# Decode the key at runtime
api_key = base64.b64decode(obfuscated_key).decode('utf-8')
print(api_key)