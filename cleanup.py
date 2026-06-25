import requests

token_line = open(r"C:\Users\82578\.git-credentials").read().strip()
token = token_line.split(":")[-1].split("@")[0]

OWNER = "TheeTarnished"
REPO = "paper-super-reviewer"
API = f"https://api.github.com/repos/{OWNER}/{REPO}/contents"
HEADERS = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

# Files to DELETE (contain experiment details):
to_delete = ["ab_test_report.pdf", "ab_test_report.tex", "REVIEW_REPORT.md"]

for f in to_delete:
    try:
        r = requests.get(f"{API}/{f}", headers=HEADERS, timeout=15)
        if r.status_code == 200:
            sha = r.json()["sha"]
            dr = requests.delete(f"{API}/{f}", headers=HEADERS, 
                json={"message": f"Remove {f} - experiment details only", "sha": sha}, timeout=15)
            if dr.status_code == 200:
                print(f"  ✅ Deleted {f}")
            else:
                print(f"  ❌ {f}: {dr.json().get('message')}")
        else:
            print(f"  ⚠️ {f} not found")
    except Exception as e:
        print(f"  💥 {f}: {e}")

print("Done")
