def msg_toString(msg, t):

    s=''
    for i in msg:
        s = s+i
    print s
    return s

def msg_length(s):
    print 'length of message = ', len(s)

def msg_n_1bits (s):
    sum = 0
    for i in s:
        if i == '1':
            sum+=1
    print 'number of \'1\' ', sum

def msg_efficiency(msg_list, entropy,t):
    sum = 0
    for i in range (0, len(t)):
        sum += t[i]*len(msg_list[i])
    efficiency = entropy/sum
    print "efficiency = ", efficiency
    return efficiency


