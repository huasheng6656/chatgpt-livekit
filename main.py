import uuid

import requests

chatgpt_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJzZXNzaW9uX2lkIjoiS2xvSVBlSEQyS0xMbU5hb2h0NGY1WVhLd2lscmhLTnkiLCJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJ1c2c3ZnF6bXU5QGhvdG1haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsicG9pZCI6Im9yZy1iY3pNNmNzUU1PeThmTHRmT0EyM1N3ZlgiLCJ1c2VyX2lkIjoidXNlci1taVYxYTNHVVVubDB4bE11OUJsRkYza0wifSwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5vcGVuYWkuY29tLyIsInN1YiI6ImF1dGgwfDY2OGViODZhYmI2YTY3NjY5YTliMWQ3YSIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MjI4NTQ1NTEsImV4cCI6MTcyMzcxODU1MSwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSBtb2RlbC5yZWFkIG1vZGVsLnJlcXVlc3Qgb3JnYW5pemF0aW9uLnJlYWQgb3JnYW5pemF0aW9uLndyaXRlIG9mZmxpbmVfYWNjZXNzIiwiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEcifQ.N3hM_pzpZYQ7MqENy-xQc-Vl6Krr1n05A1T-7zCsn__M82WOz6x6V4qcAjsmduBGANF0VaygAvcu5Ch2l0TALfYfX6__r8piVdmmQqE-J5JuP6Dok1YXO7Gw71mzqISLm7XKcEUrpylOw6SQddIPBAdeAr7DOMVUAO_O3TkxNrYhWgQEFsrjQSC7wRTCz28F2ua5KYcJ1bzhwsAwT9wf1lws-awt5o_LqTOGFvfeBNfd0eIaPYMoeOY68KBeOtF-L5hd04b-WDg0j3TaN9WilOfjlzjr5QJvm9qHMpi6GcjQQWUWtSiPz0oSCgppB2jlVVD67wNGTkzWu68zjgLN9w"



def get_livekit_url():
    headers = {
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "authorization": "Bearer {}".format(chatgpt_token),
    }

    res = requests.post("https://chatgpt.com/voice/get_token", headers=headers, cookies={'__cf_bm': ''}, json={
        "voice": "cove",
        "voice_mode": "standard",
        "parent_message_id": str(uuid.uuid4()),
        "model_slug": "auto",
        "voice_training_allowed": False,
        "enable_message_streaming": False,
        "language": "zh",
        "video_training_allowed": False,
        "voice_session_id": str(uuid.uuid4())
    }).json()

    # livekit url
    livekit_url = "https://meet.livekit.io"
    url = "{}/custom?liveKitUrl={}&token={}#{}".format(livekit_url, res["url"], res["token"], res["e2ee_key"])
    return url


if not chatgpt_token:
    print("Get ChatGPT Token: https://chatgpt.com/api/auth/session")
else:
    print(get_livekit_url())
