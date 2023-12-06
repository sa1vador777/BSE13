#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def prod(*args: list[float]) -> float:
    
    max_num_index, min_num_index = (
        args.index(max(args)), args.index(min(args))
    )

    return sum([i for i in args[min_num_index+1:max_num_index]]) if min_num_index\
    < max_num_index else sum([i for i in args[max_num_index+1:min_num_index]])


if __name__ == "__main__":
    args: list[float] = list(map(float, input("Введите значения через пробел: ").split()))
    print(prod(*args))
