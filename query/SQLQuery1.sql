-- Step 1: Remove unnecessary columns from teams 
ALTER TABLE all_teams DROP COLUMN name, position;

 -- Step 2: Data Selection
 -- The data pertains exclusively to the 2023/2024 regular season.

 -- CASE 1: Home and away games - wins and losses
SELECT playerTeam, home_or_away, 
	(CASE 
	WHEN goalsFor > goalsAgainst THEN 'win'
	WHEN goalsFor < goalsAgainst THEN 'lose'
	WHEN goalsFor = goalsAgainst THEN 'draw'
	END) AS result
FROM all_teams
WHERE season = '2023' AND
	situation = 'all'
ORDER BY playerTeam

-- CASE 2: Home and away games - goals scored and goals conceded
SELECT playerTeam, home_or_away, SUM(CAST(goalsFor AS FLOAT)) AS TotalGoalsFor, SUM(CAST(goalsAgainst AS FLOAT)) AS TotalGoalsAgainst
FROM all_teams
WHERE season = '2023' AND
	situation = 'all'
GROUP BY playerTeam, home_or_away

-- CASE 3: Goals scored in 5on5 situations
SELECT playerTeam, home_or_away, SUM(CAST(goalsFor AS FLOAT)) AS TotalGoalsFor, SUM(CAST(goalsAgainst AS FLOAT)) AS TotalGoalsAgainst
FROM all_teams
WHERE season = '2023' AND
	situation = '5on5'
GROUP BY playerTeam, home_or_away

-- CASE 4: Goals scored in 5on4 situations
SELECT playerTeam, home_or_away, SUM(CAST(goalsFor AS FLOAT)) AS TotalGoalsFor, SUM(CAST(goalsAgainst AS FLOAT)) AS TotalGoalsAgainst
FROM all_teams
WHERE season = '2023' AND
	situation = '5on4'
GROUP BY playerTeam, home_or_away

-- CASE 5: Goals scored in 4on5 situations
SELECT playerTeam, home_or_away, SUM(CAST(goalsFor AS FLOAT)) AS TotalGoalsFor, SUM(CAST(goalsAgainst AS FLOAT)) AS TotalGoalsAgainst
FROM all_teams
WHERE season = '2023' AND
	situation = '4on5'
GROUP BY playerTeam, home_or_away

-- CASE 6: Goals scored in other situations
SELECT playerTeam, home_or_away, SUM(CAST(goalsFor AS FLOAT)) AS TotalGoalsFor, SUM(CAST(goalsAgainst AS FLOAT)) AS TotalGoalsAgainst
FROM all_teams
WHERE season = '2023' AND
	situation = 'other'
GROUP BY playerTeam, home_or_away

-- CASE 7: Shots on goals in total
SELECT playerTeam, home_or_away, SUM(CAST(shotAttemptsFOR AS FLOAT)) AS TotalShotsFor, SUM(CAST(shotAttemptsAgainst AS FLOAT)) AS TotalShotsAgainst
FROM all_teams
WHERE season = '2023' AND
	situation = 'all'
GROUP BY playerTeam, home_or_away

-- CASE 8: Shots on goals in 5on5
SELECT playerTeam, home_or_away, SUM(CAST(shotAttemptsFOR AS FLOAT)) AS TotalShotsFor, SUM(CAST(shotAttemptsAgainst AS FLOAT)) AS TotalShotsAgainst
FROM all_teams
WHERE season = '2023' AND
	situation = '5on5'
GROUP BY playerTeam, home_or_away

-- CASE 9: Shots on goals in 5on4
SELECT playerTeam, home_or_away, SUM(CAST(shotAttemptsFOR AS FLOAT)) AS TotalShotsFor, SUM(CAST(shotAttemptsAgainst AS FLOAT)) AS TotalShotsAgainst
FROM all_teams
WHERE season = '2023' AND
	situation = '5on4'
GROUP BY playerTeam, home_or_away

-- CASE 10: Shots on goals in 4on5
SELECT playerTeam, home_or_away, SUM(CAST(shotAttemptsFOR AS FLOAT)) AS TotalShotsFor, SUM(CAST(shotAttemptsAgainst AS FLOAT)) AS TotalShotsAgainst
FROM all_teams
WHERE season = '2023' AND
	situation = '4on5'
GROUP BY playerTeam, home_or_away

-- CASE 11: Shots on goals in other situations
SELECT playerTeam, home_or_away, SUM(CAST(shotAttemptsFOR AS FLOAT)) AS TotalShotsFor, SUM(CAST(shotAttemptsAgainst AS FLOAT)) AS TotalShotsAgainst
FROM all_teams
WHERE season = '2023' AND
	situation = 'other'
GROUP BY playerTeam, home_or_away