#!/usr/bin/env python3
import sys
def main():
  contents = sys.stdin.read()   # Leemos el standard input
  sys.stdout.write(contents.replace(sys.argv[1], sys.argv[2]))  # escribimos en el standard output
main()