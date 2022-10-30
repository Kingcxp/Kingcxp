rank_list = {}

def getRank(group_id):
    try:
        tmp = str()
        tot = int(0)
        print(rank_list[group_id].items())
        rank = sorted(rank_list[group_id].items(), key = lambda x : x[1], reverse = True)
        for name, num in rank:
            tot += 1
            tmp = tmp + "第%d名 "%tot + name + " 胜场数：%d\n"%num
        return tmp
    except:
        return "这个群暂时还没有排名哦~"