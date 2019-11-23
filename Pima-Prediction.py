import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def pd_print(pd_data):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'expand_frame_repr', True,
                           'display.width', '256'):
        print(pd_data)

df = pd.read_csv("./Notebooks/data/pima-data.csv")
print(df.shape)
pd_print(df.head(5))
pd_print(df.tail(5))

def plot_corr(df, size=11):
    """
    Function plots a graphical correlation matrix for each pair of columns in the dataframe.

    :param df: pandas dataframe
    :param size:  vertical and horizontal size of the plot
    :return: n/a
    :display: matrix of correlation between columns.  Blue-cyan-yellow-red-darkred => less to more correlated
                                                        0 ----------------> 1
    """

    corr: object = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)


#del df['skin']
#plot_corr(df)