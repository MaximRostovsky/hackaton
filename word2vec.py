import numpy as np
from tqdm import tqdm
import gensim


def load_vectors(file_name, remove_tags=False, n=None):
    words = dict()

    with open(file_name, "rb") as f:

        total = int(f.readline().strip().split()[0])
        if n is not None:
            total = min(total, n)

        for i, line in enumerate(tqdm(f, total=total)):

            if n is not None and n == i:
                break

            word, space, vector = line.partition(" ")

            if remove_tags:
                word = word.split("_")[0]

            words[word] = np.fromstring(vector, sep=" ")

    return words


if __name__ == "__main__":
    model = gensim.models.KeyedVectors.load_word2vec_format(
        "web_mystem_skipgram_500_2_2015.bin", binary=True)
    model.init_sims(replace=True)
    model