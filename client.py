import pandas as pd
import requests
import concurrent.futures

MAIN_URL = "http://localhost:8000/get/"
# Function to send a single request and print the response
def send_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: {response.status_code} - {response.text}")


df = pd.read_csv('example.input.data')
def extract_first_part(text):
    return text.split(' ')[0]

# Apply the function to each element in the DataFrame using applymap
df_processed = df.applymap(lambda x: extract_first_part(x))
urls = []
urls += [i[0] for i in df_processed.values.tolist()[:100]]

# Create a thread pool executor with a maximum of 5 threads (you can adjust this number)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Submit each URL to the executor to send requests concurrently
    futures = [executor.submit(send_request, MAIN_URL + url) for url in urls]

    # Wait for all tasks to complete
    concurrent.futures.wait(futures)
