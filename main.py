import logging
import re
import sys
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

NUMBER_WORDS = 25


def corpus_cleanup(file):
    f = open(file)
    contents = f.read()
    contents = contents.lower()
    contents = re.sub("-", " ", contents)
    contents = re.sub("[^a-záàâãéèêíïóôõöúçñ ]", "", contents)
    contents = re.sub("\n", " ", contents)
    contents = re.sub(" {2,}", " ", contents)

    return contents


def plot_histogram(list_to_plot, title, filename):
    labels, values = zip(*list_to_plot)

    # sort your values in descending order
    indSort = np.argsort(values)[::-1]

    # rearrange your data
    labels = np.array(labels)[indSort]
    values = np.array(values)[indSort]

    indexes = np.arange(len(labels))

    bar_width = 0.35

    plt.bar(indexes, values)

    # add labels
    plt.xticks(indexes + bar_width, labels, rotation=90)
    plt.title(title)
    # plt.show()
    plt.savefig("./images/" + filename)


def prefix_suffix_list(words_to_count, char_size, is_prefix):
    frequency_list = []
    for word in words_to_count:
        if is_prefix:
            if len(word[:char_size]) == char_size:
                frequency_list.append(word[:char_size])
        else:
            if len(word[char_size:]) == char_size:
                frequency_list.append(word[char_size:])

    return frequency_list


logging.basicConfig(stream=sys.stderr, level=logging.INFO)

corpus = corpus_cleanup("./data/corpus.txt")
logging.debug(corpus)

wordlist = corpus.split()
logging.debug(wordlist)
logging.info("Total de palavras: " + str(len(wordlist)))

wordlist_unique = list(dict.fromkeys(wordlist))
logging.debug(wordlist_unique)
logging.info("Total de palavras únicas: " + str(len(wordlist_unique)))

# words_counter = Counter(wordlist)
most_common_words = Counter(wordlist).most_common()
logging.info(most_common_words[:NUMBER_WORDS])
plot_histogram(most_common_words[:NUMBER_WORDS], "Histograma das 25 palavras mais frequentes", "frequent_words.png")

# PREFIX
suffix_1_list = prefix_suffix_list(wordlist, 1, True)
suffix_1_count = Counter(suffix_1_list).most_common(NUMBER_WORDS)
plot_histogram(suffix_1_count, "Prefixo: 1 - Top 25", "prefix_1.png")
logging.info(suffix_1_count)

suffix_2_list = prefix_suffix_list(wordlist, 2, True)
suffix_2_count = Counter(suffix_2_list).most_common(NUMBER_WORDS)
plot_histogram(suffix_2_count, "Prefixo: 2 - Top 25", "prefix_2.png")
logging.info(suffix_2_count)

suffix_3_list = prefix_suffix_list(wordlist, 3, True)
suffix_3_count = Counter(suffix_3_list).most_common(NUMBER_WORDS)
plot_histogram(suffix_3_count, "Prefixo: 3 - Top 25", "prefix_3.png")
logging.info(suffix_3_count)

suffix_4_list = prefix_suffix_list(wordlist, 4, True)
suffix_4_count = Counter(suffix_4_list).most_common(NUMBER_WORDS)
plot_histogram(suffix_4_count, "Prefixo: 4 - Top 25", "prefix_4.png")
logging.info(suffix_4_count)

suffix_5_list = prefix_suffix_list(wordlist, 5, True)
suffix_5_count = Counter(suffix_5_list).most_common(NUMBER_WORDS)
plot_histogram(suffix_5_count, "Prefixo: 5 - Top 25", "prefix_5.png")
logging.info(suffix_5_count)

# SUFFIX
suffix_1_list = prefix_suffix_list(wordlist, 1, False)
suffix_1_count = Counter(suffix_1_list).most_common(NUMBER_WORDS)
plot_histogram(suffix_1_count, "Sufixo: 1 - Top 25", "suffix_1.png")
logging.info(suffix_1_count)

suffix_2_list = prefix_suffix_list(wordlist, 2, False)
suffix_2_count = Counter(suffix_2_list).most_common(NUMBER_WORDS)
plot_histogram(suffix_2_count, "Sufixo: 2 - Top 25", "suffix_2.png")
logging.info(suffix_2_count)

suffix_3_list = prefix_suffix_list(wordlist, 3, False)
suffix_3_count = Counter(suffix_3_list).most_common(NUMBER_WORDS)
plot_histogram(suffix_3_count, "Sufixo: 3 - Top 25", "suffix_3.png")
logging.info(suffix_3_count)

suffix_4_list = prefix_suffix_list(wordlist, 4, False)
suffix_4_count = Counter(suffix_4_list).most_common(NUMBER_WORDS)
plot_histogram(suffix_4_count, "Sufixo: 4 - Top 25", "suffix_4.png")
logging.info(suffix_4_count)

suffix_5_list = prefix_suffix_list(wordlist, 5, False)
suffix_5_count = Counter(suffix_5_list).most_common(NUMBER_WORDS)
plot_histogram(suffix_5_count, "Sufixo: 5 - Top 25", "suffix_5.png")
logging.info(suffix_5_count)
