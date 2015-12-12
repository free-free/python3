#!/usr/bin/env python3
from collections import namedtuple,Iterable,Iterator
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
if isinstance(p,Point):
	print(p.x,p.y)
#deque 是为了实现高效插入和删除操作的双向列表,适用于队列和栈
from collections import deque
q=deque(['a','v','c'])
q.append('x')
q.appendleft('y')
print(q)
q.popleft()
q.pop()
print(q)
#使用dict时,如果引用的key不存在,就会抛出KeyError
#如果希望key不存在的时候,返回一个默认值,就可以使用defaultdict
from collections import defaultdict
dd=defaultdict(lambda:'N/A')
dd['key1']='acc'
print(dd['key1'])
print(dd['key2'])
#使用dict时,key是无序的,如果要保持key的顺序,可以使用OrderedDict
from collections import OrderedDict
d=dict([('a',1),('b',2),('c',3)])
print(d)

#OrderedDict会按照key插入顺序排列,不是key本身排序
od=OrderedDict(d)
print(od)
class LastUpdatedOrderedDict(OrderedDict):
	def __init__(self,capacity):
		super(LastUpdatedOrderedDict,self).__init__()
		self._capacity=capacity
	def __setitem__(self,key,value):
		containsKey=1 if key in self else 0
		if len(self)-containKey>=self._capacity:
			last=self.popitem(last=False)
			print('remove:',last)
		if containsKey:
			del self[key]
			print('set:',(key,value))
		else:
			print('add:',(key,value))
		OrderedDict__setitme__(self,key,value)

#Counter 是一个简单的计数器,应用于统计字符出现的个数
from collections import Counter
c=Counter()
for ch in 'programing':
	c[ch]=c[ch]+1
print(c)


