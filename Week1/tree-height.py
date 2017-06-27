# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                maxHeight = 0;
                heights = [0] * len(self.parent)
                # print('heights ' + str(heights))
                for vertex in range(self.n):
                    if (heights[vertex] != 0):
                        # print('first if')
                        continue
                    height = 0
                    i = vertex
                    while i != -1:
                        # print('first i = '+ str(i))
                        if (heights[i] != 0):
                            height += heights[i]
                            # print('first height = '+str(height))
                            break
                        height += 1
                        # print('height at end of first if = '+str(height))
                        i = self.parent[i]
                    maxHeight = max(maxHeight, height)
                    # print('max height ' +str(maxHeight))
                    i = vertex
                    while i != -1:
                        # print('second i = ' + str(i))
                        if (heights[i] != 0):
                            break
                        heights[i] = height
                        height -= 1
                        i = self.parent[i]
                return maxHeight








        def old_compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
