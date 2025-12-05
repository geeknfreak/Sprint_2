class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses


class Football(Results):

    def number_of_wins(self):
        print('Футбольных побед:', self.victories)
        
    def number_of_draws(self):
         print('Футбольных ничьих:', self.draws)

    def number_of_losses(self):
         print('Футбольных поражений:', self.losses)

    def total_points(self):
        print('Общее количество очков:', 3 * self.victories + self.draws)

class Hockey(Results):
     
     def number_of_wins(self):
          print('Хоккейных побед:', self.victories)

     def number_of_draws(self):
          print('Хоккейных ничьих:', self.draws)

     def number_of_losses(self):
          print('Хоккейных поражений:', self.losses)

     def total_points(self):
        print('Общее количество очков:', 2 * self.victories + self.draws)

     
football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)
teams = [football_team, hockey_team]

for team in teams:
    if isinstance(team, Football):
        print("\n=== Футбольная команда ===")
    else:
        print("\n=== Хоккейная команда ===")

    team.number_of_wins()
    team.number_of_draws()
    team.number_of_losses()
    team.total_points()