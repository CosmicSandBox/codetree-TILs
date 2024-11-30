	1.	1월 (January): 31일
	2.	2월 (February):
	•	일반적으로 28일
	3.	3월 (March): 31일
	4.	4월 (April): 30일
	5.	5월 (May): 31일
	6.	6월 (June): 30일
	7.	7월 (July): 31일
	8.	8월 (August): 31일
	9.	9월 (September): 30일
	10.	10월 (October): 31일
	11.	11월 (November): 30일
	12.	12월 (December): 31일

n = int(input())

if n == 1 or 3 or 5 or 7 or 8 or 10 or 12 :
    print(31)
elif n == 4 or 6 or 9 or 11 :
    print(30)
else :
    print(28)