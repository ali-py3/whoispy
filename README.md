# whopy tools

This tool do Reverse Whois from ip (like whois tool but with better managment ). you can give file contains ip or give a single ip to the tool

# Files

This tool is wrote with python version 3.x

## Usage

usage: whopy [-h] [--file FILE] [--ipaddress IPADDRESS]

options:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  ip list
  --ipaddress IPADDRESS, -ip IPADDRESS

Example 1 : python3 whopy -ip 1.1.1.1
Example 1 : python3 whopy -f ips.txt
## Installations
You can install this tool or using normal command for use the tool
#### Installation :
	cd whoispy
	python3 setup.py install 
After run this command you can run tool in any path with `whopy` command like :
	`whopy -h`
##### Normal using
	cd whoispy
	python3 whopy.py -h
##### Output
`whopy -ip 1.1.1.1`

	 [*] Ip whois result

           IP = 1.1.1.1
           ASN Registry = apnic
           Org = APNIC and Cloudflare DNS Resolver projectRouted globally by AS13335/CloudflareResearch prefix for APNIC Labs
           Net Handle = AA1412-AP
           Net Name = APNIC-LABS
           Emails = ['resolverabuse@cloudflare.com','helpdes@apnic.net', 'research@apnic.net']
           ASN = AS13335
           CIDR = 1.1.1.0/24
