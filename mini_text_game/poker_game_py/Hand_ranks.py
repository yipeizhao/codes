import collections
# Giving the rank of each card
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
# Reverse nums_dict, val become key, key become val
nums_dict_inv = {v:k for k,v in nums_dict.items()}

# Rank of each hand situation, higher the int, better the hand
rank_dict = {"Straight flush":9,
              "Four of a kind":8,
              "Full house":7,
              "Flush":6,
              "Straight":5,
              "Three of a kind":4,
              "Two pair":3,
              "Pair":2,
              "High card":1}

# find the key by the given value
def key_by_val(v,d):
    res = [key for key, val in d.items() if val == v]
    return res if len(res)!=1 else res[0]


# Return the hand rank
# Para:
    # cards, list
# Return:
    # List
    # list[0] = Name of the rank
    # list[1] = Ranking of the hand, in int, higher the int, better the hand
    # list[2] = int, number of the highest rank in hand
    # list[3] = int, number of the second highest rank in hand
    # list[4] = list, rest of the hand
def hand_ranks(cards):
    res = ""; straight = False; flush = False
    # First item is suit
    suits = [item[0] for item in cards]
    # Second item is the number
    nums = [item[1:] for item in cards]
    nums = sorted([nums_dict[item] for item in nums])
    nums.reverse()
    # if cards only have 1 suit
    if len(set(suits)) == 1:
        flush = True
        res = "Flush"
    # If sum of the cards is equal to the arithmetic progression
    if nums == list(range(max(nums),min(nums)-1,-1)):
        straight  = True
        res = "Straight"
    if flush & straight:
        res = "Straight flush"
        res = [rank_dict[res],nums[0],nums[1],[],res]
        return res
    elif flush:
        res = [rank_dict[res],0,0,nums,res]
        return res
    elif straight:
        res = [rank_dict[res],nums[0],nums[1],[],res]
        return res
    
    # Determine the pairness of the cards
    counter = dict(collections.Counter(nums))
    
    if max(counter.values()) == 4:
        res = "Four of a kind"
        res = [rank_dict[res],key_by_val(4,counter),0,key_by_val(1, counter),res]
        
    elif max(counter.values()) == 3:
        if min(counter.values()) == 2:
            res = "Full house"
            res = [rank_dict[res],key_by_val(3,counter),key_by_val(2,counter),[],res]
        elif min(counter.values()) == 1:
            res = "Three of a kind"
            # list[3] = max of the high card
            # list[4] = min of the high card
            res = [rank_dict[res],key_by_val(3,counter),0,sorted(key_by_val(1, counter)),res]
            
    elif max(counter.values()) == 2:
        pairs = []
        # Collect all pairs
        for item in counter.keys():
            if counter[item] == 2:
                pairs.append(item)
        # If there is only one pair
        if len(pairs) == 1:
            res = "Pair"
            res = [rank_dict[res],key_by_val(2,counter),0,key_by_val(1, counter),res]
        elif len(pairs) == 2:
            res= "Two pair"
            res = [rank_dict[res],max(key_by_val(2,counter)),min(key_by_val(2,counter)),[key_by_val(1,counter)],res]
        
    elif max(counter.values()) == 1:
        res = "High card"
        res = [rank_dict[res],0,0,nums,res]
    
    else:
        Exception("Ops, something went wrong in hands ranking.")
    
    return res

# Quick sort algorithm
# Para:
    # arr, list
# Return:
    # List
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [item for item in arr[1:] if item <= pivot]
    right = [item for item in arr[1:] if item > pivot]
    return quick_sort(right) + [pivot] + quick_sort(left)

# Retur a sorted player list depending on their rank
# Para:
    # players_arr, list
# Return:
    # List
def sort_hand(players_arr):
    # Get the hand rank for all players
    hand_array = [p.get_hand_rank() for p in players_arr]
    # Sort the hand ranks
    hand_array = quick_sort(hand_array)
    # Sort the players according to the hand rank
    # Using double pointer to associate rank with playerss
    rank = []
    for i in range(len(hand_array)):
        for p in players_arr:
            if hand_array[i] == p.get_hand_rank():
                rank.append(p)
    return rank