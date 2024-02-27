import redis
def load_data(file):
  # Replace with your Redis configuration
  redis_client = redis.Redis(host='127.0.0.1', port=6379, db=0)

  # Open the data file and iterate over each line
  with open(file, 'r') as f:
      for line in f:
          key, value = line.strip().split(' ', 1)
          # Add the key-value pair to Redis using HSET
          redis_client.hset('data', key, value)
load_data('example.input.data')
print("Data loaded successfully!")

