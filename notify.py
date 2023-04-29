import requests
import json
import base64
import sys

def send_slack_notification(title, external_ip, internal_ip, hostname, username, slack_webhook_url):

    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "attachments": [
            {
                "color": "#0076D7",
                "title": title,
                "text": "New Beacon notification",
                "fields": [
                    {
                        "title": "New Beacon from:",
                        "value": external_ip
                    },
                    {
                        "title": "Internal IP:",
                        "value": internal_ip
                    },
                    {
                        "title": "Host name:",
                        "value": hostname
                    },
                    {
                        "title": "User name:",
                        "value": username
                    }
                ]
            }
        ]
    }
    try:
        json.loads(json.dumps(payload))
    except ValueError as e:
        print(f"Invalid JSON: {e}")

    response = requests.post(slack_webhook_url, headers=headers, data=json.dumps(payload))
    #print(response.status_code)
    return response.status_code

if __name__ == "__main__":
    # Replace the slack_webhook_url variable with your own Slack webhook URL
    slack_webhook_url = "https://hooks.slack.com/services/"
    
    title = sys.argv[1]
    external_ip = sys.argv[2].split(':')[1].strip()
    internal_ip = sys.argv[3].split(':')[1].strip()
    hostname = sys.argv[4].split(':')[1].strip()
    username = sys.argv[5].split(':')[1].strip()
    
    send_slack_notification(title, external_ip, internal_ip, hostname, username, slack_webhook_url)
