#!/usr/bin/env python
# encoding: utf-8
# developped by Sébastien Boisvert

"""
CheckNotInTree.py TreeOfLife-Edges.tsv Taxon-Names.tsv

check the sanity of the tree

"""

import sys

if len(sys.argv)!=3:
	print __doc__
	sys.exit(1)

parents={}
children={}
names={}
ranks={}

def printVertex(vertex):
	return "(taxon (identifier "+str(vertex)+") (taxon "+str(names[vertex])+") (rank "+ranks[vertex]+"))"
	
for line in open(sys.argv[2]):
	tokens=line.split("\t")

	vertex=int(tokens[0])
	name=tokens[1].strip()
	rank=tokens[2].strip()
	
	names[vertex]=name
	ranks[vertex]=rank

for line in open(sys.argv[1]):
	tokens=line.split("\t")
	parent=int(tokens[0])
	child=int(tokens[1])

	if child in parents:
		print ""
		print "Error, "+printVertex(child)+" already has parent "+printVertex(parents[child])+" Tried to add second parent "+printVertex(parent)

	parents[child]=parent

	if parent not in children:
		children[parent]={}

	if child in children[parent]:
		print "Error, "+str(parent)+" already has child "+str(child)


print "OK, loaded tree"

for line in open(sys.argv[2]):
	tokens=line.split("\t")

	vertex=int(tokens[0])
	name=tokens[1].strip()
	rank=tokens[2].strip()
	
	if vertex not in parents:
		print "Error, "+str(vertex)+" has no parent and thus is not in the tree unless it is the root, name="+name+" rank="+rank

print "Good luck."
