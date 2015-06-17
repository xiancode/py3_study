#!/usr/bin/env python3
#-*- coding=utf-8 -*-

print(r"建立列表s,s=['1','2']")
s = ['1','2']
print('s    ID= %s' %id(s))
print('s[%s] ID= %s' %(0,id(s[0])))
print('s[%s] ID= %s' %(1,id(s[1])))


print(r"更改s列表中的s[0],s[1]的值")
print(r"s[0]='X'")
print(r"s[1]='Y'")
s[0] = 'X'
s[1] = 'Y'

print(r"更换后的ID信息:")
print('s    ID= %s' %id(s))
print('s[%s] ID= %s' %(0,id(s[0])))
print('s[%s] ID= %s' %(1,id(s[1])))

print(r"重新对s赋值")
print(r"s=['A','B']")
s = ['A','B']

print(r"赋值后的ID信息:")
print('s    ID= %s' %id(s))
print('s[%s] ID= %s' %(0,id(s[0])))
print('s[%s] ID= %s' %(1,id(s[1])))
