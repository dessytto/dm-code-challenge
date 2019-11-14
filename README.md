This script reates a reusable tool that generates a csv file of filtered results and creates a pie chart that renders in the browser. 

How to use the script:
===================================
Download the project directory and navigate to the folder.

From a python terminal:
------------

- type or paste the following: ﻿runfile('./dosing.py', wdir='./', args='w02 Y 280 output/directory/for/results/')
- args are the parameters based on which the results will be filtered. 
- In this example:
	○ registry.viscode is w02
	○ registry.svdose is Y
	○ ECSDSTXT is not 280
	
### For example, if you downloaded the folder to your Downloads folder and want the results to be output in the same folder, type:
	cd ~/Downloads/dm-data-challenge
	runfile('./dosing.py', wdir='./', args='w02 Y 280 ./')	

Directly from the terminal:
------------
- type or paste the following:   python dosing.py w02 Y 280 output/directory/for/results/

### For example, if you downloaded the folder to your Downloads folder and want the results to be output in the same folder, type:
	cd ~/Downloads/dm-data-challenge
	python dosing.py w02 Y 280 ./

