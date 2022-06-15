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
nums_dict_rev = {v:k for k,v in nums_dict.items()}

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
    if (min(nums_encode)+max(nums_encode))*2.5 == sum(nums_encode):
        straight  = True
        res = "Straight"
    if flush & straight:
        res = "Straight flush"
    if flush|straight:
        return res + ", " + nums_dict_rev[max(nums_encode)] + " high"
    
    