import requests
import names
i=1234567890
url = 'https://docs.google.com/forms/u/0/d/e/YOUR FORM LINK WILL BE HERE WITH FORM RESPONSE/formResponse'
while True:
    i=i+1
    rname = names.get_full_name()
    form_data = {'entry.<ID/here i have enrollment no>':i,
                'entry.<ID/random name>':rname}
    r = requests.post(url, data=form_data)
