
class GuessingAgent:

    def __init__(self, low=1, high=100):
        self.low = low
        self.high = high
        self.guesses = 0

    def make_guess(self):
        self.guesses += 1
        return (self.low + self.high) // 2

    def update(self, guess, feedback):
        if feedback == 'higher':
            self.low = guess + 1

        elif feedback == 'lower':
            self.high = guess - 1


def environment(secret):

    def feedback(guess):
        if guess == secret:
            return 'correct'

        return 'higher' if secret > guess else 'lower'

    return feedback


def play(secret, low=1, high=100, verbose=True):
    agent = GuessingAgent(low, high)
    env = environment(secret)

    while True:
        guess = agent.make_guess()
        fb = env(guess)

        if verbose:
            print(f'Guess {agent.guesses}: {guess:>3} -> {fb:<7} (range was {agent.low}-{agent.high})')

        if fb == 'correct':
            return agent.guesses

        agent.update(guess, fb)


def interactive(low=1, high=100):
    agent = GuessingAgent(low, high)

    while agent.low <= agent.high:
        g = agent.make_guess()
        ans = input(f'Is it {g}? (h/l/c): ').strip().lower()

        if ans == 'c':
            print(f'Guessed in {agent.guesses} tries!')
            return

        agent.update(g, 'higher' if ans == 'h' else 'lower')

    print('Your answers were inconsistent.')


if __name__ == '__main__':
    print('Secret number = 73')
    n = play(73)
    print('Solved in', n, 'guesses\n')

    worst = max(play(s, verbose=False) for s in range(1, 101))
    avg = sum(play(s, verbose=False) for s in range(1, 101)) / 100

    print('Worst case over 1..100:', worst, '| Average:', avg)
