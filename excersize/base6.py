class GameScore:

    champion_name = ""
    high_score = 0

    def __init__(self, player_name, current_score=0):
        self.player_name = player_name
        self.current_score = current_score

    def __call__(self, points):
        # スコア加算機能
        self.current_score = points
        # ハイスコア更新機能
        if GameScore.high_score < self.current_score:
            GameScore.champion_name = self.player_name
            GameScore.high_score = self.current_score
            print(f"新記録！{self.player_name}: {self.high_score}点")
        return self.current_score

    @classmethod
    def get_champion(cls):
        if cls.champion_name:
            return f"{cls.champion_name} ({cls.high_score}点)"
        else:
            return "まだ記録がありません"

    def reset(self):
        self.current_score = 0


player1 = GameScore("Alice")
player2 = GameScore("Bob")

print(player1(150))
print(player2(200))
print(player1(100))
print(player1.current_score)

print(GameScore.get_champion())
player2.reset()
print(player2.current_score)
print(GameScore.get_champion())

player3 = GameScore("Charlie")
player3(300)
print(GameScore.get_champion())
