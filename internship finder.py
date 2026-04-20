import requests


keyword = input("Enter job keyword: ").lower()


url = "https://www.arbeitnow.com/api/job-board-api"

response = requests.get(url)

data = response.json()


jobs = data["data"]

print("Latest matching jobs:\n")

count = 0

for job in jobs:
    title = job["title"]
    company = job["company_name"]
    location = job["location"]
    link = job["url"]

    if keyword.lower() in title.lower():
        count += 1
        print(f"{count}. {title}")
        print(f"   Company: {company}")
        print(f"   Location: {location}")
        print(f"   Apply here: {link}\n")

  
    if count == 5:
        break

if count == 0:
    print("No matching jobs found.")
