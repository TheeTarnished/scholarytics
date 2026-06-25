import requests, base64, os

token_line = open(r"C:\Users\82578\.git-credentials").read().strip()
token = token_line.split(":")[-1].split("@")[0]

OWNER, REPO = "TheeTarnished", "paper-super-reviewer"
API = f"https://api.github.com/repos/{OWNER}/{REPO}/contents"
H = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

def get_sha(path):
    r = requests.get(f"{API}/{path}", headers=H, timeout=15)
    return r.json().get("sha") if r.status_code == 200 else None

def push(path, local_path):
    if not os.path.exists(local_path):
        print(f"  SKIP {path} (no file)")
        return
    content = base64.b64encode(open(local_path,'rb').read()).decode()
    sha = get_sha(path)
    body = {"message": f"v2.1.0: {path}", "content": content}
    if sha: body["sha"] = sha
    r = requests.put(f"{API}/{path}", headers=H, json=body, timeout=30)
    ok = 'content' in r.json()
    print(f"  {'✅' if ok else '❌'} {path} {'— ' + r.json().get('message','') if not ok else ''}")

# Only push skill files — NO experiment data
BASE = r"C:\Users\82578\Desktop\paper-super-reviewer"

# 1. Delete any leftover experiment files
for f in ["ab_test_report.pdf","ab_test_report.tex","REVIEW_REPORT.md"]:
    sha = get_sha(f)
    if sha:
        r = requests.delete(f"{API}/{f}", headers=H, json={"message":"cleanup","sha":sha}, timeout=15)
        print(f"  {'✅' if r.status_code==200 else '❌'} delete {f}")
    else:
        print(f"  ⚪ no-op  {f}")

# 2. Push skill files only
push("SKILL.md", os.path.join(BASE, "SKILL.md"))
push("README.md", os.path.join(BASE, "README.md"))
push("templates/review_report_template.md", os.path.join(BASE, "templates", "review_report_template.md"))

print(f"\nhttps://github.com/{OWNER}/{REPO}")
