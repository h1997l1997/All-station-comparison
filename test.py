import os
import requests
import time

def clear1():
    with open('list.txt','r') as f:
        url=f.readlines()
        url_right=[]
        header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        for url_single in url:
            try:
                tf=requests.get(url_single,headers=header)
            except:
                pass
            finally:
                print(tf.status_code)
                if tf.status_code == 500:
                    url_right.insert(0,url_single)
        print (url_right)
        return (url_right)

def clear2():
    with open('list2.txt','r') as f:
        url=f.readlines()
        url_right=[]
        header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        for url_single in url:
            try:
                tf=requests.get(url_single,headers=header)
            except:
                pass
            finally:
                print(tf.status_code)
                if tf.status_code == 500:
                    url_right.insert(0,url_single)
        print (url_right)
        return (url_right)

def compare(list1,list2):
    t=0
    for x1 in list1:
        for x2 in list2:
            c1=requests.get(x1)
            c2=requests.get(x2)
            if c1.text==c2.text:
                t=t+1
    print (t)
    return t

if __name__ == '__main__':
    os.system("test1.py")
    os.system("test2.py")
    url_be=clear1()
    url_been=clear2()
    t=compare(url_be,url_been)
    t_all_be=t/len(url_be)
    t_all_been=t/len(url_been)
    print('相似度1为:%s%%,相似度2为:%s%%' %(t_all_be,t_all_been))
