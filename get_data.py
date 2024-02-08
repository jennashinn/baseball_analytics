
## Getting data 

import pandas as pd
pd.set_option('display.max_columns', None)
import feather

## BATTING STATS
from pybaseball import batting_stats
# Retrieve data on only players who have 100+ plate appearances between 2000 and 2023
batting = batting_stats(2000, 2023, qual=100)
# Save as feather (more effecient than csv)
feather.write_dataframe(batting, 'data/batting.feather')

## BWAR STATS
from pybaseball import bwar_bat
# get war stats from baseball reference 
bwar_batting = bwar_bat()
# Filter bwar_bat from 2000 on with a minimum of 100 plate appearances
bwar_batting_df = bwar_batting[(bwar_batting['year_ID'].between(2000,2023)) & (bwar_batting['PA'] >= 100)]
feather.write_dataframe(bwar_batting_df, 'data/bwar_bat.feather')

## PITCHING STATS
from pybaseball import pitching_stats
# Retrieve data on only players who have pitched 30+ innings since 2000
pitching = pitching_stats(2000, 2023, qual=30)
feather.write_dataframe(pitching, 'data/pitching.feather')

## BWAR PITCHING STATS
from pybaseball import bwar_pitch
# Get WAR stats from baseball reference 
bwar_pitching = bwar_pitch(return_all = True)
# Filter bwar_pitch to 2000 to current
bwar_pitch_df = bwar_pitching[(bwar_pitching['year_ID'] >= 2000)]
feather.write_dataframe(bwar_pitch_df, 'data/bwar_pitch.feather')

## FIELDING
from pybaseball.lahman import *
fielding_df = fielding()
# Filter to 2000 and later
fielding_df = fielding_df[fielding_df['yearID'] >= 2000]
feather.write_dataframe(fielding_df, 'data/positions.feather')

## TEAMS
# Data on teams by season: record, division, stadium, attendance, etc
teams = teams_core()
# Filter to 1900 and later
teams = teams[teams['yearID'] >= 1900]
teams_df = teams[['yearID', 'name', 'franchID', 'attendance', 'W', 'L']]
teams_df = teams_df.dropna()
feather.write_dataframe(teams_df, 'data/teams.feather')
