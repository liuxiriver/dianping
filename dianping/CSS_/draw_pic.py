import matplotlib.pyplot as plt
import re

str = """ 
         <pt x="297" y="714" on="1"/>
        <pt x="262" y="674" on="0"/>
        <pt x="160" y="612" on="0"/>
        <pt x="111" y="598" on="1"/>
        <pt x="111" y="516" on="1"/>
        <pt x="212" y="546" on="0"/>
        <pt x="279" y="614" on="1"/>
        <pt x="279" y="0" on="1"/>
        <pt x="361" y="0" on="1"/>
        <pt x="361" y="714" on="1"/>
"""
x = [int(i) for i in re.findall(r'<pt .*?x="(.*?)"', str)]
y = [int(i) for i in re.findall(r'<pt .*?y="(.*?)"', str)]
print(x)
print(y)
plt.plot(x, y)
plt.show()