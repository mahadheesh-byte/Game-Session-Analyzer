import time
import psutil as p 
import win32gui as w
import win32process as wi
from collections import defaultdict
import csv
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

fps_time = 0
moba_time = 0
story_time = 0
total_time = 0
model = LinearRegression()

usage_time = defaultdict(float)

current_app = None
start_time = time.time()

fps_games = [
    "VALORANT.exe",
    "cs2.exe",
    "csgo.exe",
    "callofduty.exe",
    "modernwarfare.exe",
    "warzone.exe",
    "apexlegends.exe",
    "overwatch.exe",
    "overwatch2.exe",
    "rainbowsix.exe",
    "battlefield2042.exe",
    "battlefieldv.exe",
    "escapeFromTarkov.exe",
    "halo.exe",
    "haloInfinite.exe",
    "doom.exe",
    "doomEternal.exe",
    "farcry5.exe",
    "farcry6.exe",
    "pubg.exe",
    "Taskmgr.exe"
]
story_games = [
    "gta5.exe",
    "reddeadredemption2.exe",
    "witcher3.exe",
    "cyberpunk2077.exe",
    "eldenring.exe",
    "sekiro.exe",
    "skyrim.exe",
    "fallout4.exe",
    "fallout76.exe",
    "assassinscreed.exe",
    "assassinscreedodyssey.exe",
    "assassinscreedvalhalla.exe",
    "tombraider.exe",
    "shadowofthetombraider.exe",
    "riseofthetombraider.exe",
    "horizonzerodawn.exe",
    "deathstranding.exe",
    "godofwar.exe",
    "spiderman.exe",
    "spidermanremastered.exe"
]
moba_games = [
    "dota2.exe",
    "leagueclient.exe",
    "leagueoflegends.exe",
    "smite.exe",
    "heroesofthestorm.exe",
    "vainglory.exe"
]


def data1():



    df = pd.read_csv(r"C:\Users\lenovo loq\cafe\sessions.csv")

    df.columns = df.columns.str.strip()

    print(df.columns)
   
    x1 = df[['session_length']]
    y1 = df[['fps_time']]



    print(df.columns)

    model.fit(x1 , y1)

    y_line1 = model.predict(x1)

    plt.scatter(df['session_length'], df['fps_time'])
    plt.plot(x1, y_line1, color='red', linewidth=2, label='Relationship Line') 
    plt.xlabel("Session Length (seconds)")
    plt.ylabel("time spent for fps_games")
    plt.title("fps_time")
    plt.legend()
    plt.show()
   
    pre1 = np.array([[int(input("amount of time alotted to predict for fps_time:"))]])

    if not pre1 <= 0:
        
        print(model.predict(pre1))

def data2():
    


    df = pd.read_csv(r"C:\Users\lenovo loq\cafe\sessions.csv")

    df.columns = df.columns.str.strip()

    print(df.columns)
   
    x2 = df[['session_length']]
    y2 = df[['story_time']]



    print(df.columns)

    

    model.fit(x2 , y2)

    y_line2 = model.predict(x2)

    plt.scatter(df['session_length'], df['story_time'])
    plt.plot(x2, y_line2, color='red', linewidth=2, label='Relationship Line') 
    plt.xlabel("Session Length (seconds)")
    plt.ylabel("time spent for story_time games")
    plt.title("story_time")
    plt.show()


    pre2 = np.array([[int(input("amount of time alotted to predict for storygames:"))]])

    if not pre2 <= 0:
        print(model.predict(pre2))



def data3():
    

    df = pd.read_csv(r"C:\Users\lenovo loq\cafe\sessions.csv")

    df.columns = df.columns.str.strip()

    print(df.columns)
   
    x3 = df[['session_length']]
    y3 = df[['moba_time']]



    print(df.columns)

    model.fit(x3 , y3)

    y_line3 = model.predict(x3)

    plt.scatter(df['session_length'], df['moba_time'])
    plt.plot(x3, y_line3, color='red', linewidth=2, label='Relationship Line') 
    plt.xlabel("Session Length (seconds)")
    plt.ylabel("time spent for moba_time games")
    plt.title("moba_time")
    plt.show()

    pre3 = np.array([[int(input("amount of time alotted to predict for moba:"))]])

    if pre3 > 0 : 
        print(model.predict(pre3))




try:

    while True:
        
        try:
            hnd = w.GetForegroundWindow()
            _ , pid = wi.GetWindowThreadProcessId(hnd)

            if pid <= 0:
                continue
            app = p.Process(pid).name()

        except p.NoSuchProcess:
            continue
           

        now = time.time()

        if app != current_app:
            if current_app is not None:
                usage_time[current_app] += now - start_time

            start_time = now
            
            current_app = app

except KeyboardInterrupt:


    print("stopped")

    if current_app:
        usage_time[current_app] += time.time() - start_time

    with open("usage.csv" , "w" , newline="") as file:
        writer = csv.writer(file)

        for app , seconds in usage_time.items():
            hour = int(seconds / 60 / 60) 
            mini = int(seconds / 60)  
            writer.writerow([app , hour , mini , int(seconds)])
    
    for app, seconds in usage_time.items():
    
    
        if app in fps_games:
            fps_time += seconds
        
        elif app.lower() in story_games:
            story_time += seconds
        
        elif app.lower() in moba_games:
            moba_time += seconds

    with open("sessions.csv" , "w" , newline="") as f:
        wrt = csv.writer(f)
        wrt.writerow(['fps_time' , 'story_time' , 'moba_time' , 'session_length'])
        wrt.writerow([6.08,0,0,6.0])
        wrt.writerow([fps_time , story_time , moba_time , int(seconds) ])
        
    while True:
        leave = input("press 1 to check fps_time \n press 2 to check storygame_time \n press 3 to check moba_time \n and to 0 to leave: ")


        if leave == "1":
            data1()

        if leave == "2":
            data2()

        if leave == "3":
            data3()
            
        if leave == "0":
            break 
            
