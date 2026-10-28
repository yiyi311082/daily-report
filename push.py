import requests
import json
import datetime
import os

WEBHOOKURL = os.environ.get("WEBHOOKURL")
CONTENT_URL = "https://keyanweiwu.github.io/daily-report/today.json"

def sendtowecom(content):
  data = {
    "msgtype": "markdown",
    "markdown": {"content": content}
  }
  headers = {"Content-Type": "application/json"}
  resp = requests.post(WEBHOOK_URL, data=json.dumps(data), headers=headers, timeout=10)
  return resp.json()

def main():
  today = datetime.date.today()
  weekday = today.weekday()
  if weekday >= 5:
    print("周末不推送")
    return
  
  resp = requests.get(CONTENT_URL, timeout=10)
  if resp.status_code == 200:
    content = resp.json().get("content", "")
    if content:
      result = sendtowecom(content)
      print(f"推送结果：{result}")
    else:
      print("内容为空")
  else:
    print(f"读取失败：{resp.status_code}")

if name == "main":
  main()
