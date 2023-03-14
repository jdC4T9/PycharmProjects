# file input.txt contains numbers separated by a comma as shown below,
# 6 ,8
# 7 ,6
# 2 ,8
# 9 ,5
# 9 ,6

# with open("c:\\users\\jd mamangun\\pycharmprojects\\pythonProject-JSON\\input.txt","w") as input:
#     input.write("6 ,8\n")
#     input.write("7 ,6\n")
#     input.write("2 ,8\n")
#     input.write("9 ,5\n")
#     input.write("9 ,6\n")
#

# (1)
# def countNum(num):
#     total=0
#     with open("c:\\users\\jd mamangun\\pycharmprojects\\pythonProject-JSON\\input.txt", "r") as input:
#         for line in input:
#             n=line.split(",")
#             for i in n:
#                 i=int(i)
#                 if num==i:
#                      total=total+1
#                 else:
#                     continue
#     return(total)
#
#
# print(countNum(9))


# (2)

with open("c:\\users\\jd mamangun\\pycharmprojects\\pythonProject-JSON\\input.txt", "r") as input:
    for line in input:
        total = 0
        n = line.split(",")
        for i in n:
            i = int(i)
            total=total+i
        print(total)

        with open("c:\\users\\jd mamangun\\pycharmprojects\\pythonProject-JSON\\input-sum.txt", "a") as inputSum:
             inputSum.write("sum: " + str(total) + " | " + line)
