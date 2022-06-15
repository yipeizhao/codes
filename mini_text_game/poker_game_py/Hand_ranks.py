import collections
nums_dict={
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14
}
nums_dict_inv = {v:k for k,v in nums_dict.items()}

def hand_ranks(cards):
    res = ""; straight = False; flush = False
    # First item is suit
    suits = [item[0] for item in cards]
    # Second item is the number
    nums = [item[1:] for item in cards]
    nums_encode = [nums_dict[item] for item in nums]
    
    # if cards only have 1 suit
    if len(set(suits)) == 1:
        flush = True
        res = "Flush"
    # If sum of the cards is equal to the arithmetic progression
    if set(nums_encode) == set(range(min(nums_encode),max(nums_encode)+1)):
        straight  = True
        res = "Straight"
    if flush & straight:
        res = "Straight flush"
    if flush|straight:
        return res + ", " + nums_dict_inv[max(nums_encode)] + " high"
    
    # Determine the pairness of the cards
    counter = dict(collections.Counter(nums))
    counter_inv = {v:k for k,v in counter.items()}
    if max(counter.values()) == 4:
        return "Four of a kind, " + counter_inv[4]
    
    elif max(counter.values()) == 3:
        if min(counter.values()) == 2:
            return "Full house, three of a kind of " + counter_inv[3] + ", and a pair of " + counter_inv[2]
        elif min(counter.values()) == 1:
            return "Three of a kind of " + counter_inv[3]
        
    elif max(counter.values()) == 2:
        pairs = []
        # Collect all pairs
        for item in counter.keys():
            if counter[item] == 2:
                pairs.append(item)
        # If there is only one pair
        pairs = [nums_dict[item] for item in pairs]
        if len(pairs) == 1:
            return "One pair, " + counter_inv[2]
        elif len(pairs) == 2:
            return "Two pair, high pair " + str(sorted(pairs)[1]) +", low pair " + str(sorted(pairs)[0])
        
    elif max(counter.values()) == 1:
        return "High card, " + nums_dict_inv[max(nums_encode)]
    
    else:
        Exception("Ops, something went wrong in hands ranking.")
        
test = hand_ranks(["H7","S8","C10","D9","S6"])