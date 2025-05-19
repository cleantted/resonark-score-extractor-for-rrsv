import json
import sys

PLATFORM = [
    "PCVR",
    "PCDesktop",
    "QuestVR",
    "Mobile",
]

STATE = {
    500: "EX",
    400: "AP",
    300: "FC",
}


with open("./pt1.json") as f_pt1:
    pt1_json = json.load(f_pt1)

with open("./pt2.json") as f_pt2:
    pt2_json = json.load(f_pt2)

# [music, difficulty] であることを想定
with open("./list.tsv") as f_list:
    targets = [l.strip().split("\t") for l in f_list.readlines()]

# 楽曲のリストにする
pt1_list = list(map(lambda x: x[1], filter(lambda x: len(x[0]) > 6, pt1_json["items"].items())))
pt2_list = list(map(lambda x: x[1], filter(lambda x: len(x[0]) > 6, pt2_json["items"].items())))

# platform は、1種類しかない想定とする
assert pt1_list[0]["platform"] == pt2_list[0]["platform"], "pt1とpt2のplatformが一致しません"
platform = PLATFORM[pt1_list[0]["platform"]]
print(f"platform: {platform}", file=sys.stderr)

scores = dict()
for item in pt1_list + pt2_list:
    title = item["title"]
    difficulty = item["dName"]
    score = item["score"]
    teck_rate = item["tRate"]
    state = item["state"] 

    scores[(title, difficulty)] = (score, teck_rate, state)  

with open("./score.tsv", "w") as f_score, open("./state.tsv", "w") as f_state:
    for title, difficulty in targets:
        score, teck_rate, state = scores.get((title, difficulty), (0, 0, 0))
        state = STATE.get(state, "")
        print(f"{score}\t{teck_rate}", file=f_score)
        print(f"{state}", file=f_state)
