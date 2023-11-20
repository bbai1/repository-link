#upup.py
def Dayup(df): #计算一年后进步多少
    dayup=1.0
    for i in range (365):
        if i%7 in [6,0]: #周六日水平下降
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+df)
    return dayup
dayfactor=0.01
while(Dayup(dayfactor)<37.78):
    dayfactor+=0.001         #如果小于37.78，则增加0.01
print("每天努力的参数是：{:.3f}".format(dayfactor)) #打印最终结果