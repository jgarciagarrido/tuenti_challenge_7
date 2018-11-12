def min_pizzas_needed(slices):
    slices_needed = reduce(lambda x,y: x+y, slices, 0)
    pizzas_needed = slices_needed / 8
    if slices_needed % 8 != 0:
        pizzas_needed += 1
    return pizzas_needed

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n = int(raw_input())
        slices = [int(s) for s in raw_input().split(" ")]
        print "Case #{}: {}".format(i, min_pizzas_needed(slices))
