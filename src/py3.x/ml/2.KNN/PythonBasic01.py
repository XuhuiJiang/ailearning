
#元祖
print ("tuple:a=(1,2,3,4,5)")
a=(1,2,3,4,5)
print(a)
print(type(a))
#单元祖
b=(1,)
c=(1)
print(type(c))
print(a[1:2])
print(a[::2])
print(a[::1])
#列表
print("列表:d=[1,2,3,4,5]")
d=[1,2,3,4,5]
#索引
print(d[0])
#分片，谨记python的分片是左闭右开
print(d[2:-1])
print(d[::2])
print(d[::-2])
#列表元素的替换
d[::-2]=[3,2,1]
print(d)
d.reverse()
print(d)


#字典，键必须不变，值可以改变
print("字典:c={}")
c={}
print(type(c))
c={"1":"this is 1","2":"this is 2","三":"这是三"}
print(c.get("2"))
print(c)
synonyms = {}
synonyms['1']=4
synonyms['mutable'] = ['changeable', 'variable', 'varying', 'fluctuating']
synonyms['immutable'] = ['fixed', 'set', 'rigid', 'inflexible',]
print(synonyms)
print(synonyms.pop('1'))
print(synonyms)
sys_modify={'2':'3','mutable':'1','immutable':['a', 'b', 'c']}
synonyms.update(sys_modify)
print(synonyms)
print(synonyms.keys())
print(synonyms.values())
print(synonyms.items())#返回键值对组成的元祖列表

#集合
d=set(a);
print(d)
d1={5,6,7,10,8,9}
print(d.union(d1))
print(d.intersection(d1))
print(d.symmetric_difference(d1))


