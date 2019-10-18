#p239

#save
import pickle

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __str__(self):
        return ("이름: "+self.name+"\n나이: "+str(self.age))

perl = Person("정유경",18)
print(perl)

f=open("object.bin","wb")
pickle.dump(perl,f)   #perl 객체를 f 파일에서 내맘속에 저장
f.close()


#load
#p247
f=open("object.bin","rb")
person=pickle.load(f)
f.close()

print(person)

#f.write(perl.name)  텍스트로 출력할땐 이렇게 김.
#f.write("\t")
#f.write(perl.name)
#f.write("\t")
# while True:             바이트는 한줄인데 텍스트로 읽을때 이렇게 김
#     data=f.readline()
#     if not data:
#         break
#     l=data.split()
#     per2=Person([0],l[1])
#     print(per2)

#object list
p1=Person("정유경",18)
p2=Person("정재현",23)
p3=Person("강하늘",33)
people=[p1,p2,p3]

f=open("people.bin","wb")
pickle.dump(people,f)
f.close()

f=open("people.bin","rb")
people2=pickle.load(f)
f.close()

for item in people2:
    print(item)