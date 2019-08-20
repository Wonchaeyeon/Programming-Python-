#p153 main_repeater.py

#import repeater   #다 똑같은 방법임

#from repeater import repeat,once

#from repeater import *

import repeater as re  #같은 디렉토리에 있는건 그냥 import하기 

s=input("반복할 문자를 입력하세요: ")
n=input("반복 횟수를 입력하세요: ")
#repeater.repeat(s,int(n))
#repeater.repeat(s)
#repeater.once(s)


#repeat(s,int(n))
#repeat(s)
#once(s)


re.repeat(s,int(n))
re.repeat(s)
re.once(s)
