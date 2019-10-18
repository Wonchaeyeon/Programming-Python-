#p244
import xml.etree.ElementTree as ET

f=open("order.xml",encoding="UTF-8")
string=f.read()
#print(string) 이렇게 하면 xml문서가 그냥 text로 찍힘
tree=ET.ElementTree(ET.fromstring(string))  #트리에 제일 높은걸 뽑아라
root=tree.getroot()   #뽑아서 root에 넣기
#print(root.tag)
#print(root.text)    #None

for child in root:
    print("tag: ",child.tag, "text: ",child.text)
f.close()