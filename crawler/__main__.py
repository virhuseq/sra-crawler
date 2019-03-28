from Bio import Entrez
from fire import Fire


def search_sra(query, email="dummy@domain.com"):
    Entrez.email = email
    handle = Entrez.esearch(
        db="sra", sort="relevance", retmax="20", retmode="json", term=query
    )
    results = Entrez.read(handle)
    return results


def main(query):
    print(search_sra(query))


if __name__ == "__main__":
    Fire(main)
