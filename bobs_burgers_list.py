# List practice

# insert 'teddy' after 'louise'
# remove 'linda'
# get the index for 'bob', and then remove 'bob' using that index
# count the occurrences of 'gene'

def main():
    reviewList = ['tina', 'bob', 'gene', 'louise', 'gene', 'linda']

    reviewList.insert(4, 'teddy')
    
    reviewList.remove('linda')

    bob_idx = reviewList.index('bob')
    del reviewList[bob_idx]

    gene_count = reviewList.count('gene')

    print(reviewList, f'\nGene Count: {gene_count}')

main()