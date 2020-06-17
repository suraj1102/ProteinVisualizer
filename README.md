# Protein Visualizer
Protein Visualizer that shows how proteins look and converts the amino acid sequence into a DNA sequence. 

Program Flow:
- The program asks for a protein from the user.
- Searches the NCBI Protein database for that search quiry and displays top 20 results. 
- The user may choose a protein from one of those results. 
- The program will then do two things:
  1. Create a .pdb file for that protein and open that file if you have a software like UCSF Chimera installed. 
  2. Convert that amino acid sequence into a DNA sequence while choosing codons arbitrarily and display the number of nucleotides in the DNA sequence and also display the GC Ratio of the DNA sequence. 
