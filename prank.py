import requests
import names
i=1234567890
url = 'https://docs.google.com/forms/u/0/d/e/YOUR FORM LINK WILL BE HERE WITH FORM RESPONSE/formResponse'
while True:
    i=i+1
    rname = names.get_full_name()
    form_data = {'entry.<ID/here i have enrollment no>':i,
                'entry.<ID/random name>':rname,
                'draftResponse':[],
                'pageHistory':0}
    user_agent = {'Referer':'https://docs.google.com/forms/d/e/VEW FORM URL OF THE FORM/viewform','User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
    r = requests.post(url, data=form_data,headers=user_agent)