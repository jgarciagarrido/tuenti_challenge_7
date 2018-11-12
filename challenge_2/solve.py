def score_per_frame(start_at, pins_knocked):
    score = pins_knocked[start_at]
    next_frame = start_at + 1
    if pins_knocked[start_at] == 10:
        score += pins_knocked[start_at+1] + pins_knocked[start_at+2]
    elif (pins_knocked[start_at] + pins_knocked[start_at+1]) == 10:
        score += pins_knocked[start_at+1] + pins_knocked[start_at+2]
        next_frame += 1
    else:
        score += pins_knocked[start_at+1]
        next_frame += 1
    return score, next_frame

def game_score(pins_knocked):
    next_frame = 0
    frame_score = []
    total = 0
    for frame in xrange(1, 11):
        score, next_frame = score_per_frame(next_frame, pins_knocked)
        total += score
        frame_score.append(total)
    return " ".join(map(str,frame_score))

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        rolls = int(raw_input())
        pins_knocked = [int(s) for s in raw_input().split(" ")]
        frame_score = game_score(pins_knocked)
        print "Case #{}: {}".format(i, frame_score)
