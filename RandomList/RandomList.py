"""
Program: Creating and populating a list with specific criteria
Author: Riyam Arabo
Last Modified: 9/22/18

Purpose: To create and populate a list using the following criteria:
1. The list's length must be determined by a random number between 5 and 8
2. The list must be initialized with 2
3. The rest of the list's elements must be populated using random numbers
4. Each element populated must be equal to or greater than the previous element, but must be smaller than the double of the previous element
5. Display the list contents, the sum of the elements, their median and average.
6. The program must be written in 5 lines or less
"""
import random
randomList = [2] * random.randint(5, 8)
for generate in range(1, len(randomList)):
    randomList[generate] = random.randint(randomList[generate - 1], (randomList[generate - 1] * 2) - 1)
print("List:", ' '.join(str(x) for x in randomList), "-Sum:", sum(randomList), " -Median:", randomList[len(randomList) // 2] if len(randomList) % 2 == 1 else (randomList[len(randomList) // 2] + (randomList[len(randomList) // 2 - 1])) / 2, " -Average: %0.2f" % (sum(randomList) / len(randomList)))
