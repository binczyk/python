import matplotlib.pyplot as plt
import numpy as np


class Graph:
    algorithmCompersion = []
    algorithmTime = []
    algorithmName = []

    def __init__(self, algorithmTime, algorithmCompersion):
        self.algorithmCompersion.append(algorithmCompersion['Force'] // 100)
        self.algorithmCompersion.append(algorithmCompersion['SundayCustom'])
        self.algorithmCompersion.append(algorithmCompersion['Sunday2charCustom'])
        self.algorithmCompersion.append(algorithmCompersion['SundayOriginal'])
        self.algorithmCompersion.append(algorithmCompersion['Sunday2charOriginal'])

        self.algorithmTime.append(float(algorithmTime['Force']) * 10000)
        self.algorithmTime.append(float(algorithmTime['SundayCustom']) * 100000)
        self.algorithmTime.append(float(algorithmTime['Sunday2charCustom']) * 100000)
        self.algorithmTime.append(float(algorithmTime['SundayOriginal']) * 100000)
        self.algorithmTime.append(float(algorithmTime['Sunday2charOriginal']) * 100000)

        self.algorithmName.append('Force')
        self.algorithmName.append('SundayCustom')
        self.algorithmName.append('Sunday2charCustom')
        self.algorithmName.append('SundayOriginal')
        self.algorithmName.append('Sunday2charOriginal')

    def draw(self):
        fig, ax = plt.subplots()

        index = np.arange(len(self.algorithmCompersion))
        bar_width = 0.35

        opacity = 0.4
        error_config = {'ecolor': '0.3'}

        rects1 = ax.bar(index, self.algorithmCompersion, bar_width,
                        alpha=opacity, color='b', error_kw=error_config,
                        label='Ilość porównań')

        rects2 = ax.bar(index + bar_width, self.algorithmTime, bar_width,
                        alpha=opacity, color='r', error_kw=error_config,
                        label='Czas w mikrosekundach')

        ax.set_xlabel('Algorytmy')
        ax.set_ylabel('Prównania i czasy')
        ax.set_title('Ilość porównań i czas')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(self.algorithmName)
        ax.legend()

        fig.tight_layout()
        plt.show()
