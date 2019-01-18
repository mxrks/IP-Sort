# IP-Sort
This simple python script will put IPv4 addresses in numeric order starting from the first octet.

# Example usage
Input file is default to "targets.txt and automatically overwrites targets.txt with the addresses in order. Change this according to your specifications in the source code

- with open("input.txt", "r") as infile: -- infile (Input File) = "input.txt" 
- with open("output.txt", "w") as outfile: -- outfile (Output File) = "output.txt"

```
py ipsort.py
```
# Before Execution
A randomly generated set of IPv4 addreses.
```
222.21.147.97
187.234.9.45
144.101.36.131
31.192.196.59
24.16.131.84
8.52.22.181
17.40.228.224
58.164.169.156
234.78.147.45
254.150.145.225
167.111.243.3
```

# After execution of the script
Organised list of IP addresses 
```
8.52.22.181
17.40.228.224
24.16.131.84
31.192.196.59
58.164.169.156
144.101.36.131
167.111.243.3
187.234.9.45
222.21.147.97
234.78.147.45
254.150.145.225
```
