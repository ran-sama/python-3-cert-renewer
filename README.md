# python3-cert-renewer
A python3 script to renew letsencrypt certs. 

Overengineered but with nice features:

* checks if a cert needs to be renewed
* can configure minimum lifetime (default 14 days)
* will restart services associated with the certificate
* can renew multiple domains independently

Dependency:  
https://github.com/acmesh-official/acme.sh  
```
wget https://raw.githubusercontent.com/acmesh-official/acme.sh/master/acme.sh
chmod +x acme.sh
```

Use with:

https://github.com/ran-sama/systemd-service-examples  
https://github.com/ran-sama/python3-https-tls1-3-microserver  


## License
Licensed under the WTFPL license.
