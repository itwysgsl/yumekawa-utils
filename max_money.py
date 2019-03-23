#!/usr/bin/python
# Code from https://github.com/bitcoinbook/bitcoinbook/blob/develop/code/max_money.py

#######
### BTC
#######

start_block_reward = 50 # Original block reward for miners was 50 BTC
reward_interval = 210000 # 210000 is around every 4 years with a 10 minute block interval

current_reward = float(50.0 * 10**8) # 50 BTC = 50 0000 0000 Satoshis
total = float(0.0)
halving_count = int(0)

print "count\tsupply\t\t\treward" 
print "%d\t" % halving_count,
print "%.4f\t\t\t" % total, # current supply is 0
print "%.8f" % (current_reward / 10**8)

while current_reward > 1: # bigger than one satoshi
    halving_count += 1
    print "%d\t" % halving_count,
    total += reward_interval * current_reward
    print "%.4f\t" % total, # current supply is going bigger to max_money
    current_reward /= 2
    print "%.8f" % (current_reward / 10**8)

print "Total BTC to ever be created:", total, "Satoshis"
print "Total BTC to ever be created:", total/10**8, "BTC"


# output example - BTC
"""
$ ./max_money.py 
count	supply			reward
0	0.0000			50.00000000
1	1050000000000000.0000	25.00000000
2	1575000000000000.0000	12.50000000
3	1837500000000000.0000	6.25000000
4	1968750000000000.0000	3.12500000
5	2034375000000000.0000	1.56250000
6	2067187500000000.0000	0.78125000
7	2083593750000000.0000	0.39062500
8	2091796875000000.0000	0.19531250
9	2095898437500000.0000	0.09765625
10	2097949218750000.0000	0.04882812
11	2098974609375000.0000	0.02441406
12	2099487304687500.0000	0.01220703
13	2099743652343750.0000	0.00610352
14	2099871826171875.0000	0.00305176
15	2099935913085937.5000	0.00152588
16	2099967956542968.7500	0.00076294
17	2099983978271484.5000	0.00038147
18	2099991989135742.2500	0.00019073
19	2099995994567871.2500	0.00009537
20	2099997997283935.7500	0.00004768
21	2099998998641968.0000	0.00002384
22	2099999499320984.0000	0.00001192
23	2099999749660492.0000	0.00000596
24	2099999874830246.0000	0.00000298
25	2099999937415123.0000	0.00000149
26	2099999968707561.5000	0.00000075
27	2099999984353780.7500	0.00000037
28	2099999992176890.5000	0.00000019
29	2099999996088445.2500	0.00000009
30	2099999998044222.7500	0.00000005
31	2099999999022111.5000	0.00000002
32	2099999999511055.7500	0.00000001
33	2099999999755528.0000	0.00000001
Total BTC to ever be created: 2.09999999976e+15 Satoshis
Total BTC to ever be created: 20999999.9976 BTC
"""


#########
### SUGAR
#########

# Original block reward for miners was 50 BTC
start_block_reward = 50
# 210000 is around every 4 years with a 10 minute block interval
reward_interval = 210000*120

def max_money_SUGAR():
    # 50 BTC = 50 0000 0000 Satoshis
    current_reward = 50 * 10**8
    total = 0
    while current_reward > 0:
        total += reward_interval * current_reward
        current_reward /= 2
    return total

print "\nSUGAR"
print "Total SUGAR to ever be created:", max_money_SUGAR(), "Satoshis"
print "Total SUGAR to ever be created:", max_money_SUGAR() / 10**8, "SUGAR"


# output
"""
$ ./max_money.py 

BTC
Total BTC to ever be created: 2099999997690000 Satoshis
Total BTC to ever be created: 20999999 BTC

SUGAR
Total SUGAR to ever be created: 251999999722800000 Satoshis
Total SUGAR to ever be created: 2519999997 SUGAR
"""