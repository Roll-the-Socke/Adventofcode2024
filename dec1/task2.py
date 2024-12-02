frst = []
snd = []
final_sim = 0



with open("input2.txt") as i:
    input = i.read().split()
    content = list(map(int, input))
    for num in content[::2]:
        frst.append(num)
    for num in content[1::2]:
        snd.append(num)

    print (frst)
    print(snd)

    for i in range(len(frst)):
        count = snd.count(frst[i])
        sim_score = frst[i] * count
        final_sim += sim_score
    print(final_sim)

