def cards_needed(points):
    score = 1
    cards = 1
    point_cards = 1
    while (score < points):
        point_cards += point_cards
        cards += 1
        score += point_cards
    return cards

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        max_points = int(raw_input())
        cards = cards_needed(max_points)
        print "Case #{}: {}".format(i, cards)
