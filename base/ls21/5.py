def heal(hl, player=3):
    if hl % player == 0:
        print(0)
    else:
        # print(((hl//player+1)*player)-hl)
        print(player-hl%player)
        # c = 0
        # while hl % player != 0:
        #     hl += 1
        #     c += 1
        # print(c)


heal(12)



