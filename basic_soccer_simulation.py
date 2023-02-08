import random

class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Player:
    def __init__(self, name, team, position, skill):
        self.name = name
        self.team = team
        self.position = position    # position one of ["defender", "attacker", "midfielder", "keeper"]
        self.skill = skill          # skill int between 1 and 99

def simulate_play(home_team, away_team):
    home_skill = sum([p.skill for p in home_team.players])
    away_skill = sum([p.skill for p in away_team.players])
    skill_difference = home_skill - away_skill
    if random.uniform(0, 1) < 0.5 + 0.01 * skill_difference:
        home_team.score += 1
    else:
        away_team.score += 1

def simulate_game(home_team, away_team):
    for i in range(90):
        simulate_play(home_team, away_team)

home_team = Team("Home Team")
home_team.players = [Player("Player 1", home_team, "defender", 100),
                     Player("Player 2", home_team, "attacker", 90),
                     Player("Player 3", home_team, "keeper", 80)]

away_team = Team("Away Team")
away_team.players = [Player("Player 4", away_team, "defender", 100),
                     Player("Player 5", away_team, "attacker", 80),
                     Player("Player 6", away_team, "keeper", 50)]

simulate_game(home_team, away_team)
print("Final Score: home-", home_team.score, ", away-", away_team.score)