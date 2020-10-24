import requests
from re import findall as reg
from collections import OrderedDict
from time import sleep
from pyfiglet import Figlet
from bs4 import BeautifulSoup


custom_fig = Figlet(font='graffiti')

print(custom_fig. renderText('G.SMTP'))
print('\t Gmass mass sender')
print('\t By https://github.com/xcapri/\n')

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

def gMass(mail,too):
  mass = mail.split("|")

  SmtpServer = mass[0]
  port = mass[1]
  username = mass[2]
  password = mass[3]
  frm = mass[4]
  to = too
  
  try:
    
  

    

    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.gmass.co',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.gmass.co/smtp-test',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    data = {
      'SmtpServer': SmtpServer,
      'port': port,
      'sso': 'Auto',
      'username': username,
      'password': password,
      'from': frm,
      'to': to
    }

    response = requests.post('https://www.gmass.co/Smtp/CreateTest', headers=headers,  data=data)

    #print(response.status_code)
    stat = response.status_code
    if stat == 200:
      #print(response)
      print(' [ Test send to :'+to+' ] <= [ From :'+frm+' ]')

      tesid = response.text.replace('"','')
      # print()
      # print(tesid)
      # print(response.text.replace('"',''))

      getres = requests.get('https://www.gmass.co/smtp/teststatus?testId='+tesid, headers=headers)
      #print(getres)
      od = OrderedDict([('<pre style="background-color: black">', ''), ('</pre>', ''),('<div class="neither">',''),('<div class="client">',''),('<div class="server">',''),('</div>',''),('<div class="error">',''),('&lt;&lt;','[p0n]'),(' &gt;&gt;','[p0n]'),('    ',''),('   ','')])
      repl = replace_all(getres.text, od)
      soup = BeautifulSoup(repl,"html.parser")
      print(soup)
      
      sleep(3)
  except Exception as e:
    print(e)
  


try:

  try:
    lists = raw_input("List SMTP : ")
    readsplit = open(lists).read().splitlines()
    
  except:
    print("Wrong input or list not found!")
    exit()
  try:
      too = raw_input("Mail To : ")
  except:
      print("Wrong input mail!")
      exit()
  if 'txt' in lists:
        # gMass(lists,too)
        for x in readsplit:
          # print(x)
          # print(too)
          gMass(x,too)

except Exception as e:
  print(e)
