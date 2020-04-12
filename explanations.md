# Problems vs. Algorithms

Hello, my name is Aitor Rodriguez and in this file i'm going to explain the algorithms I used to solve each problem. Let's go!

## Problem 1
Time complexity is O(log n) due to tha fact that in the  worst case we search through half of half of an array. In this problem we findthe square root of the integer without using any Python library.

The problem Space complexity is: O(n) 

## Problem 2

In this problem we have Time complexity is O(log n) because at worst case we search through half of half of an array.

You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

The problem Space complexity is: O(n)  space to store the list plus the additional variables.

## 


## Problem 3
| Time Complexity      | The time complexity is `O(n log(n))`.                           |
| -------------------- | ------------------------------------------------------------ |
| Explanation | Our functions gets as the input an array of numbers and returns the tupple of the max sums. |

The problem Space complexity is: O(n)  to copy the list.

## 

## Problem 4

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Using pointers to save the index we can get the array ordered using only a single traversal.

Time Complexity: O(n)

The array is iterated through once.

The problem Space complexity is: O(n)  




## Problem 5
To solve this problem i use  a Trie with DFS In-order search. 
The time complexity for insert and find is O(n).

Time complexity for suffixes is O(V + E) where V is the vertices and E is the edges. 

The problem Space complexity is: O(n) 

## 

## Problem 6

This problem has a time complexity of O(n) .

We iterate through each number in a list of integers.

We set two variables, min_value and max_value, which we will update as check the min and max of each number. While we go trhought the array, max and min are updated if found.

The problem Space complexity is: O(n) 

## 


## Problem 7
| Time Complexity      | The time complexity is `O(1)`.                           |
| -------------------- | ------------------------------------------------------------ |
| **Space Complexity** | The space complexity is `O(1)`. No extra space is required to use this algorithm. |

We solve this problem using a Trie and node as is asked in the sample code of the problem. The handler splits the path to insert a new node which can then be traversed for the lookup.

