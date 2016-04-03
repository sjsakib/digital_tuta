#encoding:utf-8

import time
import os
import math


def err():
    print "দুঃখিত আপনার কথা বুঝতে পারি নি । আগেই বলেছি আমার বয়স মাত্র ২ দিন । দয়া করে আরএকটু বুঝিয়ে বলুন..."




def find_number(strng):
    
    digit = ['0','1','2','3','4','5','6','7','8','9']
    nums = []
    
    start = None
    
    while len(strng):
        first = True
        index = 0
        for ch in strng:
            if ch in digit:
                pos = index
                if first:
                    first = False
                    start = pos
            if not ch in digit and not first:
                break
            index+=1
            
        if first:
            strng = []

        if start is not None:
            nums.append(int(strng[start:pos+1]))
            strng = strng[pos+1:]
            start = None
            
            
    return nums
    


def num_err(s,t = False):
    if t:
        x = 2
    else:
        x = 1
    l = find_number(s)
    while len(l)<x:
        print "দয়া করে ইংলিশ ডিজিটে সংখ্যা দিন (কমপক্ষে "+str(x)+"টি)"
        s = raw_input('-->')
        l = find_number(s)
    return l

def square(s):
    l = num_err(s)
    print l[0]*l[0]
    
    
def how_are_you():
    t1 = time.time()
    t2 = t1 + 4
    print 'আমি কেমন আছি জানতে চান ? দেখাচ্ছি... আমি অনেকটা এমন আছি...'
    while t2>t1:
        t1 = time.time()
    os.system('gnome-system-monitor')




def play_song():
    os.system('rhythmbox bangla1.mp3')


def root(s):
    l = num_err(s)
    print math.sqrt(l[0])





def banner():
    ln = "+-----+"
    print "\n\n"
    print ' '*10 + ln*11
    print ' '*10 +'|'+' '*75+'|'
    print ' '*10 +' '*75
    print ' '*10 +' '*75
    print ' '*10 +' '*32+'ডিজিটাল তোতা'
    print ' '*10 +' '*32+'নির্মাতা : সাকিব'
    print ' '*10 +' '*32+'আশুগঞ্জ সারকারখানা কলেজ'
    print ' '*10 +' '*32+'দ্বিতীয় বর্ষের ছাত্র'
    print ' '*10 +' '*75
    print ' '*10 +'|'+' '*75+'|'
    print ' '*10 +ln*11
    print "\n\n"
    
    
    
    print "    আমি ডিজিটাল তোতা । আমি মানুষের সাথে কথা বলতে পারি । নাম তোতা বলে ভাববেন না",
    print "আমি বুদ্ধিহীন প্রাণী । আমি অঙ্কে খুব পাকা । আমাকে যেকোন যোগ-বিয়োগ, গুণ-ভাগ দিন",
    print "চোখের পলকে করে দেব । অনেক বড় কোন সংখ্যা মৌলিক কি না জানতে হলে আমাকে  জিজ্ঞেস করতে পারেন । আপনার জন্য  ত্রিভুজের ক্ষেত্রফল বের করে দেয়ার মত কাজ করতে   পারি",
    print "তবে আমি আপনার সব কথা হয়ত বুঝব না । আমার বয়স যে মাত্র ২ দিন !",
    print "২ দিনের একটা বাচ্চার সাথে তুলনা করলে আমার কাছে কিছুটা বেশীই আশা করতে পারেন  এটা বলতে    পারি । আমি  ফিডার খাই না । সময়মত না পেলে কেঁদে   ভূমিকম্প  আনি না । আবার কোলে নিলে সময়ে অসময়ে কাপড়ও নষ্ট  করি না ! আমি আপনাকে গানও শুনাতে পারি"
    
    
    print "\n\n"
    
    
    
    
    
    
    
def is_prime(x,n =10000000000 ,list = []):
	"""takes a number and returns True if prime and False if not.
	is compromised with speed and memorry
	if number is larger than 10000 then you need to
	provide the rangeas a second argument."""
	if x<2:
		return False
	n = int(math.sqrt(n))
	if len(list) is 0:
		root = int(math.sqrt(n))
		for i in range(n+1):
			list.append(True)
		i = 2
		j = 2
		while i <= root:
			if list[i] == True:
				while i*j <= n:
					list[i*j] = False
					j += 1
			i += 1
			j = 2
def generate_prime(frm = 2,to= 1000 , after = 0):
    
    
    if not after:
        l = []
        while frm <= to:
            if  is_prime(frm):
                l.append(frm)
            frm+=1
        return l
    else:
        while True:
            if is_prime(after):
                return after
            after+=1
	
	
	for i in range(2,n+1):
		if list[i] and i is not x:
			if x%i == 0:
				return False
	else:
		return True
	
def prime(s):
    l = num_err(s)
    t1 = time.time()
    if "বড়" in s or 'larger' in s:
            l = num_err(s)
            print generate_prime(after= l[0])
    else:
        if is_prime(l[0]):
            print "হ্যাঁ।"
        else:
            print "না ।" 
    t2 = time.time()
    print "এটা হিসেব করতে আমার", t2-t1,"সেকেন্ড লেগেছে" 
    
    
    
def add(s):
    l =num_err(s)
    s = 0
    for i in l:
        s+= i
    print s
    
    
    
def play_hindi():
    print "sorry, no hindi"
    
    
def minus(s):
    l = num_err(s,t= True)
    print l[0] - l[1]
    
    
def maker():
    print "আমার বস । সাকিব" 
    
def chat_hi():
    print "হেলো :) নাইস টু মিট ইউ । "
        
        
    
def process():
    print "আমার সোর্স কোড লেখে হয়েছে পাইথন ল্যাঙ্গুয়েজ ব্যবহার করে । গাণিতিক কাজগুলো করি math  মডিউল ব্যবহার করে । আর অন্যান্য কাজগুলো করি লিনাক্সের টার্মিনাল ব্যবহার করে । "
    
def multiply(s):
    l = num_err(s)
    s = 1
    for x in l:
        s = s*x
    print s
    
def divide(s):
    l = num_err(s,t = True)
    l[0] = float(l[0])
    print l[0]/l[1]
    
    
def sin(s):
    l = num_err(s)
    print math.sin(l[0]*.017453292)
    
def cos(s):
    l = num_err(s)
    print math.cos(l[0]*.017453292)
    
def tan(s):
    l = num_err(s)
    print math.tan(l[0]*.017453292)
    
def triangle(s):
    l = num_err(s, t = True)
    print l[0]*l[1]*.5,"বর্গ একক"
    
def sex(s):
    print "আপনি যেকোন একটা ধরে নিতে পারেন"

