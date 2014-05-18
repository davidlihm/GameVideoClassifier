#-*- coding:utf-8 -*
from __future__ import division# -
import sqlite
import segment
import os

# list_title : list of video titles.
# format: [ "title1", "title2", "title3" ...]
list_title = []

def classifier(title):
    '''
    Implementation of Naive Bayes
    A: war3, D:Dota, H: HS, L:LOL, W:WOW
    '''
    list_type = ['A','D','H','L','W']
    num_of_type = len(list_type)
    conn = sqlite.Connection(os.getcwd()+'\\db.db') # Database connection instance
    segment.load_userdict(os.getcwd()+'\\segment\\gamedict.txt') #Load personalized segment dict
    # sql_wordinfo: String of prepared SQL statement that fetch word info of every word
    sql_wordinfo ="select * from Word where word = ?"
    sql_sum = "select sum(A) as A, sum(D) as D,sum(H) as H ,sum(L) as L ,sum(W) as W from Word"
    #dict_sum: a dict that stores the sum of total number of  word occurrence of each type.
    dict_sum = conn.get(sql_sum)
    word_list = segment.cut(title, cut_all=False)
    list_prob = [] #Each element represents all kinds of probs of one word
    list_prob_type = [] #Each element represents
    for word in list(word_list):
        word_info = conn.query(sql_wordinfo, word)
        #print(word_info)
        if word_info != []:
            num_A = int(word_info[0]['A'])/int(dict_sum['A'])
            num_D = int(word_info[0]['D'])/int(dict_sum['D'])
            num_H = int(word_info[0]['H'])/int(dict_sum['H'])
            num_L = int(word_info[0]['L'])/int(dict_sum['L'])
            num_W = int(word_info[0]['W'])/int(dict_sum['W'])
            sum = num_A + num_D + num_H + num_L + num_W
            if sum == 0: sum = 1
            #print("%d, %d, %d, %d, %d" % (num_A, num_D, num_H, num_L, num_W))
            t = (
                    (num_A/sum, 1-num_A/sum),
                    (num_D/sum, 1-num_D/sum),
                    (num_H/sum, 1-num_H/sum),
                    (num_L/sum, 1-num_L/sum),
                    (num_W/sum, 1-num_W/sum)
            )
            list_prob.append(t)
    for i in range(num_of_type):
        prob_true, prob_false = 1,1
        for e in list_prob:
            t,f = e[i][0],e[i][1]
            if t ==0 : t =0.01
            prob_true =  t * prob_true
            if  f ==0 : f =0.01
            prob_false =  f * prob_false
        final_prob = t/(t+f)

        list_prob_type.append(final_prob)
        #print(list_prob_type)
    max_index,max = 3,0
    for i in range(len(list_prob_type)):
        #print("%f,%f" % (list_prob_type[i], max))
        if list_prob_type[i] > max:
            max_index,max = i,list_prob_type[i]
    return list_type[max_index]
def test(s):
    if s == 'A':print("Warcraft3")
    elif s == "D": print("Dota/Dota2")
    elif s == "L": print("LeagueOfLengends")
    elif s == "H": print("HearthStone")
    elif s == "W": print("WorldOfWarcraft")

if __name__ == "__main__":
    s_lol = "[放空姿态全面开启]OGN春季赛季军赛Samsung O vs CJ B 第二场"
    s_war3 = "第三季YY天梯爬坑行第二十五期 人造骷髅海"
    s_dota = "Zsmj圣剑 TA 大战4跳刀"
    test(classifier(s_lol))
    test(classifier(s_war3))
    test(classifier(s_dota))










