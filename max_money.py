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
print "%.2f\t\t\t" % total, # current supply is 0
print "%.24g" % (current_reward / 10**8)

while current_reward > 1: # bigger than one satoshi
    halving_count += 1
    print "%d\t" % halving_count,
    total += reward_interval * current_reward
    print "%.2f\t" % (total / 1), # current supply is going bigger to max_money
    current_reward /= 2
    print "%.24g" % (current_reward / 1)

print "Total BTC to ever be created:", total, "Satoshis"
print "Total BTC to ever be created:", total/10**8, "BTC"


# output example - BTC
"""
count	supply			reward
0	0.00			50
1	1050000000000000.00	2500000000
2	1575000000000000.00	1250000000
3	1837500000000000.00	625000000
4	1968750000000000.00	312500000
5	2034375000000000.00	156250000
6	2067187500000000.00	78125000
7	2083593750000000.00	39062500
8	2091796875000000.00	19531250
9	2095898437500000.00	9765625
10	2097949218750000.00	4882812.5
11	2098974609375000.00	2441406.25
12	2099487304687500.00	1220703.125
13	2099743652343750.00	610351.5625
14	2099871826171875.00	305175.78125
15	2099935913085937.50	152587.890625
16	2099967956542968.75	76293.9453125
17	2099983978271484.50	38146.97265625
18	2099991989135742.25	19073.486328125
19	2099995994567871.25	9536.7431640625
20	2099997997283935.75	4768.37158203125
21	2099998998641968.00	2384.185791015625
22	2099999499320984.00	1192.0928955078125
23	2099999749660492.00	596.04644775390625
24	2099999874830246.00	298.023223876953125
25	2099999937415123.00	149.0116119384765625
26	2099999968707561.50	74.50580596923828125
27	2099999984353780.75	37.252902984619140625
28	2099999992176890.50	18.6264514923095703125
29	2099999996088445.25	9.31322574615478515625
30	2099999998044222.75	4.656612873077392578125
31	2099999999022111.50	2.3283064365386962890625
32	2099999999511055.75	1.16415321826934814453125
33	2099999999755528.00	0.582076609134674072265625
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