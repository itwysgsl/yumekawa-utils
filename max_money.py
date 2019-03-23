#!/usr/bin/python
# Code from https://github.com/bitcoinbook/bitcoinbook/blob/develop/code/max_money.py

#######
### BTC
#######

# Original block reward for miners was 50 BTC
start_block_reward = 50
# 210000 is around every 4 years with a 10 minute block interval
reward_interval = 210000

def max_money_BTC():
    # 50 BTC = 50 0000 0000 Satoshis
    current_reward = 50 * 10**8
    total = 0
    while current_reward > 0:
        total += reward_interval * current_reward
        current_reward /= 2
    return total

print "\nBTC"
print "Total BTC to ever be created:", max_money_BTC(), "Satoshis"
print "Total BTC to ever be created:", max_money_BTC() / 10**8, "BTC"

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