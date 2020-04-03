# This program was a problem in Google's Round A 2020 Kick Start
# T is the number of test cases. A is the list of home costs. N are
# the total numbers of homes for sale. B is the budget. THe program
# gets the required info, sorts the list, then determines how many
# homes can be bought. The Kick Start required no additional prompts
# for a user.

T = int(input())
case = 1
while case <= T:
    A = []
    N, B = [int(x) for x in input().split()]
    while len(A) != N:
        A = [int(x) for x in input().split()]
    A.sort()
    temp, i, count = 0,0,0
    while temp < B and i <= len(A) - 1:
        if temp + A[i] <= B:
            temp += A[i]
            count += 1
            i += 1
        else:
            i += len(A)
    print("Case #", case, ": ", count, sep="")
    case += 1
