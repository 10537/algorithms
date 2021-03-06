#!/usr/bin/env python
# encoding: utf-8

import cProfile
import trace


'''
This exercise check a list of tuple that containt pairs of words for know if the 
partner is a anagram of the first element of the tuple. 
'''

#~ For more information use trace
tracer = trace.Trace(count=True, trace=False, outfile='001.dat')

def ToDict(word=''):
	freq = {}
	listword = list(word.replace(" ",""))
	for char in listword:
		if freq.get(char):
			freq[char] += 1
		else:
			freq[char] = 1
	return freq

def CheckAnagram(word=()):
	word = (ToDict(word[0]), ToDict(word[1]))
	for comp in word[0].keys():
		if word[1].get(comp):
			if word[0][comp] != word[1][comp]:
				return False
		else:
			return False 
	return True

def CheckList(words):
	for word in words:
		print "%s is anagram of %s : %s" % (word[0], word[1], CheckAnagram(word))

listofwords = [('anagram', 'gramana'), ('bad credit', 'debit cart'), ('duck', 'kucd'), ('yard', 'rady')]

# cProfile.run('CheckList(listofwords)')
tracer.runfunc(CheckList, listofwords)
report = tracer.results()
report = trace.Trace(count=False, trace=False, infile='001.dat')
results = tracer.results()
results.write_results(summary=True, coverdir='.')