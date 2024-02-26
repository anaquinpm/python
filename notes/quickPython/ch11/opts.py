#! /usr/bin/env python3
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()       # Crea una instancia del objeto
    parser.add_argument("indent", type=int, help="indent for report")     # Positional arg (no tienen declarado al inicio "-opt")
    parser.add_argument("input_file", help="read data from this file")    # Positional arg
    parser.add_argument("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE") # optional arg
    parser.add_argument("-x", "--xray", help="specify xray strength factor")                          # optional arg
    parser.add_argument("-q", "--quiet", action="store_false", dest="verbose", default=True, help="don't print status messages to std out")
    args = parser.parse_args()
    print("arguments: ", args)
main()