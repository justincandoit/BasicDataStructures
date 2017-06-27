# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def parent(i):
    return int((i - 1) / 2)

  def leftchild(i):
    return 2 * i + 1

  def rightchild(i):
    return 2 * i + 2

  def siftdown(self, start, end):
    left = HeapBuilder.leftchild(start)

    while left <= end:
        swap = start
        right = HeapBuilder.rightchild(start)

        if self._data[swap] > self._data[left]:
            swap = left

        if right <= end and self._data[swap] > self._data[right]:
            swap = right

        if swap == start:
            break
        else:
            self._swaps.append((start, swap))
            self._data[swap], self._data[start] = self._data[start], self._data[swap]
            start = swap
            left = HeapBuilder.leftchild(start)

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    end = len(self._data) -1
    start = HeapBuilder.parent(end)
    while start >= 0:
      self.siftdown(start, end)
      start -= 1






  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
