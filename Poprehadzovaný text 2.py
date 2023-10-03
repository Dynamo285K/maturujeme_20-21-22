import random

def pomiesaj(path):
    temp = ''
    bad_temp = ''
    result = ''
    with open(path,'r', encoding='utf-8') as fp:
        for line in fp:
            witout_enter = line.replace('\n','')
            x = witout_enter.split(' ')
            # print(x)
            for i in x:
                for j in i:
                    if j.isalpha():
                        temp += j
                    else:
                        bad_temp += j
                if len(temp) > 2:
                     res = random.sample(temp[1:-1],len(temp)-2)
                     g = ''.join(res)
                     result += temp[0] + g +temp[-1] + bad_temp + ' '
                     temp = ''
                     bad_temp = ''
                else:
                    result += temp +bad_temp + ' '
                    temp = ''
                    bad_temp = ''
            result = result.rstrip(' ')
            result += '\n'
        print(result)
    with open('poprehadzovany_text.txt.','w',encoding='utf-8') as fr:
        fr.write(result)

pomiesaj('poprehadzovany_text_vstup2.txt')
