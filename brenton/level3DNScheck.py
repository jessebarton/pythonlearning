import dns.resolver
 
myResolver = dns.resolver.Resolver()
myResolver.nameservers = ['209.244.0.3', '209.244.0.4']
 
for rdata in range(1, 100):
    try:
            myAnswers = myResolver.query("lcokcok.fellowshiponeapi.com", "A")
            for rdata in myAnswers:
                    print(rdata)
    except:
            print("Query failed")