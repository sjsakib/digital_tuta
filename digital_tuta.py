#encoding:utf-8


from math import *
from functions import *

global p

p = '\nব্যাবহারকারীঃ---> '#prompt
s = None #user input string



banner()
exit = ['exit','বিদায়','খোদা হাফেজ','বাই','bye']

while  not s in exit:
    
    s = raw_input(p)
    
    print "\nডিজিটাল তোতাঃ----> ",
    
    if s in exit:
        break
    
    if 'বর্গমূল' in s or 'square root' in s:
        root(s) 
    elif 'বর্গ'in s or 'square' in s:
        square(s)
    elif 'গুণ' in s or 'multiply' in s or '*' in s:
        multiply(s)
    elif 'ভাগ' in s or 'divide' in s or '/' in s:
        divide(s)
    elif 'তৈরী' in s or 'বানাইসে' in s or 'আবিষ্কারক' in s or 'আবিষ্কার' in s or "বানানো" in s or 'made' in s:
        maker()
        if "কিভাবে" in s:
            process()
    elif 'আসসালামুয়ালাইকুম' in s or 'আসসালামুআলাইকুম' in s:
        print "ওয়ালাইকুম-আসসালাম"
    elif 'যোগ' in s or 'add' in s or '+' in s:
        add(s)
    elif 'বিয়োগ' in s or '-' in s or 'minus' in s:
        minus(s)
    elif 'কেমন আছ' in s or 'how are you' in s:
        how_are_you()
    elif 'মৌলিক' in s or 'prime' in s or 'প্রাইম' in s:
        if "বড়" in s:
            l = num_err(s)
            
        prime(s)
    elif 'গান' in s or ('play' in s and 'song' in s):
        play_song()
    elif 'hi' in s or 'হাই' in s or 'hello' in s or 'Hi' in s or 'হেলো' in s:
        chat_hi()
    elif 'fuck' in s or 'sex' in s:
        print "আমার বয়স মাত্র ২ দিন । দয়া করে খারাপ শব্দ ব্যবহার করবেন না "
    elif "কিভাবে" in s or ('how' in s and 'work' in s):
        process()
    elif 'sin' in s or 'সাইন' in s:
        sin(s)
    elif 'cos' in s or 'কস' in s:
        cos(s)
    elif 'tan' in s or 'ট্যান' in s:
        tan(s)
    elif 'ত্রিভুজ' in s or'ত্রিভূজ' in s or 'triangle' in s:
         triangle(s)
    elif 'দেশের নাম' in s or ('country' in s and 'name' in s):
        print 'বাংলাদেশ'
    elif 'রাজধানী' in s or 'capital' in s:
        print 'ঢাকা'
    elif 'ফুল' in s or 'flower' in s:
        print 'শাপলা'
    elif 'ফল' in s or 'fruit' in s:
        print 'কাঁঠাল'
    elif 'গাছ' in s or 'tree' in s:
        print 'আমগাছ'
    elif 'পাখি' in s or 'bird' in s:
        print 'দোয়েল'
    elif 'মাছ' in s or 'fish' in s:
        print 'ইলিশ'
    elif 'ছেলে' in s and 'মেয়ে' in s:
        sex(s)
    elif 'থাক' in s or 'live' in s or 'বাড়ি' in s or 'home' in s:
        print "আমি যেখানে যাই সেখানেই আমার বাড়ী । আমি বেশিরভাগ সময় ই ঘুমিয়ে থাকি । যখন ডাক     দেয়া হয় তখন ওঠি ।"
    elif 'doing' in s or 'করছ' in s:
        print 'আপনার সাথে চ্যাট'
    elif 'এত' in  s or 'অত' in s in s:
        print "বস জানে"
    elif 'school' in s or 'class' in s or 'ক্লাসে' in s or 'college' in s or 'স্কুল' in s:
        print 'আমার বয়স মাত্র দুই দিন । স্কুল কলেজে পড়ি না । আমার বস আমাকে শেখায় । মাথার ভেতরে   ঢুকে '
    elif 'অধিনায়ক' in s:
        print 'মুশফিকুর রহিম'
    elif 'নাম' in s or  'name' in s:
        print 'ডিজিটাল তোতা'
    elif 'খাও' in s or 'khao' in s or 'eat' in s:
        print 'এনার্জি'  
    elif '?' in s:
        print "দুঃখিত । আমার জানা নেই । " 
    else:
        err()
        
        
print "খোদা হাফেজ । আবার দেখা হবে । আপাতত ঘুমিয়ে পড়ছি । আবার যদি ইচ্ছা হয় অধমকে ডাকবেন ।" 
