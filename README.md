🎮 Game Session Analyzer

Track which applications you use, categorize games by genre, and analyze how much time you spend playing them.

This Python project monitors the foreground application in Windows, records usage time, classifies games into categories (FPS, Story, MOBA), and uses linear regression to predict how long you might spend playing based on session length.

It also visualizes the relationship between session length and time spent in each genre.

🚀 Features

⏱ Real-time application usage tracking

🎮 Automatic game classification

📊 Usage statistics export to CSV

📈 Visualization with Matplotlib & Seaborn

🤖 Machine learning prediction using Linear Regression

📁 Session data storage for future analysis

🧠 How It Works
1️⃣ Application Monitoring

The script continuously checks the foreground window using Windows APIs.

It retrieves the process name and measures how long each application stays active.

2️⃣ Usage Tracking

Time spent in each application is stored in:

usage_time = defaultdict(float)

Example output:

VALORANT.exe → 7200 seconds
chrome.exe → 1800 seconds
3️⃣ Game Categorization

Games are grouped into three categories:

Category	Examples
FPS	Valorant, CS2, Call of Duty
Story	GTA V, Witcher 3, Cyberpunk
MOBA	Dota 2, League of Legends

The program sums time spent in each category.

4️⃣ Data Storage

Session results are stored in:

usage.csv
sessions.csv

Example:

fps_time,story_time,moba_time,session_length
3600,1200,600,5400
5️⃣ Machine Learning Prediction

A Linear Regression model is trained on past session data.

The model predicts how much time a player may spend in each genre given a total session length.

Example:

Session Length: 7200 seconds
Predicted FPS Time: 5100 seconds
📊 Data Visualization

The program generates scatter plots showing the relationship between session length and time spent playing each genre.

Example graphs:

Session length vs FPS playtime

Session length vs Story playtime

Session length vs MOBA playtime

A regression line shows the predicted relationship.
