import requests, base64, os

token_line = open(r"C:\Users\82578\.git-credentials").read().strip()
token = token_line.split(":")[-1].split("@")[0]

OWNER = "TheeTarnished"
REPO = "paper-super-reviewer"
API = f"https://api.github.com/repos/{OWNER}/{REPO}/contents"
H = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

def get_sha(path):
    try:
        r = requests.get(f"{API}/{path}", headers=H, timeout=15)
        return r.json().get("sha") if r.status_code == 200 else None
    except: return None

def delete(path):
    sha = get_sha(path)
    if sha:
        r = requests.delete(f"{API}/{path}", headers=H, json={"message":"cleanup","sha":sha}, timeout=15)
        return f"✅ deleted" if r.status_code == 200 else f"❌ {r.json().get('message')}"
    return "not found"

def push(path):
    fpath = r"C:\Users\82578\Desktop\paper-super-reviewer" + "\\" + path.replace("/","\\")
    if not os.path.exists(fpath): return f"SKIP - no local file"
    content = base64.b64encode(open(fpath,'rb').read()).decode()
    sha = get_sha(path)
    body = {"message": f"Update {path}", "content": content}
    if sha: body["sha"] = sha
    r = requests.put(f"{API}/{path}", headers=H, json=body, timeout=30)
    s = r.json()
    return "✅" if 'content' in s else f"❌ {s.get('message','?')}"

# Step 1: DELETE experiment files
for f in ["ab_test_report.pdf","ab_test_report.tex","REVIEW_REPORT.md"]:
    print(f"  {delete(f):20s} {f}")

# Step 2: PUSH only skill files
for f in ["README.md","SKILL.md","templates/review_report_template.md"]:
    print(f"  {push(f):20s} {f}")

print(f"\nhttps://github.com/{OWNER}/{REPO}")
