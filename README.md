Parking
=======

This python script detects if the domain is parked or not provided it resolves to an IP.

Please refer to the following blog for details: http://labs.opendns.com/2013/03/20/discovery-of-new-suspicious-domains-using-authoritative-dns-traffic-and-parked-domains-analysis/

The method in the script will only work if there is a webserver on the IP hosting the domain.

Another method could be to check if the following method returns an ip.

dig a random.domain.com +short

None of the methods are guaranteed to work 100% of the time though.
