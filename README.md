**Fast API key/value server**

---

### Project Overview
This project hosts the key/value server in Redis using FastAPI. It contains a simple FastAPI web application (`main.py`) integrated with Redis for key-value data storage. Additionally, it includes a client script (`client.py`) to demonstrate concurrent HTTP requests to the FastAPI server and a script (`data.py`) to load data into Redis from a file. Furthermore, it contains test cases (`test_main.py`) for the FastAPI endpoints using `pytest`.

### Files Included
1. **main.py**: This file contains the FastAPI application with an endpoint to retrieve values from Redis based on a given key.

2. **client.py**: This script demonstrates concurrent HTTP requests to the FastAPI server using Python's `concurrent.futures.ThreadPoolExecutor`.

3. **data.py**: This script is responsible for loading data from a file into Redis using the `redis` library.

4. **tests/test_main.py**: This file contains test cases for the FastAPI endpoints using `pytest`. It verifies the functionality of the `/get/{key}` endpoint.

### Usage
1. **Setting Up Environment**: Ensure you have Python installed on your system. Additionally, install the required dependencies using pip:
   ```
   pip install fastapi uvicorn requests pandas pytest redis
   ```

2. **Loading Data into Redis**: Before running the client script or tests, load data into Redis by executing `data.py`:
   ```
   python data.py
   ```

3. **Running the FastAPI Server**: Execute `main.py` to run the FastAPI server:
   ```
   python main.py
   ```

4. **Sending Concurrent Requests**: Run the client script to send concurrent requests to the FastAPI server:
   ```
   python client.py
   ```

5. **Running Tests**: Execute the test script to run the test cases:
   ```
   pytest tests/test_main.py
   ```

### Configuration
- **Redis Configuration**: The Redis connection parameters (`host`, `port`, `db`) can be configured in `data.py` and `main.py` according to your Redis setup.

- **FastAPI Server Configuration**: You can modify the host and port settings in `main.py` as per your requirements.

### Note
- Ensure that Redis is running and accessible before running the application and tests.
- Adjust the number of concurrent threads in `client.py` (`max_workers`) based on your system's capabilities and requirements.

### Dependencies
- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python.
- Uvicorn: A lightning-fast ASGI server implementation, using uvloop and httptools.
- Redis: A Python client library for Redis, the in-memory data structure store.
- Requests: A simple HTTP library for making requests and working with responses.
- Pandas: A powerful data manipulation and analysis library.
- Pytest: A framework for building simple and scalable test cases.

### Queries
- **How much data can your server handle? How could you improve it so it can handle even larger datasets?**

   This implementation can handle millions of key-value pairs reasonably well due to utilizing Redis as an in-memory key-value store. 
   Redis offers significant performance benefits compared to storing data in a dictionary within the server itself.
   However, this performance further can be improved by tuning redis configurations like memory allocation, eviction policies and persistence options   

- **How many milliseconds it takes for the client to get a response on average? How could you improve the latency?**

    This system has been tested by calling multiple concurrent responses. Average response time by server is 0.01 seconds.
    Latency can be improved by many ways including Optimizing Network Configurations, Performance Tuning, Caching, Load Balancing and utilizing CDN's.
  
- **What are some failure patterns that you can anticipate?**

    Some failure patterns that can be anticipated include:

    - Network Failures: Communication failures between the client and server due to network issues such as packet loss, latency, or network congestion.
    
    - Server Overload: The server may become overloaded and unresponsive due to a sudden surge in incoming requests, hardware failures, or software issues.
    
    - Database Errors: In this case, it is Redis so there can be issues related to Redis, its configuration and sometimes If data gets increase to billions 
      of key value pairs.

### Author
Talha Zubair

