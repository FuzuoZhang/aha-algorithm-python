import numpy as np

def find_optimal_site(themap):
    n,m=len(themap), len(themap[0])
    maxtarget = 0
    opt_i = -1
    opt_j = -1
    print(n,m)
    for i in range(1,n-1):
        for j in range(1,m-1):
            if themap[i][j]!='.':
                continue
            tmp_total = 0
            #向上搜索
            x = i-1
            while themap[x][j]!="#":
                if themap[x][j]=="G":
                    tmp_total +=1
                x-=1
            #向下搜索
            x = i+1
            while themap[x][j]!="#":
                if themap[x][j]=="G":
                    tmp_total +=1
                x+=1
            #向左搜索
            y = j-1
            while themap[i][y]!="#":
                if themap[i][y]=="G":
                    tmp_total +=1
                y-=1
            #向右搜索
            y=j+1
            while themap[i][y]!="#":
                if themap[i][y]=="G":
                    tmp_total+=1
                y+=1
            if tmp_total>maxtarget:
                maxtarget=tmp_total
                opt_i=i
                opt_j=j

    print("放置炸弹的最佳位置为：(%d,%d)" %(opt_i,opt_j))
    print("可炸死的敌人个数为：%d" %maxtarget)   

if __name__ == "__main__":
    themap = [
        "#############",
        "#GG.GGG#GGG.#",
        "###.#G#G#G#G#",
        "#.......#..G#",
        "#G#.###.#G#G#",
        "#GG.GGG.#.GG#",
        "#G#.#G#.#.###",
        "##G...G.....#",
        "#G#.#G###.#G#",
        "#...G#GGG.GG#",
        "#G#.#G#G#.#G#",
        "#GG.GGG#G.GG#",
        "#############"
        ]
    #themap = ["####","#.GG#","#G..#","####"]
    find_optimal_site(themap)
            