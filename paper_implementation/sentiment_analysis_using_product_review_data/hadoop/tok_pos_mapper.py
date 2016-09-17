#!/usr/bin/env python

import nltk;
import sys;

def proc_input(lines):
	for line in lines:
		yield eval(line)

def main(separator='\t'):
	review_text = 'reviewText'
	all_keys = ['reviewText', 'reviewerID', 'reviewTime', 'asin', 'reviewerName', 'overall', 'unixReviewTime', 'summary', 'helpful']
	req_keys = ['reviewText', 'overall', 'asin']
	df = {}
	for d in proc_input(sys.stdin):
		df = {key: d[key] for key in req_keys}
		df[review_text] = nltk.word_tokenize(df[review_text])
		print(df['asin'], '\t', df[review_text], '\s\s', df['overall'])

if __name__ == "__main__":
        main()
