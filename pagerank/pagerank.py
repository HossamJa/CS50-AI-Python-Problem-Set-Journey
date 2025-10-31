import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    probabilities = dict()
    total_pages = len(corpus)
    links = corpus[page]

    # If the page has outgoing links
    if links:
        # Calculate probabilities
        link_prob = damping_factor / len(links)
        random_prob = (1 - damping_factor) / total_pages

        # Assign probabilities
        for p in corpus:
            probabilities[p] = random_prob
        for link in links:
            probabilities[link] += link_prob
    else:
        for p in corpus:
            probabilities[p] = 1 / total_pages
    return probabilities


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    
    page_counts = {page: 0 for page in corpus}
    # Start with a random page
    current_page = random.choice(list(corpus.keys()))
    for _ in range(n):
        page_counts[current_page] += 1
        probabilities = transition_model(corpus, current_page, damping_factor)
        current_page = random.choices(
            population=list(probabilities.keys()),
            weights=list(probabilities.values()),
            k=1
        )[0]
    # Normalize counts to get probabilities
    pagerank = {page: count / n for page, count in page_counts.items()}
    return pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    total_pages = len(corpus)
    pagerank = {page: 1 / total_pages for page in corpus}
    convergence_threshold = 0.001
    converged = False

    while not converged:
        new_pagerank = dict()
        converged = True
        
        for page in corpus:
            rank_sum = 0
            for possible_page in corpus:
                if page in corpus[possible_page]:
                    rank_sum += pagerank[possible_page] / len(corpus[possible_page])
                if not corpus[possible_page]:
                    rank_sum += pagerank[possible_page] / total_pages

            new_rank = (1 - damping_factor) / total_pages + damping_factor * rank_sum
            new_pagerank[page] = new_rank

            if abs(new_rank - pagerank[page]) > convergence_threshold:
                converged = False

        pagerank = new_pagerank

    return pagerank


if __name__ == "__main__":
    main()
