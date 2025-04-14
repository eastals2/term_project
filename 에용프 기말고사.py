class BowlingGame:
    def __init__(self):
        self.frames = []

    def add_frame(self, first_roll, second_roll, bonus_roll=None):
        # 10프레임은 보너스 포함될 수 있음
        self.frames.append((first_roll, second_roll, bonus_roll))

    def calculate_score(self):
        total_score = 0
        for i in range(10):  # 10프레임까지만 계산
            frame = self.frames[i]
            first, second = frame[0], frame[1]
            bonus = frame[2] if len(frame) > 2 else None
            total_score += first + second

            # 스트라이크
            if first == 10:
                total_score += self._strike_bonus(i)
            # 스페어
            elif first + second == 10:
                total_score += self._spare_bonus(i)

            # 10프레임 보너스
            if i == 9 and bonus is not None:
                total_score += bonus

        return total_score

    def _strike_bonus(self, i):
        if i + 1 >= len(self.frames):
            return 0
        next_frame = self.frames[i + 1]
        first = next_frame[0]
        second = next_frame[1]

        # 다음 프레임이 스트라이크이고 그 다음 프레임도 있으면
        if first == 10 and i + 2 < len(self.frames):
            return 10 + self.frames[i + 2][0]
        return first + second

    def _spare_bonus(self, i):
        if i + 1 >= len(self.frames):
            return 0
        return self.frames[i + 1][0]

    def calculate_average(self, total_score, games_played):
        return total_score / games_played if games_played else 0


def main():
    games_played = int(input("몇 게임을 플레이했나요? "))
    total_score = 0

    for game_number in range(games_played):
        game = BowlingGame()
        print(f"\n🎳 게임 {game_number + 1} 점수 입력:")

        # 1~9프레임
        for i in range(9):
            print(f"\nFrame {i + 1}")
            first = int(input("첫 번째 투구: "))
            if first == 10:
                second = 0  # 스트라이크면 두 번째는 0
            else:
                second = int(input("두 번째 투구: "))
            game.add_frame(first, second)

        # 10프레임
        print("\nFrame 10")
        first = int(input("첫 번째 투구: "))
        second = int(input("두 번째 투구: "))
        bonus = None

        if first == 10 or first + second == 10:
            bonus = int(input("보너스 투구: "))

        game.add_frame(first, second, bonus)

        score = game.calculate_score()
        total_score += score
        print(f"게임 {game_number + 1} 총 점수: {score}")

    average = game.calculate_average(total_score, games_played)
    print(f"\n총 점수: {total_score}")
    print(f"평균 점수: {average:.2f}")


if __name__ == "__main__":
    main()
