
def offByOne(a, b):
    """return true if b can be made by removing one character from a.
    assumes len(a) == len(b) + 1
    """
    ai = 0
    incd = False
    for c in b:
        if a[ai] == c:
            ai += 1
        elif incd:
            return False
        else:
            incd = True
            ai += 1
            if a[ai] == c:
                ai += 1
            else:
                return False
    return True


def longestChain(words):
    word_len = {}
    for word in words:
        l = len(word)
        if l in word_len:
            word_len[l].append({'word': word, 'chain': 1})
        else:
            word_len[l] = [{'word': word, 'chain': 1}]

    lens = word_len.keys()
    max_limit = 1
    cur_chain = 1
    prev = -2
    for l in sorted(lens):
        if l == prev + 1:
            cur_chain += 1
            if cur_chain > max_limit:
                max_limit = cur_chain
        else:
            cur_chain = 1
        prev = l
    cur = prev
    while cur > 0:
        if cur in word_len and cur - 1 in word_len:
            for word_dict in word_len[cur - 1]:
                matches = [wd for wd in word_len[cur] if offByOne(wd['word'], word_dict['word'])]
                if matches:
                    word_dict['chain'] += max([wd['chain'] for wd in matches])
                    if word_dict['chain'] == max_limit:
                        return max_limit
        cur -= 1
    return max([wd['chain'] for wds in word_len.values() for wd in wds])
