file = open('test 2', 'r')
lines = file.readlines()
file.close()

def compare(set_hand, test_hand):
    set_hand_numbers = [numberify[i] for i in set_hand]
    test_hand_numbers = [numberify[i] for i in test_hand]
    for i in range(len(set_hand_numbers)):
        if set_hand_numbers[i] > test_hand_numbers[i]:
            return 1
        elif set_hand_numbers[i] < test_hand_numbers[i]:
            return 0
        
    return 0


hands = []
for line in lines:
    hands.append([line.strip().split(' ')[0], int(line.strip().split(' ')[1])])

numberify = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

for hand in range(len(hands)):
    sorted_hand = ""
    for i in order:
        for _ in range(hands[hand][0].count(i)):
            sorted_hand += i

    hands[hand][0] = sorted_hand

hands_sorted = []
hands_sorted.append(hands[0])
del hands[0]
# sort the hands based on the first card
for i in range(len(hands)):
    for j in range(len(hands_sorted)):
        place = compare(hands_sorted[j][0], hands[i][0])
        if place == 0:
            hands_sorted.insert(j, hands[i])
            break    
    else:
        hands_sorted.append(hands[i])

high_card = []
one_pair = []
two_pair = []
three_of_a_kind = []
full_house = []
four_of_a_kind = []
five_of_a_kind = []


# sort the hands into their respected lists. 
for i in hands_sorted:
    count = 0
    for j in i[0]:
        count += i[0].count(j)

    if count == 25:
        five_of_a_kind.append(i)
    
    elif count == 17:
        four_of_a_kind.append(i)
        
    elif count == 13:
        full_house.append(i)

    elif count == 11:
        three_of_a_kind.append(i)
        
    elif count == 9:
        two_pair.append(i)
        
    elif count == 7:
        one_pair.append(i)
        
    elif count == 5:
        high_card.append(i)

    




together = five_of_a_kind + four_of_a_kind + full_house + three_of_a_kind + two_pair + one_pair + high_card
print(together)
together.reverse()

num = 0

for i in range(len(together)):
    num += together[i][1] * (i+1)

print(num)
