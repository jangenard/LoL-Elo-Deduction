import re

def parse_team_score(texts):
    joined = " ".join(texts)
    nums = list(map(int, re.findall(r"\d+", joined)))

    if len(nums) >= 2:
        return nums[0], nums[1]
    return None, None

def parse_kda(texts):
    joined = " ".join(texts)
    match = re.search(r"(\d+)\s*/\s*(\d+)\s*/\s*(\d+)", joined)

    if match:
        return map(int, match.groups())
    return None, None, None

def parse_cs(texts):
    nums = list(map(int, re.findall(r"\d+", " ".join(texts))))
    return max(nums) if nums else None

def parse_time(texts):
    joined = " ".join(texts)

    match = re.search(r"(\d{1,2})[.:](\d{2})", joined)
    if match:
        minutes = int(match.group(1))
        seconds = int(match.group(2))
        return minutes + seconds / 60

    return None