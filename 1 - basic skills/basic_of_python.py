##
## 12. April. 2021
## introduction of python
##

#simple py
languages = ['python', 'perl', 'c', 'java']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")

#
a = 80
b = 75
c = 55
(a+b+c) / 3 # float 형으로 나옴.
(a+b+c) // 3 # 소수점 짤림.

