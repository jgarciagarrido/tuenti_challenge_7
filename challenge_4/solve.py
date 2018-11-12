def is_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (a + c > b)


def perimeter(triangle):
    return triangle[0] + triangle[1] + triangle[2]


def min_perimeter_triangle(n, sides):
    sides.sort()
    triangle = None
    for i in xrange(1, n-1):
        b = sides[i]
        c = sides[i+1]
        for j in xrange(0, i):
            a = sides[j]
            if is_triangle(a, b, c):
                return perimeter((a, b, c))
    return "IMPOSSIBLE"

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        sides_line = [int(s) for s in raw_input().split(" ")]
        n_sides = sides_line[0]
        sides = sides_line[1:]
        print "Case #{}: {}".format(i, min_perimeter_triangle(n_sides, sides))
