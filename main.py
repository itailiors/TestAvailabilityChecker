import requests

# Configuration
API_URL = "https://proxy.nite.org.il/net-registration/days-by-month-and-center?networkExamId=3&monthForward=1&centerId=2"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

def check_slots_and_notify():
    # Step 1: Request the API with headers
    response = requests.get(API_URL, headers=headers)

    # Step 2: Check the status code
    if response.status_code == 200:
        try:
            available_slots = response.json()
            slots_less_than_10 = [slot for slot in available_slots if slot < 10]

            if slots_less_than_10:
                print(f"Available slots less than 10: {slots_less_than_10}")
            else:
                print("No slots available that are less than 10.")

        except requests.exceptions.JSONDecodeError:
            print("Failed to parse response as JSON. Response content:")
            print(response.text)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        print("Response content:")
        print(response.text)

if __name__ == "__main__":
    check_slots_and_notify()
