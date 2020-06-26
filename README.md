# Protein Visualizer
Protein Visualizer that shows how proteins look and converts the amino acid sequence into a DNA sequence. 

Program Flow:
- The program asks for a protein from the user.
- Searches the NCBI Protein database for that search quiry and displays top 20 results. 
- The user may choose a protein from one of those results. 
- The program will then do two things:
  1. Create a .pdb file for that protein and open that file with a software like UCSF Chimera or PyMol. 
  2. Convert that amino acid sequence into a DNA sequence while choosing codons arbitrarily and display the number of nucleotides in the DNA sequence and also display the GC Ratio of the DNA sequence. 
  
Note: It may take 2-5 minutes for the program to make the "BLAST" which is essentialy the model of the protein. The program stores that info in XML and PDB files so that when you try and visualize the same protein again it just directly accesses those files rather than regenerating that "BLAST" again and thus saving time. 

# Demo Video
Click on picture to see video

[![Alt text](https://img.youtube.com/vi/MHKekgioHR0/0.jpg)](https://www.youtube.com/watch?v=MHKekgioHR0)

# Dependencies
1. Python 3.6 or above.
    - Can be downloaded from https://www.python.org/downloads/
2. Requests module
  - Terminal command to download: ```pip install requests```
3. Beautiful soup module
  - Terminal command to download: ```pip install beautifulsoup4```
4. BioPython module
  - Terminal command to download: ```pip install biopython```
