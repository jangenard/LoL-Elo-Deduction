import csv

from pathlib import Path 

from rank_deduction.data.ocr import ocr_region
from rank_deduction.data.ocr_parsing import parse_team_score, parse_kda, parse_cs, parse_time

CSV_PATH = "outputs/stats.csv"

FIELDNAMES = [
    "image",
    "rank",
    "total_kills_per_min",
    "kills_per_min",
    "deaths_per_min",
    "kda_ratio",
    "kill_participation",
    "cs_per_min",
    "time"
]
def write_row(row):
    file_exists = Path(CSV_PATH).exists()

    with open(CSV_PATH, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)

        if not file_exists:
            writer.writeheader()

        writer.writerow(row)

def create_csv(dataset) :
    for sample in dataset:
        score_img = sample["crop_score"]
        kda_img = sample["crop_kda"]
        cs_img = sample["crop_cs"]
        time_img = sample["crop_time"]

        rank = sample["rank"]
        filename = sample["filename"]

        score_text = ocr_region(score_img)
        kda_text = ocr_region(kda_img)
        cs_text = ocr_region(cs_img)
        time_text = ocr_region(time_img)

        team_kills, enemy_kills = parse_team_score(score_text)
        kills, deaths, assists  = parse_kda(kda_text)
        cs = parse_cs(cs_text)
        time = parse_time(time_text)

        if None in [team_kills, enemy_kills, kills, deaths, assists, cs, time]:
            print(f"[SKIP] OCR failed for {filename}")
            continue


        total_kills_per_min = round((team_kills + enemy_kills) / time, 1)
        kda = round((kills + assists) / (deaths + 1), 2)
        kills_per_min = round(kills / time, 1)
        deaths_per_min = round(deaths / time, 1)
        
        if (kills == 0 and assists == 0) or team_kills == 0 :
            kill_participation=0
        else :
            kill_participation = round((kills + assists) / team_kills, 1)
        cs_per_min = round(cs / time, 2)

        row = {
            "image": filename,
            "rank": rank,
            "total_kills_per_min": total_kills_per_min,
            "kills_per_min": kills_per_min,
            "deaths_per_min": deaths_per_min,
            "kda_ratio": kda,
            "kill_participation": kill_participation,
            "cs_per_min": cs_per_min,
            "time": time
        }
        

        write_row(row)