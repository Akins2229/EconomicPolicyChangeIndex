"""
M. Akins 2021


Economic Policy Change Index


M.I.T License
"""

import typing
import statistics
import os
import json

class Country:
  def __init__(
    self,
    budget: int,
    population: int,
    gdp: float,
    name: str,
    description: str,
    flag: str # filepath to assets flag (may use .assets.constants.Flags class)
  ) -> None:
    self.STARTING_BUDGET = budget
    self.money_spent = 0 # money spent by a country in the last year
    self.budget = budget - self.money_spent
    self.population = population
    self.gdp = gdp
    self.name = name
    self.description = description
    self.flag=flag

    

class Game:
  def __init__(
    self,
    countries: typing.List[Country]
  ) -> None:
    gdps = []
    budgets = []
    for country in countries:
      gdps.append(country.gdp)
      budgets.append(country.budget)
    self.AVERAGE_GDP = statistics.fmean(gdps)
    self.GLOBAL_BUDGET = statistics.mean(budgets)
    self.money_spent = 0 # rate of how much money has been spent this year globally
    self.available_budget = self.GLOBAL_BUDGET - self.money_spent

class GameState(Game):
  def __init__(
    self,
    **kwargs
  ):
    super().__init__(**kwargs)
    
