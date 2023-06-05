# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 17:41:30 2023

@author: KN_AN
"""
aclNum = int(input("What is the IPv4 ACL number? "))
if aclNum >= 1 and aclNum <= 99:
    print("This is a standard IPv4 ACL.")
elif aclNum >=100 and aclNum <= 199:
    print("This is a extended IPV4 ACL. ")
else:
    print("This is not a standard or extended IPV4 ACL. ")
        
    