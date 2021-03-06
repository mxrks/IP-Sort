#!/usr/bin/python

with open("targets.txt", "r") as infile:
    ips = sorted([i.strip() for i in infile.readlines()], key = lambda x: int(''.join((lambda a:lambda v:a(a,v))(lambda s,x: x if len(x) == 3 else s(s, '0'+x))(i) for i in x.split('.'))))

with open("targets.txt", "w") as outfile:
    outfile.write("\n".join(i for i in ips))
