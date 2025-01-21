## Import packages
import pandas as pd

## Import CSV files
case1= pd.read_csv('Case1_SQL.csv')
case2= pd.read_csv('Case2_SQL.csv')
case3= pd.read_csv('Case3_SQL.csv')
case4= pd.read_csv('Case4_SQL.csv')
case5= pd.read_csv('Case5_SQL.csv')
case6= pd.read_csv('Case6_SQL.csv')
case7= pd.read_csv('Case7_SQL.csv')
case8= pd.read_csv('Case8_SQL.csv')
case9= pd.read_csv('Case9_SQL.csv')
case10= pd.read_csv('Case10_SQL.csv')
case11= pd.read_csv('Case11_SQL.csv')

## Create final DataFrames
# Case 1: Home and away games - wins and losses
  # Filter home and away games
home_games1 = case1[case1["home_or_away"] == "HOME"]
away_games1 = case1[case1["home_or_away"] == "AWAY"]
print(home_games1)
print(away_games1)

    # Sum results
home_results1 = home_games1.groupby("playerTeam")["result"].value_counts().reset_index(name='result_count')
away_results1 = away_games1.groupby("playerTeam")["result"].value_counts().reset_index(name='result_count')
print(home_results1)
print(away_results1)

    # Create a DataFrame
#results_summary1 = pd.DataFrame({
#    "Team": home_results1.index,
#    "Home": home_results1.values,
#    "Away": away_results1.values,
#})
#print(results_summary1)

# CASE 2: Home and away games - goals scored and goals conceded
    # Filter home and away games
home_games2 = case2[case2["home_or_away"] == "HOME"]
away_games2 = case2[case2["home_or_away"] == "AWAY"]
print(home_games2)
print(away_games2)

    # Sum results
home_results2 = home_games2.groupby("playerTeam")[["TotalGoalsFor", "TotalGoalsAgainst"]].sum()
away_results2 = away_games2.groupby("playerTeam")[["TotalGoalsFor", "TotalGoalsAgainst"]].sum()
print(home_results2)
print(away_results2)

# CASE 3: Goals scored in 5on5 situations
  # Filter home and away games
home_games3 = case3[case3["home_or_away"] == "HOME"]
away_games3 = case3[case3["home_or_away"] == "AWAY"]
print(home_games3)
print(away_games3)

    # Sum results
home_results3 = home_games3.groupby("playerTeam")[["TotalGoalsFor", "TotalGoalsAgainst"]].sum()
away_results3 = away_games3.groupby("playerTeam")[["TotalGoalsFor", "TotalGoalsAgainst"]].sum()
print(home_results3)
print(away_results3)

# CASE 4: Goals scored in 5on4 situations
    # Filter home and away games
home_games4 = case4[case4["home_or_away"] == "HOME"]
away_games4 = case4[case4["home_or_away"] == "AWAY"]
print(home_games4)
print(away_games4)

    # Sum results
home_results4 = home_games4.groupby("playerTeam")[["TotalGoalsFor", "TotalGoalsAgainst"]].sum()
away_results4 = away_games4.groupby("playerTeam")[["TotalGoalsFor", "TotalGoalsAgainst"]].sum()
print(home_results4)
print(away_results4)

# CASE 5: Goals scored in 4on5 situations
    # Filter home and away games
home_games5 = case5[case5["home_or_away"] == "HOME"]
away_games5 = case5[case5["home_or_away"] == "AWAY"]
print(home_games5)
print(away_games5)

    # Sum results
home_results5 = home_games5.groupby("playerTeam")[["TotalGoalsFor", "TotalGoalsAgainst"]].sum()
away_results5 = away_games5.groupby("playerTeam")[["TotalGoalsFor", "TotalGoalsAgainst"]].sum()
print(home_results5)
print(away_results5)

# CASE 6: Goals scored in other situations
    # Filter home and away games
home_games6 = case6[case6["home_or_away"] == "HOME"]
away_games6 = case6[case6["home_or_away"] == "AWAY"]
print(home_games6)
print(away_games6)

    # Sum results
home_results6 = home_games6.groupby("playerTeam")[["TotalGoalsFor", "TotalGoalsAgainst"]].sum()
away_results6 = away_games6.groupby("playerTeam")[["TotalGoalsFor", "TotalGoalsAgainst"]].sum()
print(home_results6)
print(away_results6)

# CASE 7: Shots on goals in total
    # Filter home and away games
home_games7 = case7[case7["home_or_away"] == "HOME"]
away_games7 = case7[case7["home_or_away"] == "AWAY"]
print(home_games7)
print(away_games7)

    # Sum results
home_results7 = home_games7.groupby("playerTeam")[["TotalShotsFor", "TotalShotsAgainst"]].sum()
away_results7 = away_games7.groupby("playerTeam")[["TotalShotsFor", "TotalShotsAgainst"]].sum()
print(home_results7)
print(away_results7)

# CASE 8: Shots on goals in 5on5
    # Filter home and away games
home_games8 = case8[case8["home_or_away"] == "HOME"]
away_games8 = case8[case8["home_or_away"] == "AWAY"]
print(home_games8)
print(away_games8)

    # Sum results
home_results8 = home_games8.groupby("playerTeam")[["TotalShotsFor", "TotalShotsAgainst"]].sum()
away_results8 = away_games8.groupby("playerTeam")[["TotalShotsFor", "TotalShotsAgainst"]].sum()
print(home_results8)
print(away_results8)

# CASE 9: Shots on goals in 5on4
    # Filter home and away games
home_games9 = case9[case9["home_or_away"] == "HOME"]
away_games9 = case9[case9["home_or_away"] == "AWAY"]
print(home_games9)
print(away_games9)

    # Sum results
home_results9 = home_games9.groupby("playerTeam")[["TotalShotsFor", "TotalShotsAgainst"]].sum()
away_results9 = away_games9.groupby("playerTeam")[["TotalShotsFor", "TotalShotsAgainst"]].sum()
print(home_results9)
print(away_results9)

# CASE 10: Shots on goals in 4on5
     # Filter home and away games
home_games10 = case10[case10["home_or_away"] == "HOME"]
away_games10 = case10[case10["home_or_away"] == "AWAY"]
print(home_games10)
print(away_games10)

    # Sum results
home_results10 = home_games10.groupby("playerTeam")[["TotalShotsFor", "TotalShotsAgainst"]].sum()
away_results10 = away_games10.groupby("playerTeam")[["TotalShotsFor", "TotalShotsAgainst"]].sum()
print(home_results10)
print(away_results10)
# CASE 11: Shots on goals in other situations
     # Filter home and away games
home_games11 = case11[case11["home_or_away"] == "HOME"]
away_games11 = case11[case11["home_or_away"] == "AWAY"]
print(home_games11)
print(away_games11)

    # Sum results
home_results11 = home_games11.groupby("playerTeam")[["TotalShotsFor", "TotalShotsAgainst"]].sum()
away_results11 = away_games11.groupby("playerTeam")[["TotalShotsFor", "TotalShotsAgainst"]].sum()
print(home_results11)
print(away_results11)


    ###### Visualisation
import matplotlib.pyplot as plt
import numpy as np

    ###### Visualisation Case 1: Home and away games - wins and losses
# Data Preparation for Case 1
teams = home_results1["playerTeam"].unique()  # List of teams
results = ["win", "lose", "draw"]  # Types of results

# Initialize arrays for home and away results
home_counts = {result: [] for result in results}
away_counts = {result: [] for result in results}

# Populate arrays with counts for each result type
for team in teams:
    for result in results:
        home_counts[result].append(
            home_results1[(home_results1["playerTeam"] == team) & (home_results1["result"] == result)]["result_count"].sum()
        )
        away_counts[result].append(
            away_results1[(away_results1["playerTeam"] == team) & (away_results1["result"] == result)]["result_count"].sum()
        )

# Numeric positions for teams
x = np.arange(len(teams))
width = 0.25  # Bar width

# Create the subplots (two plots side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot Home Results - Bar chart for Wins, Losses, and Draws
bars_home_win = ax1.bar(x - width, home_counts["win"], width, label="Home Wins", color="green")
bars_home_lose = ax1.bar(x, home_counts["lose"], width, label="Home Losses", color="red")
bars_home_draw = ax1.bar(x + width, home_counts["draw"], width, label="Home Draws", color="blue")

# Plot Away Results - Bar chart for Wins, Losses, and Draws
bars_away_win = ax2.bar(x - width, away_counts["win"], width, label="Away Wins", color="lightgreen", alpha=0.7)
bars_away_lose = ax2.bar(x, away_counts["lose"], width, label="Away Losses", color="salmon", alpha=0.7)
bars_away_draw = ax2.bar(x + width, away_counts["draw"], width, label="Away Draws", color="lightblue", alpha=0.7)

# Add annotations for each bar in Home plot (wins, losses, draws)
for bar in bars_home_win:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

for bar in bars_home_lose:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

for bar in bars_home_draw:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each bar in Away plot (wins, losses, draws)
for bar in bars_away_win:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

for bar in bars_away_lose:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

for bar in bars_away_draw:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Customize Home plot (ax1)
ax1.set_title("Case 1: Home Games - Wins, Losses, and Draws", fontsize=14)
ax1.set_xlabel("Teams", fontsize=12)
ax1.set_ylabel("Number of Games", fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(teams, rotation=90, fontsize=10)
ax1.legend(fontsize=10)
ax1.grid(axis="y", linestyle="--", alpha=0.7)

# Customize Away plot (ax2)
ax2.set_title("Case 1: Away Games - Wins, Losses, and Draws", fontsize=14)
ax2.set_xlabel("Teams", fontsize=12)
ax2.set_ylabel("Number of Games", fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(teams, rotation=90, fontsize=10)
ax2.legend(fontsize=10)
ax2.grid(axis="y", linestyle="--", alpha=0.7)

# Add a main title for the entire figure
fig.suptitle("Home and away games - wins, losses and draws", fontsize=16, ha='center', va='center', y=1.02)

# Set y-axis limits to start at 75 for better view
ax1.set_ylim([0, max(max(home_counts["win"]), max(home_counts["lose"]), max(home_counts["draw"]), max(away_counts["win"]), max(away_counts["lose"]), max(away_counts["draw"])) + 10])
ax2.set_ylim([0, max(max(home_counts["win"]), max(home_counts["lose"]), max(home_counts["draw"]), max(away_counts["win"]), max(away_counts["lose"]), max(away_counts["draw"])) + 10])

# Adjust layout and save the plot
plt.tight_layout()
output_file = "case1_home_away_comparison_with_annotations_updated.png"  # Output file name
plt.savefig(output_file, dpi=300, bbox_inches="tight")  # Save in the project directory

    ###### Visualisation CASE 2: Home and away games - goals scored and goals conceded
# Data Preparation
teams = home_results2.index  # List of teams
goals_for_home = home_results2["TotalGoalsFor"]  # Home goals scored
goals_against_home = home_results2["TotalGoalsAgainst"]  # Home goals conceded
goals_for_away = away_results2["TotalGoalsFor"]  # Away goals scored
goals_against_away = away_results2["TotalGoalsAgainst"]  # Away goals conceded

# Numeric positions for teams
x = np.arange(len(teams))
width = 0.35  # Bar width

# Create the subplots (two plots side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot Home Results - Bar chart for Goals Scored, Line chart for Goals Conceded
bars_home_for = ax1.bar(x - width/2, goals_for_home, width, label="Home Goals Scored", color="green", alpha=0.7)
ax1.plot(x, goals_against_home, label="Home Goals Conceded", color="red", marker="o", linestyle="--", linewidth=2)

# Plot Away Results - Bar chart for Goals Scored, Line chart for Goals Conceded
bars_away_for = ax2.bar(x - width/2, goals_for_away, width, label="Away Goals Scored", color="lightgreen", alpha=0.7)
ax2.plot(x, goals_against_away, label="Away Goals Conceded", color="salmon", marker="o", linestyle="--", linewidth=2)

# Add annotations for each bar in Home plot (goals scored)
for bar in bars_home_for:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each bar in Away plot (goals scored)
for bar in bars_away_for:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Home plot (goals conceded)
for i, point in enumerate(goals_against_home):
    ax1.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Away plot (goals conceded)
for i, point in enumerate(goals_against_away):
    ax2.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Customize Home plot (ax1)
ax1.set_title("Case 2: Home Games - Goals Scored (Bar) and Goals Conceded (Line)", fontsize=14)
ax1.set_xlabel("Teams", fontsize=12)
ax1.set_ylabel("Goals", fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(teams, rotation=90, fontsize=10)
ax1.legend(fontsize=10)
ax1.grid(axis="y", linestyle="--", alpha=0.7)

# Customize Away plot (ax2)
ax2.set_title("Case 2: Away Games - Goals Scored (Bar) and Goals Conceded (Line)", fontsize=14)
ax2.set_xlabel("Teams", fontsize=12)
ax2.set_ylabel("Goals", fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(teams, rotation=90, fontsize=10)
ax2.legend(fontsize=10)
ax2.grid(axis="y", linestyle="--", alpha=0.7)

# Add a main title for the entire figure
fig.suptitle("Goals Scored and Conceded", fontsize=16, ha='center', va='center', y=1.02)

# Set y-axis limits to start at 40 for better view
ax1.set_ylim([75, max(goals_for_home.max(), goals_against_home.max(), goals_for_away.max(), goals_against_away.max()) + 10])
ax2.set_ylim([75, max(goals_for_home.max(), goals_against_home.max(), goals_for_away.max(), goals_against_away.max()) + 10])

# Adjust layout and save the plot
plt.tight_layout()
output_file = "case2_goals_home_away_bar_line_comparison_with_annotations.png"  # Output file name
plt.savefig(output_file, dpi=300, bbox_inches="tight")  # Save in the project directory

    ###### Visualisation CASE 3: Goals scored in 5on5 situations
# Data Preparation
teams = home_results3.index  # List of teams
goals_for_home = home_results3["TotalGoalsFor"]  # Home goals scored
goals_against_home = home_results3["TotalGoalsAgainst"]  # Home goals conceded
goals_for_away = away_results3["TotalGoalsFor"]  # Away goals scored
goals_against_away = away_results3["TotalGoalsAgainst"]  # Away goals conceded

# Numeric positions for teams
x = np.arange(len(teams))
width = 0.35  # Bar width

# Create the subplots (two plots side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot Home Results - Bar chart for Goals Scored, Line chart for Goals Conceded
bars_home_for = ax1.bar(x - width/2, goals_for_home, width, label="Home Goals Scored", color="green", alpha=0.7)
ax1.plot(x, goals_against_home, label="Home Goals Conceded", color="red", marker="o", linestyle="--", linewidth=2)

# Plot Away Results - Bar chart for Goals Scored, Line chart for Goals Conceded
bars_away_for = ax2.bar(x - width/2, goals_for_away, width, label="Away Goals Scored", color="lightgreen", alpha=0.7)
ax2.plot(x, goals_against_away, label="Away Goals Conceded", color="salmon", marker="o", linestyle="--", linewidth=2)

# Add annotations for each bar in Home plot (goals scored)
for bar in bars_home_for:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each bar in Away plot (goals scored)
for bar in bars_away_for:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Home plot (goals conceded)
for i, point in enumerate(goals_against_home):
    ax1.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Away plot (goals conceded)
for i, point in enumerate(goals_against_away):
    ax2.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Customize Home plot (ax1)
ax1.set_title("Case 3: Home Games - Goals Scored (Bar) and Goals Conceded (Line)", fontsize=14)
ax1.set_xlabel("Teams", fontsize=12)
ax1.set_ylabel("Goals", fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(teams, rotation=90, fontsize=10)
ax1.legend(fontsize=10)
ax1.grid(axis="y", linestyle="--", alpha=0.7)

# Customize Away plot (ax2)
ax2.set_title("Case 3: Away Games - Goals Scored (Bar) and Goals Conceded (Line)", fontsize=14)
ax2.set_xlabel("Teams", fontsize=12)
ax2.set_ylabel("Goals", fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(teams, rotation=90, fontsize=10)
ax2.legend(fontsize=10)
ax2.grid(axis="y", linestyle="--", alpha=0.7)

# Add a main title for the entire figure
fig.suptitle("Goals Scored and Conceded in 5on5 Situations", fontsize=16, ha='center', va='center', y=1.02)

# Set y-axis limits to start at 40 for better view
ax1.set_ylim([40, max(goals_for_home.max(), goals_against_home.max(), goals_for_away.max(), goals_against_away.max()) + 10])
ax2.set_ylim([40, max(goals_for_home.max(), goals_against_home.max(), goals_for_away.max(), goals_against_away.max()) + 10])

# Adjust layout and save the plot
plt.tight_layout()
output_file = "case3_goals_home_away_bar_line_comparison_with_annotations.png"  # Output file name
plt.savefig(output_file, dpi=300, bbox_inches="tight")  # Save in the project directory

    ###### Visualisation CASE 4: Goals scored in 5on4 situations
# Data Preparation
teams = home_results4.index  # List of teams
goals_for_home = home_results4["TotalGoalsFor"]  # Home goals scored
goals_against_home = home_results4["TotalGoalsAgainst"]  # Home goals conceded
goals_for_away = away_results4["TotalGoalsFor"]  # Away goals scored
goals_against_away = away_results4["TotalGoalsAgainst"]  # Away goals conceded

# Numeric positions for teams
x = np.arange(len(teams))
width = 0.35  # Bar width

# Create the subplots (two plots side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot Home Results - Bar chart for Goals Scored, Line chart for Goals Conceded
bars_home_for = ax1.bar(x - width/2, goals_for_home, width, label="Home Goals Scored", color="green", alpha=0.7)
ax1.plot(x, goals_against_home, label="Home Goals Conceded", color="red", marker="o", linestyle="--", linewidth=2)

# Plot Away Results - Bar chart for Goals Scored, Line chart for Goals Conceded
bars_away_for = ax2.bar(x - width/2, goals_for_away, width, label="Away Goals Scored", color="lightgreen", alpha=0.7)
ax2.plot(x, goals_against_away, label="Away Goals Conceded", color="salmon", marker="o", linestyle="--", linewidth=2)

# Add annotations for each bar in Home plot (goals scored)
for bar in bars_home_for:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each bar in Away plot (goals scored)
for bar in bars_away_for:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Home plot (goals conceded)
for i, point in enumerate(goals_against_home):
    ax1.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Away plot (goals conceded)
for i, point in enumerate(goals_against_away):
    ax2.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Customize Home plot (ax1)
ax1.set_title("Case 4: Home Games - Goals Scored (Bar) and Goals Conceded (Line)", fontsize=14)
ax1.set_xlabel("Teams", fontsize=12)
ax1.set_ylabel("Goals", fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(teams, rotation=90, fontsize=10)
ax1.legend(fontsize=10)
ax1.grid(axis="y", linestyle="--", alpha=0.7)

# Customize Away plot (ax2)
ax2.set_title("Case 4: Away Games - Goals Scored (Bar) and Goals Conceded (Line)", fontsize=14)
ax2.set_xlabel("Teams", fontsize=12)
ax2.set_ylabel("Goals", fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(teams, rotation=90, fontsize=10)
ax2.legend(fontsize=10)
ax2.grid(axis="y", linestyle="--", alpha=0.7)

# Add a main title for the entire figure
fig.suptitle("Goals Scored and Conceded in 5on4 Situations", fontsize=16, ha='center', va='center', y=1.02)

# Set y-axis limits to start at 40 for better view
ax1.set_ylim([0, max(goals_for_home.max(), goals_against_home.max(), goals_for_away.max(), goals_against_away.max()) + 10])
ax2.set_ylim([0, max(goals_for_home.max(), goals_against_home.max(), goals_for_away.max(), goals_against_away.max()) + 10])

# Adjust layout and save the plot
plt.tight_layout()
output_file = "case4_goals_home_away_bar_line_comparison_with_annotations.png"  # Output file name
plt.savefig(output_file, dpi=300, bbox_inches="tight")  # Save in the project directory

    ###### Visualisation CASE 5: Goals scored in 4on5 situations
# Data Preparation
teams = home_results5.index  # List of teams
goals_for_home = home_results5["TotalGoalsFor"]  # Home goals scored
goals_against_home = home_results5["TotalGoalsAgainst"]  # Home goals conceded
goals_for_away = away_results5["TotalGoalsFor"]  # Away goals scored
goals_against_away = away_results5["TotalGoalsAgainst"]  # Away goals conceded

# Numeric positions for teams
x = np.arange(len(teams))
width = 0.35  # Bar width

# Create the subplots (two plots side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot Home Results - Bar chart for Goals Scored, Line chart for Goals Conceded
bars_home_for = ax1.bar(x - width/2, goals_for_home, width, label="Home Goals Scored", color="green", alpha=0.7)
ax1.plot(x, goals_against_home, label="Home Goals Conceded", color="red", marker="o", linestyle="--", linewidth=2)

# Plot Away Results - Bar chart for Goals Scored, Line chart for Goals Conceded
bars_away_for = ax2.bar(x - width/2, goals_for_away, width, label="Away Goals Scored", color="lightgreen", alpha=0.7)
ax2.plot(x, goals_against_away, label="Away Goals Conceded", color="salmon", marker="o", linestyle="--", linewidth=2)

# Add annotations for each bar in Home plot (goals scored)
for bar in bars_home_for:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each bar in Away plot (goals scored)
for bar in bars_away_for:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Home plot (goals conceded)
for i, point in enumerate(goals_against_home):
    ax1.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Away plot (goals conceded)
for i, point in enumerate(goals_against_away):
    ax2.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Customize Home plot (ax1)
ax1.set_title("Case 5: Home Games - Goals Scored (Bar) and Goals Conceded (Line)", fontsize=14)
ax1.set_xlabel("Teams", fontsize=12)
ax1.set_ylabel("Goals", fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(teams, rotation=90, fontsize=10)
ax1.legend(fontsize=10)
ax1.grid(axis="y", linestyle="--", alpha=0.7)

# Customize Away plot (ax2)
ax2.set_title("Case 5: Away Games - Goals Scored (Bar) and Goals Conceded (Line)", fontsize=14)
ax2.set_xlabel("Teams", fontsize=12)
ax2.set_ylabel("Goals", fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(teams, rotation=90, fontsize=10)
ax2.legend(fontsize=10)
ax2.grid(axis="y", linestyle="--", alpha=0.7)

# Add a main title for the entire figure
fig.suptitle("Goals Scored and Conceded in 4on5 Situations", fontsize=16, ha='center', va='center', y=1.02)

# Set y-axis limits to start at 0 for better view
ax1.set_ylim([0, max(goals_for_home.max(), goals_against_home.max(), goals_for_away.max(), goals_against_away.max()) + 10])
ax2.set_ylim([0, max(goals_for_home.max(), goals_against_home.max(), goals_for_away.max(), goals_against_away.max()) + 10])

# Adjust layout and save the plot
plt.tight_layout()
output_file = "case5_goals_home_away_bar_line_comparison_with_annotations.png"  # Output file name
plt.savefig(output_file, dpi=300, bbox_inches="tight")  # Save in the project directory

    ###### Visualisation CASE 6: Goals scored in other situations
# Data Preparation
teams = home_results6.index  # List of teams
goals_for_home = home_results6["TotalGoalsFor"]  # Home goals scored
goals_against_home = home_results6["TotalGoalsAgainst"]  # Home goals conceded
goals_for_away = away_results6["TotalGoalsFor"]  # Away goals scored
goals_against_away = away_results6["TotalGoalsAgainst"]  # Away goals conceded

# Numeric positions for teams
x = np.arange(len(teams))
width = 0.35  # Bar width

# Create the subplots (two plots side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot Home Results - Bar chart for Goals Scored, Line chart for Goals Conceded
bars_home_for = ax1.bar(x - width/2, goals_for_home, width, label="Home Goals Scored", color="green", alpha=0.7)
ax1.plot(x, goals_against_home, label="Home Goals Conceded", color="red", marker="o", linestyle="--", linewidth=2)

# Plot Away Results - Bar chart for Goals Scored, Line chart for Goals Conceded
bars_away_for = ax2.bar(x - width/2, goals_for_away, width, label="Away Goals Scored", color="lightgreen", alpha=0.7)
ax2.plot(x, goals_against_away, label="Away Goals Conceded", color="salmon", marker="o", linestyle="--", linewidth=2)

# Add annotations for each bar in Home plot (goals scored)
for bar in bars_home_for:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each bar in Away plot (goals scored)
for bar in bars_away_for:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Home plot (goals conceded)
for i, point in enumerate(goals_against_home):
    ax1.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Away plot (goals conceded)
for i, point in enumerate(goals_against_away):
    ax2.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Customize Home plot (ax1)
ax1.set_title("Case 6: Home Games - Goals Scored (Bar) and Goals Conceded (Line)", fontsize=14)
ax1.set_xlabel("Teams", fontsize=12)
ax1.set_ylabel("Goals", fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(teams, rotation=90, fontsize=10)
ax1.legend(fontsize=10)
ax1.grid(axis="y", linestyle="--", alpha=0.7)

# Customize Away plot (ax2)
ax2.set_title("Case 6: Away Games - Goals Scored (Bar) and Goals Conceded (Line)", fontsize=14)
ax2.set_xlabel("Teams", fontsize=12)
ax2.set_ylabel("Goals", fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(teams, rotation=90, fontsize=10)
ax2.legend(fontsize=10)
ax2.grid(axis="y", linestyle="--", alpha=0.7)

# Add a main title for the entire figure
fig.suptitle("Goals Scored and Conceded in Other Situations", fontsize=16, ha='center', va='center', y=1.02)

# Set y-axis limits to start at 0 for better view
ax1.set_ylim([10, max(goals_for_home.max(), goals_against_home.max(), goals_for_away.max(), goals_against_away.max()) + 10])
ax2.set_ylim([10, max(goals_for_home.max(), goals_against_home.max(), goals_for_away.max(), goals_against_away.max()) + 10])

# Adjust layout and save the plot
plt.tight_layout()
output_file = "case6_goals_home_away_bar_line_comparison_with_annotations.png"  # Output file name
plt.savefig(output_file, dpi=300, bbox_inches="tight")  # Save in the project directory

    ###### Visualisation CASE 7: Shots on goals in total
###### Visualisation CASE 7: Shots on goals in total
# Data Preparation
teams = home_results7.index  # List of teams
shots_for_home = home_results7["TotalShotsFor"]  # Home shots on goals
shots_against_home = home_results7["TotalShotsAgainst"]  # Home shots conceded
shots_for_away = away_results7["TotalShotsFor"]  # Away shots on goals
shots_against_away = away_results7["TotalShotsAgainst"]  # Away shots conceded

# Numeric positions for teams
x = np.arange(len(teams))
width = 0.35  # Bar width

# Create the subplots (two plots side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot Home Results - Bar chart for Shots Scored, Line chart for Shots Conceded
bars_home_for = ax1.bar(x - width/2, shots_for_home, width, label="Home Shots on Goals", color="blue", alpha=0.7)
ax1.plot(x, shots_against_home, label="Home Shots Conceded", color="red", marker="o", linestyle="--", linewidth=2)

# Plot Away Results - Bar chart for Shots Scored, Line chart for Shots Conceded
bars_away_for = ax2.bar(x - width/2, shots_for_away, width, label="Away Shots on Goals", color="lightblue", alpha=0.7)
ax2.plot(x, shots_against_away, label="Away Shots Conceded", color="salmon", marker="o", linestyle="--", linewidth=2)

# Add annotations for each bar in Home plot (shots scored)
for bar in bars_home_for:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each bar in Away plot (shots scored)
for bar in bars_away_for:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Home plot (shots conceded)
for i, point in enumerate(shots_against_home):
    ax1.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Away plot (shots conceded)
for i, point in enumerate(shots_against_away):
    ax2.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Customize Home plot (ax1)
ax1.set_title("Case 7: Home Games - Shots on Goals (Bar) and Shots Conceded (Line)", fontsize=14)
ax1.set_xlabel("Teams", fontsize=12)
ax1.set_ylabel("Shots", fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(teams, rotation=90, fontsize=10)
ax1.legend(fontsize=10)
ax1.grid(axis="y", linestyle="--", alpha=0.7)

# Customize Away plot (ax2)
ax2.set_title("Case 7: Away Games - Shots on Goals (Bar) and Shots Conceded (Line)", fontsize=14)
ax2.set_xlabel("Teams", fontsize=12)
ax2.set_ylabel("Shots", fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(teams, rotation=90, fontsize=10)
ax2.legend(fontsize=10)
ax2.grid(axis="y", linestyle="--", alpha=0.7)

# Add a main title for the entire figure
fig.suptitle("Shots on Goals and Conceded in Total", fontsize=16, ha='center', va='center', y=1.02)

# Set y-axis limits to start at 0 for better view
ax1.set_ylim([2000, max(shots_for_home.max(), shots_against_home.max(), shots_for_away.max(), shots_against_away.max()) + 10])
ax2.set_ylim([2000, max(shots_for_home.max(), shots_against_home.max(), shots_for_away.max(), shots_against_away.max()) + 10])

# Adjust layout and save the plot
plt.tight_layout()
output_file = "case7_shots_home_away_bar_line_comparison_with_annotations.png"  # Output file name
plt.savefig(output_file, dpi=300, bbox_inches="tight")  # Save in the project directory

    ###### Visualisation CASE 8: Shots on goals in 5on5
# Data Preparation
teams = home_results8.index  # List of teams
shots_for_home = home_results8["TotalShotsFor"]  # Home shots on goals
shots_against_home = home_results8["TotalShotsAgainst"]  # Home shots conceded
shots_for_away = away_results8["TotalShotsFor"]  # Away shots on goals
shots_against_away = away_results8["TotalShotsAgainst"]  # Away shots conceded

# Numeric positions for teams
x = np.arange(len(teams))
width = 0.35  # Bar width

# Create the subplots (two plots side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot Home Results - Bar chart for Shots Scored, Line chart for Shots Conceded
bars_home_for = ax1.bar(x - width/2, shots_for_home, width, label="Home Shots on Goals", color="blue", alpha=0.7)
ax1.plot(x, shots_against_home, label="Home Shots Conceded", color="red", marker="o", linestyle="--", linewidth=2)

# Plot Away Results - Bar chart for Shots Scored, Line chart for Shots Conceded
bars_away_for = ax2.bar(x - width/2, shots_for_away, width, label="Away Shots on Goals", color="lightblue", alpha=0.7)
ax2.plot(x, shots_against_away, label="Away Shots Conceded", color="salmon", marker="o", linestyle="--", linewidth=2)

# Add annotations for each bar in Home plot (shots scored)
for bar in bars_home_for:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each bar in Away plot (shots scored)
for bar in bars_away_for:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Home plot (shots conceded)
for i, point in enumerate(shots_against_home):
    ax1.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Away plot (shots conceded)
for i, point in enumerate(shots_against_away):
    ax2.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Customize Home plot (ax1)
ax1.set_title("Case 8: Home Games - Shots on Goals (Bar) and Shots Conceded (Line)", fontsize=14)
ax1.set_xlabel("Teams", fontsize=12)
ax1.set_ylabel("Shots", fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(teams, rotation=90, fontsize=10)
ax1.legend(fontsize=10)
ax1.grid(axis="y", linestyle="--", alpha=0.7)

# Customize Away plot (ax2)
ax2.set_title("Case 8: Away Games - Shots on Goals (Bar) and Shots Conceded (Line)", fontsize=14)
ax2.set_xlabel("Teams", fontsize=12)
ax2.set_ylabel("Shots", fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(teams, rotation=90, fontsize=10)
ax2.legend(fontsize=10)
ax2.grid(axis="y", linestyle="--", alpha=0.7)

# Add a main title for the entire figure
fig.suptitle("Shots on Goals and Conceded in 5on5 Situations", fontsize=16, ha='center', va='center', y=1.02)

# Set y-axis limits to start at 0 for better view
ax1.set_ylim([1500, max(shots_for_home.max(), shots_against_home.max(), shots_for_away.max(), shots_against_away.max()) + 10])
ax2.set_ylim([1500, max(shots_for_home.max(), shots_against_home.max(), shots_for_away.max(), shots_against_away.max()) + 10])

# Adjust layout and save the plot
plt.tight_layout()
output_file = "case8_shots_home_away_bar_line_comparison_with_annotations.png"  # Output file name
plt.savefig(output_file, dpi=300, bbox_inches="tight")  # Save in the project directory

    ###### Visualisation CASE 9: Shots on goals in 5on4
# Data Preparation
teams = home_results9.index  # List of teams
shots_for_home = home_results9["TotalShotsFor"]  # Home shots on goals
shots_against_home = home_results9["TotalShotsAgainst"]  # Home shots conceded
shots_for_away = away_results9["TotalShotsFor"]  # Away shots on goals
shots_against_away = away_results9["TotalShotsAgainst"]  # Away shots conceded

# Numeric positions for teams
x = np.arange(len(teams))
width = 0.35  # Bar width

# Create the subplots (two plots side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot Home Results - Bar chart for Shots Scored, Line chart for Shots Conceded
bars_home_for = ax1.bar(x - width/2, shots_for_home, width, label="Home Shots on Goals", color="blue", alpha=0.7)
ax1.plot(x, shots_against_home, label="Home Shots Conceded", color="red", marker="o", linestyle="--", linewidth=2)

# Plot Away Results - Bar chart for Shots Scored, Line chart for Shots Conceded
bars_away_for = ax2.bar(x - width/2, shots_for_away, width, label="Away Shots on Goals", color="lightblue", alpha=0.7)
ax2.plot(x, shots_against_away, label="Away Shots Conceded", color="salmon", marker="o", linestyle="--", linewidth=2)

# Add annotations for each bar in Home plot (shots scored)
for bar in bars_home_for:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each bar in Away plot (shots scored)
for bar in bars_away_for:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Home plot (shots conceded)
for i, point in enumerate(shots_against_home):
    ax1.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Away plot (shots conceded)
for i, point in enumerate(shots_against_away):
    ax2.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Customize Home plot (ax1)
ax1.set_title("Case 9: Home Games - Shots on Goals (Bar) and Shots Conceded (Line)", fontsize=14)
ax1.set_xlabel("Teams", fontsize=12)
ax1.set_ylabel("Shots", fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(teams, rotation=90, fontsize=10)
ax1.legend(fontsize=10)
ax1.grid(axis="y", linestyle="--", alpha=0.7)

# Customize Away plot (ax2)
ax2.set_title("Case 9: Away Games - Shots on Goals (Bar) and Shots Conceded (Line)", fontsize=14)
ax2.set_xlabel("Teams", fontsize=12)
ax2.set_ylabel("Shots", fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(teams, rotation=90, fontsize=10)
ax2.legend(fontsize=10)
ax2.grid(axis="y", linestyle="--", alpha=0.7)

# Add a main title for the entire figure
fig.suptitle("Shots on Goals and Conceded in 5on4 Situations", fontsize=16, ha='center', va='center', y=1.02)

# Set y-axis limits to start at 0 for better view
ax1.set_ylim([0, max(shots_for_home.max(), shots_against_home.max(), shots_for_away.max(), shots_against_away.max()) + 10])
ax2.set_ylim([0, max(shots_for_home.max(), shots_against_home.max(), shots_for_away.max(), shots_against_away.max()) + 10])

# Adjust layout and save the plot
plt.tight_layout()
output_file = "case9_shots_home_away_bar_line_comparison_with_annotations.png"  # Output file name
plt.savefig(output_file, dpi=300, bbox_inches="tight")  # Save in the project directory

    ###### Visualisation CASE 10: Shots on goals in 4on5 situations
# Data Preparation
teams = home_results10.index  # List of teams
shots_for_home = home_results10["TotalShotsFor"]  # Home shots on goals
shots_against_home = home_results10["TotalShotsAgainst"]  # Home shots conceded
shots_for_away = away_results10["TotalShotsFor"]  # Away shots on goals
shots_against_away = away_results10["TotalShotsAgainst"]  # Away shots conceded

# Numeric positions for teams
x = np.arange(len(teams))
width = 0.35  # Bar width

# Create the subplots (two plots side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot Home Results - Bar chart for Shots Scored, Line chart for Shots Conceded
bars_home_for = ax1.bar(x - width/2, shots_for_home, width, label="Home Shots on Goals", color="blue", alpha=0.7)
ax1.plot(x, shots_against_home, label="Home Shots Conceded", color="red", marker="o", linestyle="--", linewidth=2)

# Plot Away Results - Bar chart for Shots Scored, Line chart for Shots Conceded
bars_away_for = ax2.bar(x - width/2, shots_for_away, width, label="Away Shots on Goals", color="lightblue", alpha=0.7)
ax2.plot(x, shots_against_away, label="Away Shots Conceded", color="salmon", marker="o", linestyle="--", linewidth=2)

# Add annotations for each bar in Home plot (shots scored)
for bar in bars_home_for:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each bar in Away plot (shots scored)
for bar in bars_away_for:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Home plot (shots conceded)
for i, point in enumerate(shots_against_home):
    ax1.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Away plot (shots conceded)
for i, point in enumerate(shots_against_away):
    ax2.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Customize Home plot (ax1)
ax1.set_title("Case 10: Home Games - Shots on Goals (Bar) and Shots Conceded (Line)", fontsize=14)
ax1.set_xlabel("Teams", fontsize=12)
ax1.set_ylabel("Shots", fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(teams, rotation=90, fontsize=10)
ax1.legend(fontsize=10)
ax1.grid(axis="y", linestyle="--", alpha=0.7)

# Customize Away plot (ax2)
ax2.set_title("Case 10: Away Games - Shots on Goals (Bar) and Shots Conceded (Line)", fontsize=14)
ax2.set_xlabel("Teams", fontsize=12)
ax2.set_ylabel("Shots", fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(teams, rotation=90, fontsize=10)
ax2.legend(fontsize=10)
ax2.grid(axis="y", linestyle="--", alpha=0.7)

# Add a main title for the entire figure
fig.suptitle("Shots on Goals and Conceded in 4on5 Situations", fontsize=16, ha='center', va='center', y=1.02)

# Set y-axis limits to start at 0 for better view
ax1.set_ylim([0, max(shots_for_home.max(), shots_against_home.max(), shots_for_away.max(), shots_against_away.max()) + 10])
ax2.set_ylim([0, max(shots_for_home.max(), shots_against_home.max(), shots_for_away.max(), shots_against_away.max()) + 10])

# Adjust layout and save the plot
plt.tight_layout()
output_file = "case10_shots_home_away_bar_line_comparison_with_annotations.png"  # Output file name
plt.savefig(output_file, dpi=300, bbox_inches="tight")  # Save in the project directory

    ###### Visualisation CASE 11: Shots on goals in other situations
# Data Preparation
teams = home_results11.index  # List of teams
shots_for_home = home_results11["TotalShotsFor"]  # Home shots on goals
shots_against_home = home_results11["TotalShotsAgainst"]  # Home shots conceded
shots_for_away = away_results11["TotalShotsFor"]  # Away shots on goals
shots_against_away = away_results11["TotalShotsAgainst"]  # Away shots conceded

# Numeric positions for teams
x = np.arange(len(teams))
width = 0.35  # Bar width

# Create the subplots (two plots side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot Home Results - Bar chart for Shots Scored, Line chart for Shots Conceded
bars_home_for = ax1.bar(x - width/2, shots_for_home, width, label="Home Shots on Goals", color="blue", alpha=0.7)
ax1.plot(x, shots_against_home, label="Home Shots Conceded", color="red", marker="o", linestyle="--", linewidth=2)

# Plot Away Results - Bar chart for Shots Scored, Line chart for Shots Conceded
bars_away_for = ax2.bar(x - width/2, shots_for_away, width, label="Away Shots on Goals", color="lightblue", alpha=0.7)
ax2.plot(x, shots_against_away, label="Away Shots Conceded", color="salmon", marker="o", linestyle="--", linewidth=2)

# Add annotations for each bar in Home plot (shots scored)
for bar in bars_home_for:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each bar in Away plot (shots scored)
for bar in bars_away_for:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Home plot (shots conceded)
for i, point in enumerate(shots_against_home):
    ax1.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Add annotations for each line in Away plot (shots conceded)
for i, point in enumerate(shots_against_away):
    ax2.text(x[i], point, f'{int(point)}', ha='center', va='bottom', fontsize=10, color='black')

# Customize Home plot (ax1)
ax1.set_title("Case 11: Home Games - Shots on Goals (Bar) and Shots Conceded (Line)", fontsize=14)
ax1.set_xlabel("Teams", fontsize=12)
ax1.set_ylabel("Shots", fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(teams, rotation=90, fontsize=10)
ax1.legend(fontsize=10)
ax1.grid(axis="y", linestyle="--", alpha=0.7)

# Customize Away plot (ax2)
ax2.set_title("Case 11: Away Games - Shots on Goals (Bar) and Shots Conceded (Line)", fontsize=14)
ax2.set_xlabel("Teams", fontsize=12)
ax2.set_ylabel("Shots", fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(teams, rotation=90, fontsize=10)
ax2.legend(fontsize=10)
ax2.grid(axis="y", linestyle="--", alpha=0.7)

# Add a main title for the entire figure
fig.suptitle("Shots on Goals and Conceded in Other Situations", fontsize=16, ha='center', va='center', y=1.02)

# Set y-axis limits to start at 0 for better view
ax1.set_ylim([50, max(shots_for_home.max(), shots_against_home.max(), shots_for_away.max(), shots_against_away.max()) + 10])
ax2.set_ylim([50, max(shots_for_home.max(), shots_against_home.max(), shots_for_away.max(), shots_against_away.max()) + 10])

# Adjust layout and save the plot
plt.tight_layout()
output_file = "case11_Shots_on_goals_in_other_situations_with_annotations.png"  # Output file name
plt.savefig(output_file, dpi=300, bbox_inches="tight")  # Save in the project directory