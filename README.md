This script creates a reusable tool that generates a csv file of filtered results and a pie chart that renders in the browser. 

How to use the script:
===================================
Download the project directory and navigate to the folder.

From a python terminal:
------------

- type or paste the following: ﻿runfile('./dosing.py', wdir='./', args='w02 Y 280 output/directory/for/results/')
- args are the parameters based on which the results will be filtered. 
- In this example:
	1. registry.viscode is w02
	2. registry.svdose is Y
	3. ECSDSTXT is not 280
	4. is the path to the output directory
	
### For example, if you downloaded the folder to your Downloads folder and want the results to be output in the same folder, type:
	cd ~/Downloads/dm-data-challenge
	runfile('./dosing.py', wdir='./', args='w02 Y 280 ./')	

Directly from the terminal:
------------
- type or paste the following:   python dosing.py w02 Y 280 output/directory/for/results/

### For example, if you downloaded the folder to your Downloads folder and want the results to be output in the same folder, type:
	cd ~/Downloads/dm-data-challenge
	python dosing.py w02 Y 280 ./

