#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def garmonic_mean(*args: list[float]) -> float | None:
    
    ans = 0
    for i in args:
        ans += 1/i
    
    return (len(args)/ans) if args else None


if __name__=="__main__":
    a: list[float] = list(map(float, input("Введите значения через пробел: ").split()))
    print(garmonic_mean(*a))
