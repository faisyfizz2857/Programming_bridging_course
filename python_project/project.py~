import sys # for exiting on errors
import numpy as np
import random
import matplotlib.pyplot as plt
import dnasequences as dna # import user-defined DNA sequence class
#import genome_01
def randomstr(N):
  """Generate a random string of bases of length N"""
  return "".join([random.choice('ACGT') for i in range(N)])

def read(name):
  datafile = open(name,'r')
  #print '\n reading data from',name
  lines=datafile.readlines()
  line=lines[1]
  dnaseq=dna.dnasequence(line)
  	#vars = [str(j) for j in row.split(';')]
  #temp.append (vars[0])
  #print '\n total number of bases: \n', sum(temp)
	
  return dnaseq
######################## reading file 2 ##################
def readfile2(name):
  datafile = open(name,'r')
  #print '\n reading data from',name
  lines=datafile.readlines()
  line=lines[1]
  dnafile2=dna.dnasequence(line)
  	#vars = [str(j) for j in row.split(';')]
  #temp.append (vars[0])
  #print '\n total number of bases: \n', sum(temp)
	
  return dnafile2
#######################################################

def main():

  # generate a random string of bases of length 10.
  # this is a single-stranded DNA sequence.
  mystr=randomstr(10)
  print(mystr)
  # example DNA sequence strings for testing
  crick_str= "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
  #orgcrick_str= "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
  # this is the complement of crick_str
  watson_str="TACCGGTAACATTACCCGGCGACTTTCCCACGGGCTATC"
  # crick with insert mutations
  crick2_str= "ATGGCCATTGTAATGGGCCGCTGAAACGGGTGCCTCGAT"
  #orgcrick2_str= "ATGGCCATTGTAATGGGCCGCTGAAACGGGTGCCTCGATAG"
  #stringfordna= "ACGT"
  # TEST: make a dnasequence instance with an empty sequence.
  myseq=dna.dnasequence()
  # this is how to print the seq attribute of a dnasequence
  print(myseq.seq)
  
  # TEST: make a dnasequence instance with an invalid sequence.
  # should return a fatal error.
  #myseq=dna.dnasequence(seq="U") ######if we uncomment this then it will show our work for 1st task######
  
  # this is how to create a dnasequence instance from mystr.
  myseq=dna.dnasequence(seq=mystr) ########if we comment this then it will show our work for 1st task#######
  print(myseq.seq)
  
  # Your code here...
##########task2###################
  compseq=dna.dnasequence.complement(myseq)
  print "This is the complement of dna sequence: ",compseq




#############task2 Comparing stirngs############### 
  crick = dna.dnasequence(seq=crick_str)
  comp = dna.dnasequence.complement(crick)
  print comp==watson_str
  
################## Task 3 ###################

  crick2 = dna.dnasequence(seq=crick2_str)
  print "the index of first non-matching bases in crick_str and crick2_str: ",dna.dnasequence.compare(crick, crick2)
 
#################### Task 4 ################################
  seq=read('genome_01.dat')   ### reading from genome_01 file
  print "Total number of bases", len(seq.seq)



############### task 6 reading file 2 ##################
  seq2=read('genome_02.dat')   ### reading from genome_01 file
#dna.dnasequence.gene(seq)





############################ Task5 #####################################
  list1,first_gene=seq.gene()
  print "length of first gene : ",len(first_gene.seq)
               #########################
  dna_list = [first_gene]
  y=[len(x) for x in list1]
  x=[i for i in range (0, len(list1))]
  #print y
  plt.bar(x,y) ##ploting of gene length
  plt.show()
  
  
######################### task6  #####################

  list1,list2,num=dna.dnasequence.find_nonmatch(seq,seq2)  
  print num
  y=[len(x) for x in list2]
  x=[i for i in range (0, len(list1))]
  #print y
  plt.scatter(x,y)
  plt.show()
  return  
main()


  












