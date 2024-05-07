import json
import requests

from setting.general import webhook_slack


def test_send_report_slack():
    jsonContent = open("test_bag.json", 'r').read()
    data_json = json.loads(jsonContent)

    test_success = len(data_json.get("success"))
    test_failed = len(data_json.get("failed"))
    test_all = test_success + test_failed
    success_rate = test_success / test_all * 100

    if test_failed > 0:
        color = "FF1E00"
    else:
        color = "2B7A0B"
    sr = round(success_rate, 2)

    param = {
        "attachments": [
            {
                "color": str(color),
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": f"API AUTOMATION",
                            "emoji": True
                        }
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": f"*Success Test:*\n {test_success}"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Failed Test:*\n {test_failed}"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": "*Skipped Test:*\n0"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Total Test:*\n {test_all}"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": f"*Success Rate:*\n {sr}%"
                            }
                        ]
                    }
                ]
            }
        ]
    }

    header = {
        "content-type": "application/x-www-form-urlencoded"
    }
    requests.post(webhook_slack, json=param, headers=header)