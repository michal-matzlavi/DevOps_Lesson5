import requests

response = requests.get("https://api.github.com/users/avielb/repos")
my_repos = response.json()
for repo in  my_repos:
    print(repo["full_name"])