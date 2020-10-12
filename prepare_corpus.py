import pandas as pd

articles = pd.read_csv("./data/articles.csv")

articles.drop(["title", "date", "category", "subcategory", "link"], axis=1, inplace=True)

articles_30k = articles[:30000]

print(articles_30k)

articles_30k.to_csv(r'./data/corpus.txt', header=None, index=None)
