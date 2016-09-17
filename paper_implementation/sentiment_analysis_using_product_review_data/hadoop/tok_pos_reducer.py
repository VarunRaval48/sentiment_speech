#!/usr/bin/env python

import nltk;
import sys;

def main():
	for line in sys.stdin:
		asin, review = line.split('\t')
		#print(review_text)
		review_text, overall = review.split('\s\s')
		review_pos_text = nltk.pos_tag(eval(review_text))
		print(asin, '\t', review_pos_text, '\t', overall)

if __name__ == "__main__":
        main()
