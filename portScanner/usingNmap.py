import nmap
begin =50
end=500
target='15.207.169.232'
scanner=nmap.PortScanner()
for i in range(begin,end+1):
    res=scanner.scan(target,str(i))
    res=res['scan'][target]['tcp'][i]['state']
    print(f'Port {i} is {res}.')
