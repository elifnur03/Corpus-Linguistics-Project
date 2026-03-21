import os
import pandas as pd
import random

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'dataset.csv')


academic = [
    "This study examines syntactic variation in English.",
    "The findings suggest a correlation between variables.",
    "Corpus analysis reveals significant patterns.",
    "This paper investigates discourse structures.",
    "The methodology is based on linguistic theory."
]

spoken = [
    "I mean like what are you doing",
    "You know it's kinda weird",
    "I was just thinking about that",
    "Well I don't really know",
    "It's like super confusing"
]

news = [
    "The government announced new policies today.",
    "The economy is showing signs of recovery.",
    "Scientists discovered a new species.",
    "The president held a press conference.",
    "Global markets reacted to the news."
]

social = [
    "OMG this is amazing!!!",
    "I can't believe this 😂",
    "This is literally the best thing ever",
    "So happy right now!!!",
    "This is so bad ugh"
]

categories = {
    "academic": academic,
    "spoken": spoken,
    "news": news,
    "social": social
}

rows = []

for _ in range(500):
    label = random.choice(list(categories.keys()))
    text = random.choice(categories[label])

    modifier = random.choice([
        "", " really", " very", " quite", " extremely", " honestly",
        " actually", " basically", " seriously"
    ])

    rows.append((text + modifier, label))

df = pd.DataFrame(rows, columns=["text", "label"])
df.to_csv(OUTPUT_PATH, index=False)

print("Linguistic dataset created.")