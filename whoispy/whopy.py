from ipwhois import IPWhois
import argparse
from time import sleep
parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', type=str,
                    help="ip list", required=False)
parser.add_argument('--ipaddress', '-ip', type=str,
                    help="ip address", required=False)
args = parser.parse_args()

result = []


def IpWhois():
    if args.file:
        list_ip = open(args.file, 'r').read().splitlines()
        for all_ip in list_ip:
            obj = IPWhois(all_ip)
            if obj and obj not in result:
                result.append(obj.lookup_whois())
                sleep(0.1)
    if args.ipaddress:
        obj = IPWhois(args.ipaddress)
        result.append(obj.lookup_whois())
    for i in range(len(result)):
        for j in result[i]['nets']:
            asn = result[i]['asn']
            asn_registry = result[i]['asn_registry']
            query = result[i]['query']
            handle = j['handle']
            NetName = j['name']
            description = j['description']
            asn_cidr = j['cidr']
            emails = j['emails']
            print(f"""
            [*] Ip whois result
            
                IP = {query}
                ASN Registry = {asn_registry}
                Org = {description}
                Net Handle = {handle}
                Net Name = {NetName}
                Emails = {emails}
                ASN = AS{asn}
                CIDR = {asn_cidr}
                """)
IpWhois()
