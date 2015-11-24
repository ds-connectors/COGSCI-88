import matplotlib.pyplot as plt
import re
import numpy as np

novelfile = "ulysses.txt";

# Starter code that extracts words and frequencies from "ulysses.txt" from Project Gutenberg
#############################################################################################
word_dict = {}

with open(novelfile) as f:
    for line in f:
        words = line.strip().split(' ')
        for word in words:
            word = re.sub('^[\W\.\d_]+|[\W\.\d_]+$', '', word).lower()
            if len(word) == 0:
                continue
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
#############################################################################################

numshow = 10000;

# Sort words based on frequency (or count)
count_tuple_list = [(count, word) for word, count in word_dict.items()]
count_tuple_list.sort(reverse=True)

# Obtain sorted frequencies, ranks, and corresponding word lengths
count = [i[0] for i in count_tuple_list]
rank = range(1, len(count_tuple_list) + 1)
words = [i[1] for i in count_tuple_list]
wlen = [len(i) for i in words]

# Figure 1 - Visualize raw frequency vs rank for the most common 100 words in the novel
fig = plt.figure()
plt.plot(rank[0:99],count[0:99],'bo--')
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.title('Frequency vs. Rank (Top 100 words)')

# Figure 2 - Visualize raw frequency vs rank for the most common 10000 words in the novel
fig = plt.figure()
plt.plot(rank[0:numshow],count[0:numshow],'bo--')
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.title('Frequency vs. Rank')

# Figure 3 - Visualize log(frequency) vs log(rank) for the most common 10000 words in the novel
fig = plt.figure()
plt.loglog(rank[0:numshow],count[0:numshow],'bo--')
plt.xlabel('Log-rank')
plt.ylabel('Log-frequency')
plt.title('Log-frequency vs. Log-rank')

# Figure 4 - Visualize log(frequency) vs form length for the most common 10000 words in the novel
fig = plt.figure()
plt.plot(np.log(count[0:numshow]),wlen[0:numshow],'bo')
plt.xlabel('Log-frequency')
plt.ylabel('Word length')
plt.title('Word length vs. Log-frequency')

plt.show()

# Print (count,word) pairs for the most common 20 words in the novel
for i in range(1, 20):
    print(count_tuple_list[i])


