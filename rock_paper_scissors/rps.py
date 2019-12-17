#!/usr/bin/python

import sys

def move_combinations(prev, n, all_results):
  #add R, or P, or S to prev
  if n == 0:
    all_results.append(prev)
    return

  moves = ['rock', 'paper', 'scissors']
  for move in moves:
    move_combinations(prev + [move], n - 1, all_results)

  return all_results

def rock_paper_scissors(n):
  results = []
  move_combinations([], n, results)
  return results 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

