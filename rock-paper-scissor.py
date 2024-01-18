class Participant:
    def __init__(self, name):
        self.name = name
        self.choice = ""
        self.points = 0

    def choose(self):
        self.choice = input(
            "{name}, select rock, paper, scissor, lizard or Spock: ".format(
                name=self.name
            )
        )
        print("{name} selects {choice}".format(name=self.name, choice=self.choice))

    def toNumericalChoice(self):
        switcher = {"rock": 0, "paper": 1, "scissor": 2, "lizard": 3, "spock": 4}
        return switcher.get(self.choice, "nothing")

    def incrementPoint(self):
        self.points += 1


class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0],
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()

        print(
            "Round resulted in a {result}".format(result=self.getResultAsString(result))
        )

    def compareChoices(self, p1, p2):
        print("比较选择")
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def getResultAsString(self, result):
        res = {0: "draw", 1: "win", -1: "loss"}
        return res[result]

    def awardPoints(self):
        print("奖励分数")


class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("邦")
        self.secondParticipant = Participant("小明")

    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        print("检查结束条件")

    def determineWinner(self):
        answer = input("是否继续游戏？y/n:")
        if answer == "y":
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print(
                "游戏结束, {name} 获得了 {points} 分".format(
                    name=self.participant.name, points=self.participant.points
                )
            )
            self.determineWinner()
            self.endGame = True


game = Game()

game.start()
