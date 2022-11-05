import requests
import pytest

presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Buren",
              "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln",
              "Johnson", "Grant", "Hayes", "Garfield", "Arthur", "Cleveland", "Harrison",
              "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover", "Truman",
              "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter", "Reagan", "Bush",
              "Clinton", "Obama", "Trump", "Biden"]

url_ddg = "https://api.duckduckgo.com"


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]


def test_ddg_presidents():
    resp = requests.get(url_ddg + "/?q=Presidents%20of%20the%20United%20States&format=json")
    rsp_data = resp.json()

    body_content = ""

    for item in rsp_data["RelatedTopics"]:
        body_content += item["Result"]

    all_presidents_present = True

    for president in presidents:
        if president not in body_content:
            all_presidents_present = False

    assert all_presidents_present
