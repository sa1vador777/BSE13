#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def geometric_mean(*args: list[float]) -> float | None:

    ans = 1
    for i in args:
        ans *= i
    return (ans)**(1/(len(args))) if args else None


if __name__=="__main__":
    a: list[float] = list(map(float, input("Введите значения через пробел: ").split()))
    print(geometric_mean(*a))
