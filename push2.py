import requests, base64, os

token_line = open(r"C:\Users\82578\.git-credentials").read().strip()
token = token_line.split(":")[-1].split("@")[0]

OWNER = "TheeTarnished"
REPO = "paper-super-reviewer"
API = f"https://api.github.com/repos/{OWNER}/{REPO}/contents"
HEADERS = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

REPO_DIR = r"C:\Users\82578\Desktop\paper-super-reviewer"

files_to_push = [
    "README.md",
    "SKILL.md",
    "REVIEW_REPORT.md",
    "ab_test_report.pdf",
    "ab_test_report.tex",
    "templates/review_report_template.md",
]

for rel in files_to_push:
    path = os.path.join(REPO_DIR, rel)
    if not os.path.exists(path):
        print(f"  ⚠️ SKIP {rel} (not found)")
        continue

    content = base64.b64encode(open(path, 'rb').read()).decode()
    try:
        resp = requests.put(
            f"{API}/{rel}",
            headers=HEADERS,
            json={"message": f"Add/update {rel}", "content": content},
            timeout=30
        )
        status = resp.json()
        if 'content' in status:
            print(f"  ✅ {rel}")
        else:
            print(f"  ❌ {rel}: {status.get('message','?')}")
    except Exception as e:
        print(f"  💥 {rel}: {e}")

print(f"\nhttps://github.com/{OWNER}/{REPO}")
