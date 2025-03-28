# %%
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "name": ["John", "Anna", "Peter", "Linda"],
    "location": ["New York", "Paris", "Berlin", "London"],
    "age": [24, 13, 53, 33],
}
df = pd.DataFrame(data)

# %%
df.plot(kind="bar", x="name", y="age")

# %%
