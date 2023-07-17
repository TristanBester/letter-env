from gymnasium import make, register

from letterenv import LetterEnv

if __name__ == "__main__":
    register(
        id="LetterEnv-v0",
        entry_point="letterenv:LetterEnv",
        max_episode_steps=1,
    )

    env = make("LetterEnv-v0")

    # print(env.observation_space)
    # print(env.spec)

    o, _ = env.reset()

    for i in range(100):
        print(env.render())
        a = int(input("Action: "))
        print(env.step(a))
