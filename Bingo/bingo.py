import random 
st = ""
win = {
    "win_c": "computer",
    "win_p": "player"
}
winall = [win["win_c"],win["win_p"]]
comp_pattern = [[1,2,3,10,11],[4,5,6,12,13],[7,8,9,14,15],[16,17,18,19,20],[21,22,23,24,25]]
player_pattern = [[1,2,9,12,13],[7,8,3,10,11],[4,5,6,14,15],[16,17,18,19,20],[21,22,23,24,25]] 
sum_d = {
  "sum_c_d1" : 0,
  "sum_p_d1" : 0  
}
sum_h = {
  "sum_c_h1" : 0,
  "sum_c_h2" : 0,
  "sum_c_h3" : 0,
  "sum_p_h1" : 0,
  "sum_p_h2" : 0,
  "sum_p_h3" : 0
}
sum_v = {
  "sum_c_v1" : 0,
  "sum_c_v2" : 0,
  "sum_c_v3" : 0,
  "sum_p_v1" : 0,
  "sum_p_v2" : 0,
  "sum_p_v3" : 0
}
sum_c = [sum_d["sum_c_d1"],sum_h["sum_c_h1"],sum_h["sum_c_h2"], sum_h["sum_c_h3"], sum_v["sum_c_v1"], sum_v["sum_c_v2"], sum_v["sum_c_v3"]]
sum_p = [sum_d["sum_p_d1"],sum_h["sum_p_h1"],sum_h["sum_p_h2"], sum_h["sum_p_h3"], sum_v["sum_p_v1"], sum_v["sum_p_v2"], sum_v["sum_p_v3"]]

count = {
    "comp_count" : 0,
    "player_count" : 0
}
countall = [count["comp_count"],count["player_count"]]
def combine(choosed_number,pattern,sum,count,win):    
    print("=============================")
    for i in range (5):
        print(pattern[i])

    for i in range(5):
        for j in range(5):
            if pattern[i][j] == choosed_number:
                pattern[i][j] = 26
                if i==j:
                    sum[0] = sum[0] + pattern[i][j]
                if i==0: 
                    sum[1] = sum[1] + pattern[i][j]
                elif i==1:
                    sum[2] = sum[2] + pattern[i][j]      
                elif i==2:
                    sum[3] = sum[3] + pattern[i][j]
                if j==0:
                    sum[4] = sum[4] + pattern[i][j]
                elif j==1 :
                    sum[5] = sum[5] + pattern[i][j] 
                elif j==2:
                    sum[6] = sum[6] + pattern[i][j]
    print("=====================================") 
    for i in range (5):
        print(pattern[i])
    
    print("total sum is = ",sum)
    if (sum[0]==130) or (sum[1]==130) or (sum[2]==130) or (sum[3]==130) or (sum[4]==130) or (sum[5]==130) or (sum[6]==130):
        if not sum[0] - 130:
            count = count + 1
            sum[0] = 130
        if not sum[1] - 130:
            count = count + 1
            sum[1] = 130
        if not sum[2] - 130:
            count = count + 1
            sum[2] = 130
        if not sum[3] - 130:
            count = count + 1
            sum[3] = 130
        if not sum[4] - 130:
            count = count + 1
            sum[4] = 130
        if not sum[5] - 130:
            count = count + 1
            sum[5] = 130
        if not sum[6] - 130:
            count = count + 1
            sum[6] = 130
        if count == 1:
            st = "B"
            print(f'{win} : B')
        elif count == 2:
            st = "BI"
            print(f'{win} : BI')
        elif count == 3:
            st = "BIN"
            print(f'{win} : BIN')
            # return st
        elif count == 4:
            st = "BING"
            print(f'{win} : BING')
        elif count == 5:
            st = "BINGO"
            print(f"{win} : BINGO")
            return st
        elif count == 6:
            st = "BINGOO"
            print(f"{win} : BINGOO")
        elif count == 7:
            st = "BINGOOO"
            print("BINGOOO")
            print("winner is : ",win)
            
    print(count)

    print("=============================")
def bingo(comp_pattern,player_pattern,sum_c,sum_p,countall,winall):
    choices = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    player_name = input ("player name : ")
    print("computer Vs ",player_name)
    print("choices are: ",choices)
    k = 0
    l = 0
    while True:
        if l==0:
            comp_number = random.choice(choices)
            choices.remove(comp_number)
            print("computer choosed: ",comp_number)            
            print("Remaining choices are : ", choices)
            print("=============computer=============")
            Cwin = combine(comp_number,comp_pattern,sum_c,countall[0],winall[0])
            print("=============player===============")
            Pwin = combine(comp_number,player_pattern,sum_p,countall[1],winall[1])
            if Cwin == "BINGO":
                print("computer won")
                break
            if Pwin == "BINGO":
                print(f"{player_name} won")
                break
            l=1
        else:
            player_number = int(input("your choice: "))
            choices.remove(player_number)
            print("human choosed: ", player_number)
            print("Remaining choices are : ", choices)
            print("=============player===============")
            Pwin = combine(player_number,player_pattern,sum_p,countall[1],winall[0])
            print("=============computer=============")
            Cwin = combine(player_number,comp_pattern,sum_c,countall[0],winall[1])
            if Pwin == "BINGO":
                print(f"{player_name} won")
                break
            if Cwin == "BINGO":
                print("computer won")
                break
            l=0
        if choices == []:
            print("No Remaining Choices Are There: ",choices)
            break

bingo(comp_pattern,player_pattern,sum_c,sum_p,countall,winall)
