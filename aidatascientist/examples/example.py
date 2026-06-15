from aidatascientist import DataAgent

agent = DataAgent()

agent.load(
    "sales.csv"
)

agent.clean()

stats = agent.analyze()

print(stats)

charts = agent.visualize()

print(charts)

result = agent.train_model(
    target="price"
)

print(result)

report = agent.save_report()

print(report)