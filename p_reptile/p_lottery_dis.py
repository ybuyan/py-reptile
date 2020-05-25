import pandas as pd

df = pd.read_csv("data.csv", header=None)
# 提取红球号码
red_ball = df.loc[:, 1:6]
# 红球出现次数
red_counts = pd.value_counts(red_ball.values.flatten())
# 蓝球
blue_ball = df.loc[:, [7]]
blue_counts = pd.value_counts(blue_ball.values.flatten())

# 可视化
import matplotlib.pyplot as plot

plot.pip(red_counts, lables=red_counts.index, radius=1, wedgeprops={"width": 0.3})
plot.pip(blue_counts, lables=blue_counts.index, radius=0.5, wedgeprops={"width": 0.3})

plot.show()
