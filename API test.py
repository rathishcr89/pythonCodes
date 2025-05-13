import requests
import time
from collections import Counter
import argparse

# Configuration
API_URL = "https://jsonplaceholder.typicode.com/posts"  # Test API URL
# Parse runtime parameter
parser = argparse.ArgumentParser(description="API Test Script")
parser.add_argument("--total_requests", type=int, default=100, help="Total number of API requests to send")
args = parser.parse_args()

TOTAL_REQUESTS = args.total_requests

# Tracking variables
response_times = []
status_codes = []

# Request loop
for i in range(TOTAL_REQUESTS):
    start = time.time()
    try:
        response = requests.get(API_URL)
        elapsed = time.time() - start

        response_times.append(elapsed)
        status_codes.append(response.status_code)

        print(f"Request {i+1}: Status {response.status_code}, Time {elapsed:.3f}s")
    except Exception as e:
        response_times.append(None)
        status_codes.append("EXCEPTION")
        print(f"Request {i+1}: Exception occurred - {e}")

# Analysis
valid_times = [t for t in response_times if t is not None]
print("\n--- API Performance Summary ---")
print(f"Total Requests: {TOTAL_REQUESTS}")
print(f"Successful Requests: {status_codes.count(200)}")
print(f"Failed Requests: {status_codes.count('EXCEPTION')}")
print(f"Average Response Time: {sum(valid_times)/len(valid_times):.3f}s")
print(f"Max Response Time: {max(valid_times):.3f}s")
print(f"Min Response Time: {min(valid_times):.3f}s")

# Status code distribution
code_counts = Counter(status_codes)
print("\nStatus Code Distribution:")
for code, count in code_counts.items():
    print(f"  {code}: {count}")