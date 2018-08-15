from Text_Processor import probability_manager  #some what edited
from nltk.tokenize import TweetTokenizer

uni_bigramvalues = probability_manager.activities()
tokenizer = TweetTokenizer()

fdist_ham = uni_bigramvalues[0]
fdist_spam = uni_bigramvalues[1]
bigrams_ham = uni_bigramvalues[2]
bigrams_spam = uni_bigramvalues[3]

#calculate bigrams in the corpus
def find_bigrams_in_corpus(tklist):  #find_bigrams
    bigrams = list(())
    pr = None
    for tk in tklist:
        if pr is not None:
            bigrams.append((pr, tk))
        pr = tk
    return bigrams

#calculate probability values in the corpus
def cal_probability_values_corpus(new_tokens, fdist, bigrams): #calculate_probabilities
    pv = list(())
    for t in new_tokens:
        a = t[0].lower()
        b = t[1].lower()
        uni_count = fdist[a]
        bi_count = bigrams[a, b]
        pv.append((uni_count, bi_count, (bi_count + 1) / (uni_count + len(fdist))))
    return pv

#calculate final probability values in the corpus
def calculate_final_probability(probability_values):
    final = 1
    for p in probability_values:
        final *= p[2]
    return final


def find_type():
    msg = input()
    msg_tokens = tokenizer.tokenize(msg)

    bigrams_msg = find_bigrams_in_corpus(msg_tokens)


    ham_corpus_probability_values =cal_probability_values_corpus(bigrams_msg, fdist_ham, bigrams_ham)
    spam_corpus_probability_values = cal_probability_values_corpus(bigrams_msg, fdist_spam, bigrams_spam)

    print( ham_corpus_probability_values)
    print(spam_corpus_probability_values)

    final_probability_in_ham = calculate_final_probability(ham_corpus_probability_values)
    final_probability_in_spam = calculate_final_probability(spam_corpus_probability_values)

    print("Ham Probability values :", format(final_probability_in_ham, '.12g'))
    print("Spam Probability values: ", format(final_probability_in_spam, '.12g'))



    if final_probability_in_ham >= final_probability_in_spam:
        print("Ham")
    else:
        print("Spam")


if __name__ == '__main__':
    find_type()
