import sys
import numpy as np

class dnasequence:
  """Class dnasequences creates and modifies sequences of DNA bases.
  
  Attributes:
  check 
  bases: the allowable DNA bases A,C,G,T
  seq: a string of bases without separating punctuation such as "ACGT".
  complements: a dict of complementary bases.
  """

  # "magic" initialisation method
  # seq is optional input, default is "" (empty string)
  def __init__(self,seq=""):
    """__init__ does not usually have a docstring."""

    # Initialise attributes:
    # set bases
    self.bases=np.asarray(["A","C","G","T"])
    # the complements attribute is a dict (dictionary) containing complementary base pairs.
    # Example of usage: self.complements["A"] returns "T".
    self.complements={
      "A": "T",
      "T": "A",
      "C": "G",
      "G": "C"
    }

    # First test: check if input seq is an iterable type
    try:
      it = iter(seq)
    # if not, exit
    except TypeError, te:
      print(seq, "is not a valid object for creating a sequence. Exiting program.")
      sys.exit()

    # the attribute seq is a numpy array defined from the input string seq
    self.seq=np.array(list(seq))
    
    # Second test: check seq contains only valid bases by calling isdna method
    if(not self.isdna()):
      print("seq contains invalid bases. Exiting program.")
      sys.exit()
    
    return None

  def isdna(self):
    """Check that self.seq only contains valid DNA bases.
    Returns True if so, else False."""
    passes=True
    # Task 1: your code here
  
    for i in range(len(self.seq)):
        if self.seq[i] not in self.bases:
		passes= False
    return passes

  
  # example method
  def isequal(self,other):
    """Test if a DNA sequence is identical to this one."""

    # test lengths are equal.
    if(len(self.seq) != len(other.seq)):
      print("Sequences are of different lengths. isequal() returning False.")
      equal=False
    # if equal lengths, test if values are all equal.
    else:
      equal=all(self.seq==other.seq)
    # return True or False
    return equal
######### Making of a new method that returns the complement of DNA #####################
  def complement(self): 
        """Return the complementary dna string."""  
        i = [self.complements[base] for base in self.seq] 
        return ''.join(i) 

############################################################
  def compare(self, other):
    # test lengths are equal.
	saveindex=[]
	if(len(self.seq) != len(other.seq)):  ###########if both sequences are of different length#########
		print("Sequences are of different lengths. isequal() returning False.")
     		sys.exit()
	else:
		for i in range(len(self.seq)): ###########if both are same method returns the mismatch of bases######
			if self.seq[i]!=other.seq[i]:
				saveindex.append(i+1)
	if len(saveindex)==0:        ####### if it reaches at end without finding a mismatch then following code runs and returns -1 ######
		saveindex.append(-1)
	return saveindex[0]
	
###########################################################


 
############################################################
  def gene(self):
	convertseq=self.seq.tostring()
	n = convertseq.count("AAAAAAAAAATTTTTTTTTT")
	convertseq.split("AAAAAAAAAATTTTTTTTTT")
	list1=convertseq.split("AAAAAAAAAATTTTTTTTTT")
	#print list1
	print "Number of separators : ",n
	separator="AAAAAAAAAATTTTTTTTTT"
	result = convertseq.find(separator)
	return list1,dnasequence(seq=convertseq[0:result]) 



################# task6  ############################
  def find_nonmatch(self1, other):
	convertseq1=self1.seq.tostring() #converting into tostrings
	convertseq2=other.seq.tostring()
	list1=convertseq1.split("AAAAAAAAAATTTTTTTTTT")
	list2=convertseq2.split("AAAAAAAAAATTTTTTTTTT")
	#print list1
	#print list2
	count=0
	for i in range (len(convertseq1)):
		if convertseq1[i]==convertseq2[i]:
			count=count+1
	return list1,list2,count
	















