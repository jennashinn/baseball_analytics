# Predicting MLB Player Value with Machine Learning

**This is a work in progress and will be updated often**

## Goal
Major League Baseball is the only American professional sports league without a roster salary cap. For teams big market teams like New York Yankees, New York Mets, Los Angeles Dodgers, and Boston Red Sox, this isn't much of a problem. However, for most teams, a limited budget makes building a competitive team difficult. facing a limited budget is a predicament many MLB teams face. 

Inspired by Moneyball, the goal of this project it to construct a machine learning model that can predict the salaries of MLB hitters and pitchers using historical baseball data collected since the 2000 season. Additionally, we want to better understand which statistics in baseball contribute the most to winning. 

Using these models, we can better understand the **value** of a player and identify those players are potentially undervalued or overvalued.

Furthermore, the models can be used to find any player's value at any point in time. For example, we can see how much Babe Ruth, Willie Mays, and Ted Williams would make today's market.


## Data
The data was sourced with [PyBaseball]("https://github.com/jldbc/pybaseball) which allows users to scrape Baseball Reference, Baseball Savant, and FanGraphs data.

FanGraphs provides a full [glossary](https://library.fangraphs.com/offense/offensive-statistics-list/) of the offensive terms used in the batting data.
