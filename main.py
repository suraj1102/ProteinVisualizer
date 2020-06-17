from blast import *
from protein_scraper import *

def main():
    WebScraper = WebScraper()
    WebScraper.get_search_items()
    WebScraper.get_protein_sequence()

    Blast = Blast(WebScraper.protein_id)
    Blast.make_blast()
    Blast.readxml()

if __name__ == '__main__':
    main()
