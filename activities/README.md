# non B-DNA workshop hands-on challenges

This will guide you through the challenges you have to solve today.

If you don't feel confident with your programming skills, you can use generative AI (ChatGPT or GitHub Copilot) to assist you in completing the coding tasks.

There is a set of optional exercises in subdirectory that are a warm-up before the main challenge.

## Challenge

#### Find the Genome!

The elf scientists this year are working extremely hard. In fact, they are working so hard that they forgot its already 2025! 
They detected a new strain of bacteria. They have uploaded the file on NCBI but they are unsure which one to download.

Help the elves identify the correct genomic sequence! Visit the following link and figure out which file contains the actual genome, and which the genic annotations:

```
https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/014/646/915/GCF_014646915.1_ASM1464691v1
```

After you found out which genome is the correct one, download it. What is the name of this species?

If you do not remember how, you can visit today's presentation.

Bonus: Figure out how to install `datasets` command line interface of NCBI using `micromamba` and try to download the same genome using `datasets` commands. The command you have to find starts with:

`datasets download`

Try to google or ChatGPT your way if you are unsure how to proceed!

#### Read the FASTA file

Now that you have downloaded the genomic sequence and gene annotations, your next task is to find the total number of genes contained in the annotation file.

Try to create a new python script and use `biopython` module to read the fasta sequence that you just downloaded. 

First, make sure to install `biopython` using `pip`, python's package manager.

You can do this by running:

```
pip install biopython
```

Create a file named `read_genome.py` as follows:

```
from Bio import SeqIO

genome = ""
for record in SeqIO.parse(genome, 'fasta'):
    print(record.id, len(record.seq))
```

Sometimes there are bugs! These are part of the challenge.

To run your script, you need to run:

```
python read_genome.py
```

Try to answer the following questions:

- How many sequence ids (chromosomes and/or plasmids) does your fasta file contain?
- Which one is the largest sequence?
- Which sequence has the largest GC-content (normalized)?

Bonus: Try to adjust your script, so that you can provide the genome file from the command line as an argument. You will have to use the `sys` module.

#### Extract non B-DNA

Now it's the time to extract non B-DNA.

Try to use `non_b-gfa` and find the necessary flags to extract ONLY inverted repeats, short tandem repeats and Z-DNA, and skip the 
remaining secondary structures.

Your command will look as follows:

```
gfa -seq <YOUR_FASTA_FILE> -out <OUTPUT_NAME>
```

You need to fill in the missing flags.

Now repeat the command but this time we require that the hairpin spacer length must not exceed 10 base pairs. Which flag you have to use to achieve that?

After the command runs succesfully you will notice multiple files generated in your directory.

Which file contains the inverted repeat sequences?

#### Investigation of repeat sequences

Using bash commands, try to answer the following questions:

- How many inverted repeats you identified?
- How many short tandem repeats you identified?
- How many Z-DNA sequences you identified?
- Fetch the first inverted repeat you see. Which sequence corresponds to spacer and which to the arm?
- Try to answer the previous question for the longest inverted repeat present in the file.

You may find the following commands useful:

```
wc -l
head -1
awk 
```

#### Your final task!

Concatenate all the inverted repeat sequences into one huge DNA sequence. Of course this new sequence is just an artifact. 

Now write a python script to perform the following:

Replace the DNA nucleotides by numbers from 0 to 3 as follows:

```
A ➡️ 0
G ➡️ 1
C ➡️ -1
T ➡️ 1
```

Now, replace the artificial gigantic inverted repeat sequence with numbers, and find the sum. Which number do you find?

**Move to the final section only if you have finished everything!**

#### Final Challenge

Woah! You have reached this far. This is the true final question:

Use the annotation file and the inverted repeats and extract all the gene names that overlap with an at least one inverted repeat sequence.

You may want to use `bedtools` package after you install it with `micromamba`.


## Optional warm-up problems

#### First task
Learn how to print a phrase or variable

```
print(“hello”)
```
Use the + symbol to create new cells

Learn how to define and print variables

```
string_variable = "hello""
print(string_variable)
```

```
integer_variable = 20
print(integer_variable)
```

#### Second task

Learn how to write a for loop
The task is to print all integers from 1 to 10

First try:
```
for i in range(10):
    print(i)
```
Then:

```
for i in range(1, 11):
    print(i)
```

What are the differences?

#### Third task

Learning to use if statements. Print only even numbers between 1 and 10.

You can use modulo operator (%)

```
for i in range(1,11):
	if i%2==0:
    		print(i)
```

You could also use the step variable in range function!

```
for i in range(2, 11, 2):
	print(i)
```

#### Fourth task

Print every number from 1 to 10, but add text surrounding it indicating whether that number is odd or even. Learn if-else statements and string formatting

```
for i in range(1, 11):
	if i % 2:
    		print(f"{i} is an even number")
	else:
    		print(f"{i} is an odd number")
```

#### Fifth task: Creating a function

Print any input phrase

```
def phrase_printer(phrase):
	print(phrase)
```

Try:

```
phrase_printer("hello")
phrase_printer(“this is a function”)
```

Write a function that takes a list of number as input. For every even number it replaces it with its square, for every odd number it replaces it with its root. For non-integers it does nothing.

Hint: 
```
import math
math.sqrt(x)
```

Solution:
```
import math
def weird_function(my_list):
	for i in range(len(my_list)):
    		if my_list[i] % 2 == 0:
        		my_list[i] = my_list[i] ** 2
        	elif my_list[i] % 2 == 1:
            		my_list[i] = math.sqrt(my_list[i])
	return my_list  # Caution: This modified the list itself
```

#### Sixth task

Given a list of numbers 
```
[1, 2, 3, 10, 2, 3, 5]
```

try to find the length, maximum and minimum value and the total sum. Can you find how many times 3 occurs?
Create a function that calculates each of these quantities.

After you create this function, try to find an in-built function that sorts the list in reverse order.
