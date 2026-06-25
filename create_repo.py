import requests, json

token_line = open(r"C:\Users\82578\.git-credentials").read().strip()
token = token_line.split(":")[-1].split("@")[0]

resp = requests.post(
    "https://api.github.com/user/repos",
    headers={"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"},
    json={"name": "paper-super-reviewer", "description": "Paper Super Reviewer - CCFA+Nature+PaperSpine peer review system", "private": False}
)
print(json.dumps(resp.json(), indent=2))
