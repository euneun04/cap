import pandas as pd

d1 = {"임석현": 100, "박종범":95, "성수경":90, "이준석":85, "김영일":80, "최재범":80, "박효순":80}

sr1 = pd.Series(d1, name = "명단")

print(sr1)