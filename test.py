# -*- coding: utf-8 -*-
from __future__ import print_function
p = 10
for i in range(0,10):
    for v in range(0,i):
        print(p, end=" ")
        p = p + 1
    print("")