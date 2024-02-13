import requests
from bs4 import BeautifulSoup

import requests

def get_model_list():
    url = "https://huggingface.co/models"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the HTML content of the webpage
        soup = BeautifulSoup(response.content, "html.parser")
        model_tags = soup.find_all("h4", class_=lambda x: x and "text-md" in x.split())
        model_list = [tag.text.strip() for tag in model_tags]

        return model_list
    else:
        print("Failed to retrieve the webpage.")

if __name__ == "__main__":
    models = get_model_list()
    if models:
        print("Model List:")
        for model in models:
            print(model)
    else:
        print("No models found.")
