x1 = 1
y1 = 1

x2 = 9
y2 = 9

sub_x = x1 - x2
sub_y = y1 - y2

if -1 <= x1-x2 <= 1 and -1 <= y1-y2 <= 1 or x1 == x2 or y1 == y2:
    print(1)
elif sub_x == sub_y or -sub_x == sub_y or sub_x == -sub_y:
    print(1)
else:
    print(0)