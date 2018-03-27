from __future__ import print_function

import sys, re

taqman_results = open(sys.argv[1])
regex_line = '(.+)\t(.+)\t(\d)\t(\d)'

master_dic = {}
assay_list = []
sample_list = []
missing_list = []

#Parses taqman output into lists and nested dictionary
for line in taqman_results:
	line_search = re.search(regex_line, line)	

	if line_search:
		
		if line_search.group(1) not in master_dic:
			master_dic[line_search.group(1)] = {}
			sample_list.append(line_search.group(1))
		
		if line_search.group(2) not in assay_list:
			assay_list.append(line_search.group(2))
		
		master_dic[line_search.group(1)][line_search.group(2)] = line_search.group(3) + "," + line_search.group(4)

#Puts samples in descending order and alphabetizes assays	
sample_list.sort()
assay_list.sort()

#Prints assay header
print("," , end = "")
for assay in assay_list:
	print(assay + "," + assay + "," , end = "")
print("")

#Prints samples and data
for sample in sample_list:
	print(sample + ",", end = "")
	
	for assay in assay_list:
		try:
			print(master_dic[sample][assay] + "," , end = "")
	
		except KeyError:
			print("0,0,", end = "")
			missing_list.append("Sample: " + sample + " is missing data for assay " + assay)
	
	print("")

for item in missing_list:
	print(item)