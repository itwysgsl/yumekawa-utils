#!/usr/bin/python3

# setup
OUT_FILE='emission-iamstenman'

# GRAPH_STEPS = 12 * 60 * 24 * 30  # 1 month
GRAPH_STEPS = 12 * 60 * 24 * 365  # 1 year
GRAPH_YEARS = 4

BLOCKS_PER_MINUTE = 12  # 5 secconds for block
BLOCKS_PER_YEAR = BLOCKS_PER_MINUTE * 525960  # 525960 minutes in 1 year
REWARD_PER_BLOCK = 50
HALVING_YEARS = 2
MAX_HALVINGS = 0

def supply(height=0):
	reward = REWARD_PER_BLOCK
	halvings = (BLOCKS_PER_YEAR * HALVING_YEARS) - 1
	halvings_count = 0
	supply = 0
	rheight = height
	
	while height > halvings:
		total = halvings * reward
		reward = (reward / 2.0) if halvings_count < MAX_HALVINGS or MAX_HALVINGS == 0 else reward
		height = height - halvings
		halvings_count += 1 if halvings_count < MAX_HALVINGS or MAX_HALVINGS == 0 else 0

		supply += total
	
	supply = supply + height * reward

	return '{}, {}, {}, {}, {}\n'.format(rheight, reward, supply, halvings_count, int(rheight / BLOCKS_PER_YEAR))

data = [supply(i) for i in range(0, BLOCKS_PER_YEAR * GRAPH_YEARS, GRAPH_STEPS)]
csv = 'Height, Reward, Supply, Halvings, Year\n' + ''.join(data)

with open('%s.csv' % OUT_FILE, 'w') as file:
	file.write(csv)

# cat file on console
import os
command = os.popen('cat %s.csv' % OUT_FILE)
print(command.read())
print(command.close())