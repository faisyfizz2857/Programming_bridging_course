  def gene(self):
	convertseq=self.seq.tostring()
	n = convertseq.count("AAAAAAAAAATTTTTTTTTT")
	convertseq.split("AAAAAAAAAATTTTTTTTTT")
	list1=convertseq.split("AAAAAAAAAATTTTTTTTTT")
	#print list1
	print n
	separator="AAAAAAAAAATTTTTTTTTT"
	result = convertseq.find(separator)
	return dnasequence(seq=convertseq[0:result]) 




  
  first_gene=seq.gene()
  print len(first_gene.seq)
               #########################
  dna_list = [first_gene]
  #list1=dna.dnasequence.gene.convertseq.split("AAAAAAAAAATTTTTTTTTT")
  N = str(first_gene.seq).count("AAAAAAAAAATTTTTTTTTT")
  print N
  print str(first_gene.seq)
  print first_gene.seq
  for i in range(1,N):
  	seq1=str(seq)[20*i+len(dna_list[i-1].seq)]
  	dna_list.append(dna.dnasequence(seq=seq1).gene())
  y=[len(gene.seq) for gene in dna_list]
  x=[i for i in range (0, len(dna_list))]
  print y
  plt.bar(x,y)
  plt.show()
  






##########################################


  first_gene=seq.gene()
  print len(first_gene.seq)
               #########################
  dna_list = [first_gene]
  #list1=dna.dnasequence.gene.convertseq.split("AAAAAAAAAATTTTTTTTTT")
  N = str(seq.gene()).count("AAAAAAAAAATTTTTTTTTT")
  print "this is first ",first_gene.seq
  for i in range(1,N):
  	seq1=str(seq)[20*i+len(dna_list[i-1].seq)]
  	dna_list.append(dna.gene(seq=seq1))
  y=[len(gene.seq) for gene in dna_list]
  x=[i for i in range (0, len(dna_list))]
  print "this is something",y
  plt.bar(x,y)
  plt.show()
  










 #----------------------------------task1
  # Lauri's 
  def isdna(self):
    """Check that self.seq only contains valid DNA bases.
    Returns True if so, else False."""
    passes=True

    # Searching in the np array if the bases are found in it or not
    is_match = np.isin(self.seq, self.bases)
    # k is a tuple indicating the location of the element i
    # Iterating through each element in the boolean valued is_match vector
    for k, i in np.ndenumerate(is_match):
      if i == False:
        passes = False
        break

  # if any(characters in self.seq_string for characters in base_list):
  #     passes = False
    return passes
  
  
  # Mehdi
  def isdna(self):
    """Check that self.seq only contains valid DNA bases.
    Returns True if so, else False."""
    passes=True
    for i in self.seq:
    	if i not in self.bases:
    		passes=False
    return passes
  
  
  ###faisal 
    def isdna(self):
    """Check that self.seq only contains valid DNA bases.
    Returns True if so, else False."""
    passes=True
    # Task 1: your code here
  
    for i in range(len(self.seq)):
        if self.seq[i] not in self.bases:
    			passes= False
    return passes

  ######### Babar
  
  def isdna(self):
    """Check that self.seq only contains valid DNA bases.
   -
  	for i in self.seq: 								# i element of the sequence 
  		val.append(self.complements[i]) # add to the list the complementary character using the dictionary
  	result=dnasequence(seq=''.join(val))
    return (result)
  
  	####faisal
    
    def complement(self): 
        """Return the complementary dna string."""  
        i = [self.complements[base] for base in self.seq] 
        return ''.join(i)
      
  #------------------------------------------------------------task3    
   
   	##Babar
    def mati(self,str1):
    	for index in range(len(self.seq)):
    		str2 = self.seq[:]
        if str2[index] != str1[index]:
            l=[]
            l.append(index)
        else:
              rtl = index
      	return rtl          
	
  
  ##Mehdi
  def matchDetector(self,other):
	if(len(self.seq) != len(other.seq)):
		print("Sequences are of different lengths. ")
		sys.exit()
	else:
		i=0
		res=[]
		while i<len(self.seq):
			if self.seq[i]!=other.seq[i]:
				res.append(i)
			i+=1
		if i == len(self.seq):
			return(-1)
		else:
			return(res[0])
    
    ###faisal task3

  def compare(self, other):
    # test lengths are equal.
	saveindex=[]
	if(len(self.seq) != len(other.seq)):  ###########if both sequences are of different length#########
		print("Sequences are of different lengths. isequal() returning False.")
     		sys.exit()
	else:
		for i in range(len(self.seq)): ###########if both are same, method returns the mismatch of bases######
			if self.seq[i]!=other.seq[i]:
				saveindex.append(i+1)
	if len(saveindex)==0:        ####### if it reaches at end without finding a mismatch then following code runs and returns -1 ######
		saveindex.append(-1)
	return saveindex[0]
	
  

  ### Lauri
    def find_first_non_match(self, other):
      """
      :param other: the dnasequence object of which sequence is compared to the self
      :return: the index of the non-matching base of the sequences or -1 if
      the sequences are the same
      """
      if self.isequal(other): # Checking if the two sequences are the same in sequence and length
        #print("-1")
        return -1
      #  if (self.seq==other.seq).all(): # If yes, check if they are the same.
      else:
        # If they aren't either the lengths of the sequences isn't the same
        if self.length != other.length:
          print("Exiting...")
          sys.exit()
        else: # Or the sequences aren't the same
          index = np.where(self.seq != other.seq)[0]
      print("The first non-matching base is located in index:", index[0])
      return index[0]
  
  
  
  
  
  #----------------------------------------task4
  
  
  ############### task 4 ##############
  # faisal
  def read(name):
  datafile = open(name,'r')
  print '\n reading data from',name
  lines=datafile.readlines()
  line=lines[1]
  dnaseq=dna.dnasequence(line)	
  return dnaseq.seq

# Lauri
def read_ascii_gene_file(name):
    """
    This function reads ASCII-format genome files
    :param name: the name of the file
    :return: dnasequence object containing the sequence read from the file
    """
    datafile = open(name, 'r')

    # read the first line
    header = datafile.readline()
    # read the second line
    genome = datafile.readline()

    new_dna_seq_object = dna.dnasequence(genome)

    datafile.close()
    return new_dna_seq_object
   
    
    # Mehdi
    
    
    def read_genome(name):
	""" ​reads​ ​in​ ​ASCII-format​ ​genome​ ​files"""
	datafile=open(name,'r')
	myseq=dna.dnasequence(seq=datafile.readlines()[1])
	return (myseq)

## Babar

# data file name (file should be in the same directory as this script)
import numpy as np
def Genome():

 name = 'genome_01.dat'

# read in the data from given file.
# datafile is an object of type file.
 datafile = open(name,'r')
 print '\n reading data from',name

# read the first line
 columns = datafile.readline()
# split columns string into semicolon-separated values
 columns = columns.split(';')
 print '\n column labels: \n',columns

 # loop over all rows in datafile
 for row in datafile:
   mylist =np.array(list(row))
   print mylist 
  
  
  #=======================================task5 
  #mehdi
  
  def first_Gene(self):
  	"""."""
  	separator="AAAAAAAAAATTTTTTTTTT"
  	res=self.split(separator)
  	print('length of first gene is : ', len(res[0]))
    gene=dnasequence(seq=res[0])
  	return(gene)
  
 #second part 

  dnalist1=[dna.first_Gene(genome1)]
  
  length_i=0		#length of ....					
  for i in range(1,genome1.count("AAAAAAAAAATTTTTTTTTT")):
  	length_i+=len(dnalist1[-1].seq)
  	dnalist1.append(dna.first_Gene(genome1[length_i+20*i:]))

  x=range(len(dnalist1))
  y=[len(gene) for gene in dnalist1]
  plt.bar(x,y)
  
  
  
  
  
  
  
  
  ### Lauri 
   def find_gene(self):
    """
    This method finds the first gene separated by the separator sequence
    if no separator sequence exists it returns two same dnasequence objects.
    :return:
    gene1 which is a dnasequence object containing the first dna sequence
    gene2 which is a dnasequence object containing the rest of the dna sequence
    """
    """
        Weakness with this approach would be to need to join the rest of the 
        genes back and its unnecessary to split rest but only the first gene
        index = self.seq_string.find("AAAAAAAAAAATTTTTTTTTT")
       # print(index)
        if index == -1:
          gene = dnasequence(self.seq_string)
        else:
          genelist = self.seq_string.split("AAAAAAAAAAATTTTTTTTTT")
         # print(genelist)
          gene1 = dnasequence(genelist[0])
         # print(gene.seq)
    """

    index = self.seq_string.find("AAAAAAAAAAATTTTTTTTTT")
    if index == -1:
      gene1 = dnasequence(self.seq_string)
      gene2 = dnasequence(self.seq_string)
    else:
      gene1 = dnasequence(self.seq_string[:index])
      gene2 = dnasequence(self.seq_string[index+21:])
    return gene1, gene2
  
  
  def find_gene_list(genome):
    """
    This searches through a genome (a collection of genes) and finds genes in it.
    :param genome: The collection of genes
    :return: A list of dnasequence objects (genes) found in the genome
    """
    # Initialize an empty gene list
    gene_list = []
    # Make sure that we come inside the while loop
    contain_new_genes = True
    # Searching through the genome for the first genes
    gene, the_rest = genome.find_gene()
    while contain_new_genes:
        # Checking if the two genes are the same
        if (gene.seq_string == the_rest.seq_string):
            # If they are we have come to the end of our search for genes and add just the last gene
            contain_new_genes = False
            gene_list.append(gene)
        else:
            # If the genes are not the same add the new gene to the gene_list
            gene_list.append(gene)
            # In addition find possible new genes
            gene, the_rest = the_rest.find_gene()
    return gene_list
 #############################################################

  dnalist1=[dna.dnasequence.first_Gene(dnaseq)]
 
  length_i=0					
  for i in range(1,genome1.count("AAAAAAAAAATTTTTTTTTT")):
  	length_i+=len(dnalist1[-1])
  	dnalist1.append(dna.first_Gene(genome1[length_i+20:]))

  x=range(len(dnalist1))
  y=[len(gene) for gene in dnalist1]
  plt.bar(x,y)














########################
all_genes=seq.getGenes()
  N = len(all_genes)
  #print len(all_genes.seq)
               #########################
  #dna_list = [first_gene]


  #list1=dna.dnasequence.gene.convertseq.split("AAAAAAAAAATTTTTTTTTT")
#  N = str(seq.gene()).count("AAAAAAAAAATTTTTTTTTT")
 
  
  #print "this is first ",getGenes.seq
  #for i in range(1,N):
  	#seq1=str(seq)[20*i+len(dna_list[i-1].seq)]
  	#dna_list.append(dna.gene(seq=seq1))
  #temp2=temp1
  list_for_genes=[]
  for x in all_genes:
	temp1=x.get_length_of_gene()
	list_for_genes.append(temp1)
  y=[for gene in list_for_genes]
  x=[i for i in range (0, len(list_for_genes))]
  print y
  plt.bar(x,y)
  plt.show()
  #x = range(list_for_genes)
  #print len(list_for_genes)
  #x=[i for i in range (0, len(N))]
  #print "this is something",y
  #plt.bar(x,list_for_genes)
  #plt.show()
##########################################################
  def getGenes(self):
	convertseq=self.seq.tostring()
	separator="AAAAAAAAAATTTTTTTTTT"

	n = convertseq.count(separator)
	#convertseq.split(separator)
	list1=convertseq.split(separator)

#	print list1
#	print n
	result = convertseq.find(separator)
#	return dnasequence(seq=convertseq[0:result])

	tmp = []
	for seqq in convertseq:
		tmp.append(dnasequence(seq=seqq))
	return tmp
################task6###################
  def get_length_of_gene(self):
   	temp=len(self.seq)
  	return temp
 

