#!/usr/bin/env python3

import json
import subprocess
import pandas as pd
import numpy as np
import os, sys, argparse
import glob

def generateSummaryCsv(subjectID,profiles,outdir):

	# make tract structure list
	structureList = [ x for x in os.listdir(profiles) if x.split('.')[1] == 'csv' ]
	tractNames = [ x.split('_profiles.csv')[0].replace("_","") for x in structureList ]
	
	# make temporary data frame from one profiles to identify number of nodes and measures
	df_temp = pd.read_csv(os.path.join(profiles,structureList[0]))
	df_temp_reduced = df_temp[[ x for x in list(df_temp.keys()) if x.split('_')[1] == '1' ]]
	diffusion_measures = [ x.split('_')[0] for x in list(df_temp_reduced.keys()) ]
	
	# depending on what's in the array, rearrange in a specific order I like
	if all(x in diffusion_measures for x in ['ndi','fa']):
		diffusion_measures = ['ad','fa','md','rd','ndi','isovf','odi']
	elif 'fa' in diffusion_measures:
		diffusion_measures = ['ad','fa','md','rd']
	else:
		diffusion_measures = ['ndi','isovf','odi']

	nodes = [ x for x in range(len(df_temp_reduced[diffusion_measures[0]+'_1'])) ]
	
	# clear temp data
	del df_temp,df_temp_reduced
	
	# set columns for pandas array
	columns = ['subjectID','structureID','nodeID'] + diffusion_measures

	# set up pandas dataframe
	df = pd.DataFrame([],columns=columns,dtype=object)
	df['subjectID'] = [ subjectID for x in range(len(structureList) * len(nodes)) ]
	df['structureID'] = [ tractNames[ int(x / len(nodes))] for x in range(len(structureList) * len(nodes)) ]
	df['nodeID'] = list(np.tile(np.array(range(1,len(nodes)+1)),len(structureList)))

	# loop through diffusion measures and read in diffusion measure data. each csv will contain all diffusion measures
	for tracts in range(len(structureList)):

		data = pd.read_csv(os.path.join(profiles,structureList[tracts]))
		data_means = data[[ x for x in list(data.keys()) if x.split('_')[1] == '1' ]]

		for measures in diffusion_measures:
			df.loc[df.structureID==tractNames[tracts], measures] = list(data_means[measures+'_1'])

	# sort by tract and subject ID
	df.sort_values(['structureID','nodeID'],inplace=True)
	
	# write out to csv
	df.to_csv('./%s/tracts.csv' %(outdir), index=False)

def main():

	print("setting up input parameters")
	#### load config ####
	with open('config.json','r') as config_f:
		config = json.load(config_f)

	#### parse inputs ####
	subjectID = config['_inputs'][0]['meta']['subject']
	profilesdir= config['profiles']

	#### set up other inputs ####
	# set outdir
	outdir = 'tractmeasures'
	
	# generate output directory if not already there
	if os.path.isdir(outdir):
		print("directory exits")
	else:
		print("making output directory")
		os.mkdir(outdir)

	#### run command to generate csv structures ####
	print("generating csvs")
	generateSummaryCsv(subjectID,profilesdir,outdir)

if __name__ == '__main__':
	main()
