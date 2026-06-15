import argparse

from aidatascientist import DataAgent


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--file",
        required=True
    )

    parser.add_argument(
        "--target",
        required=False
    )

    args = parser.parse_args()

    agent = DataAgent()

    agent.load(args.file)

    agent.clean()

    stats = agent.analyze()

    print(stats)

    if args.target:

        result = agent.train_model(
            args.target
        )

        print(result)


if __name__ == "__main__":
    main()