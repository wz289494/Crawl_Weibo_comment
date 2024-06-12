import time
from main import Main
import pandas as pd

main = Main()

df = pd.read_excel('烟卡数据.xlsx')
uidlist = df['UID'].tolist()

n = 1
for uid in uidlist:
    print(f'-当前进度:{n}/{len(uidlist)},uid:{uid}')
    main.get_comment_info(uid)
    time.sleep(2)

    n += 1