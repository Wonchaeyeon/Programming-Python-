#2413 원채연 / 영어 단어 암기를 위해 원하는 영어 레벨을 선택하면 뜻이 나오고  영어 단어를 입력하는 프로그램. 
#마지막엔 내 점수를 볼 수 있음. 

import random


E_words1 = {"a":"하나의","act":"행동하다,행동,행위","actor":"영화배우","box":"상자","boy":"소년, 사내아이",\
 "age":"나이","baby":"아기","back":"뒤, 등, 돌아오다","bad":"(행동이) 나쁜,(음식 등이)상한","bag":"가방",\
 "ball":"공","balloon":"풍선","banana":"바나나","band":"밴드, 악단","bank":"은행","base":"바닥, 밑면, (야구의)베이스",\
 "cream":"크림, 크림색의","cross":"(길 따위를) 건너다","cry":"울다, 외치다","cup":"컵, 잔","curtain":"커튼","cut":"자르다",\
 "cute":"귀여운","cake":"케이크","book":"책","bottle":"병","too":"또한, 역시, 지나치게","tooth":"이, 치아",\
 "top":"꼭대기,최고","dog":"개"}
E_words2 = {"ago": "~전에","air": "공기, 공중","airplane":"비행기","airport":"공항, 비행장","album":"앨범,사진첩",\
 "all":"모든, 모두","afraid":"무서워하여, 두려워하여","after":"~뒤에, ~다음에","burnt":"burn의 과거, 과거분사형",\
 "bus":"버스","busy":"바쁜","but":"그러나, 그렇지만","butter":"버터","button":"단추, (벨의)누름단추","buy":"사다",\
 "zero":"영(0)","zoo":"동물원","young":"젊은,어린","weak":"약한, 힘없는","wear":"(옷을)입다","weather":"날씨, 기후",\
"week":"주, 1주일","welcome":"환영하다","well" :"잘, 훌륭하게","west": "서쪽","beach":"해변, 바닷가",\
 "bear": "곰, 참다, 견디다","cat": "고양이","catch": "잡다","cow": "암소"}      
E_words3={"wet":"젖은","along":"~을 따라서","always":"항상, 언제나","among":"~사이에, ~가운데","an":"하나의",\
"and":"그리고, ~와","angry":"화난, 성난","animal":"동물, 짐승","answer":"대답, 대답하다","any":	"어떤, 무슨",\
"apartment":"아파트","arm":"팔","toy":"장난감","train":	"기차","travel":"여행하다","tree":"나무","trip":"여행",\
"truck":"트럭","true":"진실의, 정말인","very":"아주, 대단히","video":"비디오","village":"마을","violin":"바이올린",\
"visit":"방문하다","across":"~을 가로질러, ~을 건너서","address":"주소,연설","afternoon":"오후","again":"또, 다시 한 번",\
"chair":"의자","chalk":"분필, 백묵"}
E_words4={"bread":"빵","break":"깨다, 부수다","breakfast":"아침식사","bridge":"다리, 교량","bright":"밝은,빛나는",\
"bring"	:"가져오다, 데려오다","brother":"형제, 형, 오빠,남동생","brown":"갈색의, 갈색","club":	"클럽, 모임",\
"coat":"코트, 외투","coffee":"커피","coin":"동전","cold":"추운, 차가운","color"	:"빛깔, 색","come":	"오다","comic book":"만화책",\
"computer":"컴퓨터","cook":	"요리사","cool":"시원한, 서늘한","copy"	:"그대로 옮겨 쓰다","corner":"구석, 모퉁이",\
"count":"세다","doll":"인형","dollar":"달러(미국의 화폐단위)","dolphin":"돌고래","door":"문","down":"아래로,낮은 곳으로",\
"draw":"~을 그리다, 끌다, 끌어당기다","dream":"꿈","bicycle":"자전거"}

H_words1={"culture":"문화,교양","experience":"경험","education":"교육","symbol":"상징","effect":"결과,영향,효과",\
"liberty":"자유","affair":"사건,일","comfort":"안락,위안","tradition":"전통,전설","subject":"학과,주제",\
"object":"사물,목적,(동)반대하다","source":"출처,근원","revloution":"혁명","pollution":"오염","system":"조직,체계,지도",\
"triumph":"승리","respect":"존경,존경하다","communicatio":"전달,교통","foundation":"기초","glory":"영광","situation":"위치,사태",\
"competition":"경쟁","prairie":"대초원","effort":"노력","section":"부분, 구역","no smoking section":"금연구역",\
"rein":"고삐(억제하다,통제되다)","solution":"해결,용해","hono(u)r":"명예/경의","unity":"통일/일치","population":"인구"}
H_words2={"direction":"방향,지시","dialog(ue)":"대화","repiblic":"공화국","method":"방법","increase":"증가 [동]증가하다",\
"decrease":	"감소, [동]감소하다","amount":"양,액수,총계","ancestor":"조상,선조","voyage":"항해","sculpture"	:"조각(품)",\
"instrument":"기계, 기구, 도구","figure":"숫자, 계산, 모습, 인물","activity":"활동","cause":"원인, 이유","worth":"가치, ~에 가치가 있는",\
"accident":"사고, 뜻밖의 사건","adventure":"모험","view":"경치, 의견","relative":"친척,관계가 있는","superstition":"미신",\
"habit":"습관, 버릇","wealth":"재산, 부","treasure":"보물","universe":"우주, 전세계","adult":"성인, 성인의","feast":"향연,잔치",\
"resources"	:"자원, 수단","ruin":"파멸","monument":	"기념비, 기념물","information":	"정보, 지식, 통지"}
H_words3={"appetite":"식욕","unification":"통일,단일화","mystery":"신비, 불가사의","thermometer":"온도계",\
"burden":"무거운 짐, 짐을 지우다","series":"연속, 시리즈","oath":"맹세, 선서","appointment":"임명, 약속","clue":"실마리, 단서","debt":"은혜, 빚",\
"hydrogen":"수소","control":"통제, 지배, 통제하다, 지배하다","uniform":"제복, 한 모양의","design":"계획, 설계, 계획하다, 디자인 하다",\
"damage":"손해, 손상","custom":"습관, 풍습","traffic":"교통","sophomore":"2학년생","temperature":"온도, 체온",\
"limit":"제한하다, 한계, 제한","statue":"조각상","furniture":"가구","parade":"행렬","public	":"공중(사회), 공공의, 공중의",\
"pilgrim":"순례자","greeting":"인사, 축하","language":"언어","opinion":"의견","athlete":"운동 선수","supply":"공급, 공급하다"}
H_words4={"surface":"표면","electricity":"전기","order"	:"순서,명령","spirit":"정신","purpose":"목적","promise":"가망,약속",\
"project":"계획, 계획하다","government":"정부, 정치의","exercise":"운동, 연습하다","comparison":"비교","interest":"이익, 흥미",\
"funeral":"장례식","senior":"선배, 손위에","junior":"후배,손아래에","democracy":"민주주의,민주정치","general":"육군장군",\
"admiral":"해군대장","edge":"날,가장자리","biology":"생물학","danger":"위험","advice":"충고","practice":"연습하다",\
"mammal":"포유동물","grade":"학년","score":"점수","pause":"중지,멈추다","pronunciation":"발음 ","stress":"압박,강조하다",\
"contest":"경쟁","horizon":"수평선의"}
T_words1={"account":"계산","account for":"~를 설명하다","benefit from": "~로부터 혜택을 받다 ","condense" :"압축하다 ",\
"condense":"into ~로 압축하다","better":"~를 개선하다","conduct":"실시,시행하다","accrue":"생기다,얻어지다",\
"conductor":"지휘자,차장","confirmation":"확정서","be aware of":"~를 조심하다","biannual":"반년마다의",\
"accumulation":"축적,축적물","confirmed":"확인된 ","beneficial" :"혜택이 많은", "beneficiary":"수혜자",\
"confiscate":"압수,몰수하다","binding":"구속력 있는,의무적인","bill":"계산서, 법안 ","accurately":"정확히",\
"achievement":"업적,성과","irretrievable":"돌이킬 수 없는","issue":"발행하다,문제","be laid off":"해고되다 ",\
"landfill":"매립지","landslide":"사태","itinerary":"여행스케줄","agenda":"의사일정","mutually":"서로","natural disaster":"재해"}
T_words2={"needlessly":"불필요한","jet lag":"시차 부적응중","keynote speech": "기조연설","laboratory":"실험실","lack":"부족하다",\
"municipal":"시의","multiply":"급증하다","mutual":"상호의","largely":"주로,대량으로","lastingly":"영구적인",\
"lavatory":"기차,비행기의 화장실","support":"지지, 지주","irritate":"짜증나게(초조하게)하다","generous":"관대한,마음이 넓은",\
"tolerant":"관대한","liberal":"자유주의자","reject":"거절하다","substitute":"대리의","occur":"일어나다,나타나다",\
"despise":"경멸하다","contempt":"경멸(disdain)","gain" :"이익, 증가","avail":"도움이 되다","educate":"교육하다,양성하다",\
 "resemble" :"닮다","grasp":"지배(력)","reconsider":"재고하다","support":"지지,지주","irritate":"짜증나게(초조하게)하다",\
 "specify":"명시하다"}
T_words3={ "tolerant":"아량이 있는","prove":"입증하다 ","illustrate" :"설명하다","exemplify":"예시하다","conservative":"보수적인;전통적인",\
"progressive":"전진하는,누진적인","fortify":"견고하게 하다 ","strengthen": "강하게하다, 강해지다 ","reinforce": "보강하다 ",\
"multiply": "늘리다","reproduce":"재생시키다;재현하다","elicit":"끌어내다","extract":"끌어내다","implore":"간청(탄원,애원)하다",\
"appoint": "임명하다","disgust":"역겹게하다", "preach":"설교하다,전도하다","orship":"숭배(존경)하다","yawn":"하품하다",\
"hiccup": "딸꾹질","quarrel":"네모진 촉이 달린 화살","pillar":"기둥,주석","servitude":"노예 상태","recreation":"휴양;원기회복",\
"punctuality":"시간엄수","punctual":"시간을 엄수하는","fascination":"매혹, 눈독들임","attraction": "끄는 힘,인력","vicious":"사악한, 부도덕한",\
"distrust":"불신,의심하다"}
T_words4={"suspicion":"의심, 협의","endeavor": "노력하다","devote":"바치다,~에 몰두하다","pride":"자만,거만","proud":"자랑하고 있는",\
"discontinue":"중지하다","ignore":"무시하다,","disregard":"무시,무시하다","neglect":"소홀","depend":"의지하다",\
"ability":"능력","absenteeism": "결근","access": "접근권한","accessible":"접근이 가능한 ","accommodate":"수용하다",\
"involve":"수반하다, 포함하다","diverse" :"다양한","superb": "최고의","emergency":"비상사태","immigration":"입국심사",\
"remote":"외진, 외딴","accumulate":"축척하다","geographic":"지리상의 ","turbulence":"난기류","unavailable":"이용할 수 없는",\
"seating":"좌석 배열","drift":"떠다니다","missing":"없어진","process":"과정"}
global target   #수준 선택하는 전역변수
global level    #레벨 선택하기 
Words = []    # 각 레벨 넣는 리스트



target=input("원하시는 수준을 선택하세요(0:초등단어, 1:중-고등단어, 2:토익단어):")
if target=="0":
    level=input("초등단어의 원하시는 레벨을 선택하세요(0:1단계, 1:2단계, 2:3단계, 3:4단계):")
    if level=="0":
        Words=E_words1      #Words{}에 내가 입력한 레벨이 들어감. 
    elif level=="1":
        Words=E_words2
    elif level=="2":
        Words=E_words3
    elif level=="3":
        Words=E_words4
elif target=="1":
    level=input("중-고등 단어의 원하시는 레벨을 선택하세요(0:1단계, 1:2단계, 2:3단계, 3:4단계):")
    if level=="0":
        Words=H_words1
    elif level=="1":
        Words=H_words2
    elif level=="2":
        Words=H_words3
    elif level=="3":
        Words=H_words4
elif target=="2":
    level=input("토익 단어의 원하시는 레벨을 선택하세요(0:1단계, 1:2단계, 2:3단계, 3:4단계):")
    if level=="0":
        Words=T_words1
    elif level=="1":
        Words=T_words2
    elif level=="2":
        Words=T_words3
    elif level=="3":
        Words=T_words4
   
score = 0   
list_1 = []
list_1 = random.sample(Words.keys(), 10)   #선택한 단어 30개 중 10개의 단어의 키값만 뽑음 
print(list_1)
def word(i):                    
    print("뜻 : " + Words[i])
    ans=input("영어단어를 입력하세요. : ")
    return ans


for i in list_1:#레벨넣는 변수 안에 키 값이 있는동안 
    ans=word(i)       #입력한 단어가 word함수 키값에 있나 
    if ans.lower() == i:    #입력한 키 값을 다 소문자로 하고 입력한게 키값의 답과 같으면 
        print("참 잘했어요!\n")             #출력
        score = score + 10               #맞출때 마다 10점씩 증가
    else:
        print("틀렸어요! 다시하세요!")
        print(Words[i]+"는(은) "+i+"입니다.\n")
        ans=word(i)                 
        if ans.lower() == i:            #틀렸으면 한번 더 입력하게 함.  
            print("정답입니다!\n")
        else:
            print("또 틀렸네요. 좀 더 꼼꼼하게 외우세요!!\n")


print("100점 만점에 :", str(score) + "점")