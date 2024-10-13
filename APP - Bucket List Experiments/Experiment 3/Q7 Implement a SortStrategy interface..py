""" Implement a SortStrategy interface with a method sort. Create two concrete strategies, BubbleSort
and QuickSort, each implementing the sort method. Create a Sorter class that uses a SortStrategy
to sort a list. Demonstrate sorting a list with both strategies.
Concepts Covered: Strategy Pattern """

from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

class QuickSort(SortStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)

data = [5, 3, 8, 6, 2]

bubble_sorter = Sorter(BubbleSort())
sorted_data_bubble = bubble_sorter.sort(data.copy())
print("Bubble Sort result:", sorted_data_bubble)

quick_sorter = Sorter(QuickSort())
sorted_data_quick = quick_sorter.sort(data.copy())
print("Quick Sort result:", sorted_data_quick)
