#!/usr/bin/python3
# -*- coding: utf-8 -*-
import ssl, json, datetime, subprocess, time

cer_iso_time = r'%b %d %H:%M:%S %Y %Z'

domain_1 = "/home/ran/.acme.sh/example.noip.me_ecc/fullchain.cer"
domain_2 = "/home/ran/.acme.sh/example.ddns.net_ecc/fullchain.cer"
domain_3 = "/home/ran/.acme.sh/example.myftp.org_ecc/fullchain.cer"

renew_1 = "/home/ran/acme.sh --issue -d example.noip.me --keylength ec-384 --accountkeylength 4096 -w /home/ran/.acmeweb/ --server letsencrypt --force"
renew_2 = "/home/ran/acme.sh --issue -d example.ddns.net --keylength ec-384 --accountkeylength 4096 -w /home/ran/.acmeweb/ --server letsencrypt --force"
renew_3 = "/home/ran/acme.sh --issue -d example.myftp.org --keylength ec-384 --accountkeylength 4096 -w /home/ran/.acmeweb/ --server letsencrypt --force"

my_service1 = "sudo systemctl restart fox1.service"
my_service2 = "sudo systemctl restart fox2.service"
my_service3 = "sudo systemctl restart fox3.service"
my_service4 = "sudo systemctl restart murmur-new.service"

minimum_lifetime = 14

def cert_fox_sniff(domain, command):
    load_cert = ssl._ssl._test_decode_cert(domain)
    j = json.loads(json.dumps(load_cert))
    print(j['subject'])
    print(j['notAfter'])
    time_left = datetime.datetime.strptime(j['notAfter'], cer_iso_time)
    print(time_left)
    days_left = time_left - datetime.datetime.utcnow()
    print(days_left)
    finaldays = days_left < datetime.timedelta(days=minimum_lifetime)
    if (finaldays == True):
        print("action required")
        print(finaldays)
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        output, error = process.communicate()
        print(output)
        print(error)
        global restart_required
        restart_required = True
        print("executed, waiting 9 sec grace period")
        time.sleep(9)
    elif  (finaldays == False):
        print("nothing to do")
        print(finaldays)
    else:
        print("value not boolean")
    print("---------")

print("------------------ " + str(datetime.datetime.utcnow()) + " UTC ------------------")
cert_fox_sniff(domain_1, renew_1)
cert_fox_sniff(domain_2, renew_2)
cert_fox_sniff(domain_3, renew_3)

try:
    restart_required
except NameError:
    restart_required = False
else:
    print("s'all good man!")

print("Restart required:", restart_required)
if (restart_required == True):
    process = subprocess.Popen(my_service1.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    output, error = process.communicate()
    print(output)
    print(error)
    process = subprocess.Popen(my_service2.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    output, error = process.communicate()
    print(output)
    print(error)
    process = subprocess.Popen(my_service3.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    output, error = process.communicate()
    print(output)
    print(error)
    process = subprocess.Popen(my_service4.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    output, error = process.communicate()
    print(output)
    print(error)
else:
    print("closing without restart")
