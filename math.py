#math.py
import math
#计算中位数
def get_median(a,n):
    if n%2==1 :
        median_value=a[(n+1)//2-1] #如果数字个数为奇数
        #则中位数为（n+1）/2，切片为(n+1)/2-1
    else:
        median_value=(a[n//2-1]+a[n//2])/2
        #如果为偶数，则中位数为第n/2和第n/2+1的平均数
    return median_value
#计算平均值
def get_average(a,n):
    s = 0
    for i in a:
        s += i #求和
    average_value=s/n #计算平均值
    return average_value
#计算标准差
def get_bzc(a,n):
    average=get_average(a,n) #获取平均值
    total=0.0
    for i in a:
        total += (i-average)**2
    bzc_value=math.sqrt(total/n) #计算方差
    return bzc_value
def main():
    a=[]
    b=input('请输入一串数字：')
    for i in range(0,len(b)):
        c=int(b[i])
        a.append(c)
    n = len(a)  # 获取字符串的长度
    print("平均数为：{}".format(get_average(a,n)))
    print("中位数为：{}".format(get_median(a,n)))
    print("标准差为：{:.3f}".format(get_bzc(a,n)))
main()
