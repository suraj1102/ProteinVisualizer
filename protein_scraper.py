import requests, os
from bs4 import BeautifulSoup
from Bio import Entrez, SeqIO
from sys import exit

class WebScraper():
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
        }

    def get_search_items(self):
        self.protein = input("\nEnter Protein: ")
        
        if self.protein.strip() == 'quit':
            exit()

        page = requests.get(f"https://www.ncbi.nlm.nih.gov/protein/?term={self.protein.strip()}", headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        self.url_links = []
        self.protein_names = []

        print()
        i = 1
        for element in soup.find_all("p", class_='title'):
            url = element.find('a')['href']
            self.url_links.append(url)
            self.protein_names.append(element.text)
            print(f"{i}: {element.text}")
            i += 1

        if len(self.url_links) == 0:
            print("NO RESULTS FOUND")
            self.get_search_items()
    
    def get_protein_sequence(self):
        try:
            global index
            index = int(input("\nEnter Number: "))
            if index == 'quit':
                exit()
        except: 
            print("ENTER VALID INPUT")
            self.get_protein_sequence()
            
        try:
            self.protein_id = self.url_links[index-1].split('/')[2]
            self.protein_name = self.protein_names[index-1]

            Entrez.email = "suraj.dayma11@gmail.com"
            handle = Entrez.efetch(db = 'protein', id = self.protein_id, rettype="fasta", retmode="text")
            records = handle.read()

            with open(f'{os.getcwd()}/FastaFiles/{self.protein_id}.fasta', 'w') as f:
                f.write(records)

            with open(f'FastaFiles/{self.protein_id}.fasta', 'r') as f:
                f_lines = f.readlines()
                seq = ''.join(f_lines[1:]).replace('\n', '').replace('\r', '')
                records = f"{f_lines[0]}{seq}"

            with open(f'FastaFiles/{self.protein_id}.fasta', 'w') as f:
                f.write(records)

            print(f"\nSEQUENCE DOWNLOADED\n protein id: {self.protein_id}")

            handle.close()

        except (IndexError, ValueError):
            print("ENTER VALID INPUT")
            self.get_protein_sequence()
        
# WebScraper = WebScraper()
# WebScraper.get_search_items()
# WebScraper.get_protein_sequence()
