import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        
        response = requests.get(self.url)
        return response.content  # Return the raw response body exactly as a string

    def load_json(self):
       
        response_body = self.get_response_body()  # Get the raw response body as a string
        return json.loads(response_body)  # Parse the raw string into a Python data structure
