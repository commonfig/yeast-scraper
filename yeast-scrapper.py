import requests
import pprint
from bs4 import BeautifulSoup

gene_ids_input = input("Enter a list of gene IDs (separated by spaces): ")
gene_ids = gene_ids_input.split()
print(gene_ids)
def scrape_phenotype(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    phenotype_section = soup.find('section', id='phenotype') #change according to which section you want to find information under
    if phenotype_section:
        phenotype_text = phenotype_section.get_text()
        return phenotype_text.strip()
gene_list = []
def listing(mygenes):
    for gene in mygenes:
        phenotype = scrape_phenotype("https://www.yeastgenome.org/locus/" + gene)
        if 'lifespan' in phenotype or 'oxidative stress' in phenotype: #change according to what phenotype you want to find
            gene_list.append(f"Lifespan/oxidative stress affected for gene ID {gene}")
        else:
            gene_list.append(f"No effect found for gene ID {gene}")
    return gene_list

result = listing(gene_ids) #Effects

for i, effect in enumerate(result, 1):
    print(f"Phenotype {i}: {effect}")





