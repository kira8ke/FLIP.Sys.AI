import requests
from config FLIP_API_ENDPOINT, TEST_PAYLOAD
import time

def check_api_health():
    try:
        response = request.get(FLIP_API_ENDPOINT, timeout=5)
        if response.status_code == 200:
            print(" API is reachable and responding")
        else:
            print(" API is not reachable and not responding")
    except requests.exceptions.RequestException as e :
        print(" API health check failed : {e}")

def test_data_submission():
    try:
        response = request.post (FLIP_API_ENDPOINT, json=TEST_PAYLOAD, timeout=5)
        if response.status_code == [200,201]:
           print(" Submission successful")
        else:
            print(" Submission unsuccessful. Status {response.status_code} Message {response.message}")
    except requests.exceptions.RequestException as e :
         print(" Data submission failed : {e}")
         
def run_health_checks():
    print("\n Running Health check on API endpoint and testing data uptake")
    print("Timestamp" time.ctime)
    print("="* 60)

    check_api_health()
    test_data_submission()

    print("="* 60)
    
if __name__ == "__main__";
    run_health_check()
    
