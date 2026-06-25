import requests, base64, os, json

token_line = open(r"C:\Users\82578\.git-credentials").read().strip()
token = token_line.split(":")[-1].split("@")[0]

OWNER = "TheeTarnished"
REPO = "paper-super-reviewer"
API = f"https://api.github.com/repos/{OWNER}/{REPO}/contents"
HEADERS = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

def get_sha(path):
    try:
        r = requests.get(f"{API}/{path}", headers=HEADERS, timeout=15)
        if r.status_code == 200:
            return r.json().get("sha")
    except:
        pass
    return None

files = ["README.md","SKILL.md","REVIEW_REPORT.md","ab_test_report.pdf","ab_test_report.tex","templates/review_report_template.md"]
REPO_DIR = r"C:\Users\82578\Desktop\paper-super-reviewer"

for rel in files:
    fpath = os.path.join(REPO_DIR, rel)
    if not os.path.exists(fpath):
        print(f"  SKIP {rel}")
        continue
    content = base64.b64encode(open(fpath,'rb').read()).decode()
    sha = get_sha(rel)
    body = {"message": f"Update {rel}", "content": content}
    if sha: body["sha"] = sha
    try:
        r = requests.put(f"{API}/{rel}", headers=HEADERS, json=body, timeout=30)
        s = r.json()
        if 'content' in s: print(f"  ✅ {rel}")
        else: print(f"  ❌ {rel}: {s.get('message','?')}")
    except Exception as e:
        print(f"  💥 {rel}: {e}")

print(f"\nhttps://github.com/{OWNER}/{REPO}")
