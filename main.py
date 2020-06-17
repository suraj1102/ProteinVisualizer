import protein_scraper
import blast
import seq_tools

def main():
    # Web scraping to get amino acid sequence
    WebScraper = protein_scraper.WebScraper()
    WebScraper.get_search_items()
    WebScraper.get_protein_sequence()

    # Creating the BLAST (Visualization)
    Blast = blast.Blast(WebScraper.protein_id)
    Blast.make_blast()
    Blast.readxml()

    # Converting amino acid sequence to DNA sequence and displaying nucleotide data
    SeqTools = seq_tools.SeqTools(WebScraper.protein_id)
    print(SeqTools.read_seq())
    print(SeqTools.protein_to_dna())
    print(SeqTools.nucleotide_values())

if __name__ == '__main__':
    main()
