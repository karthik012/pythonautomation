import re

def method1(arg1):
    print(arg1)
    
def method2(arg1,arg2):
    print(arg1,arg2)
    

def patternCheck(arg1):
    pattern = '^ip-.*\.eu-central-1.compute.internal$'
    URLmatch = re.match(pattern ,arg1)!=None
    return URLmatch

def CertficateChainBlockCreation():
    Flag= 0
    Cnt = 1
    f = open(r"C:\Users\dava7002\Desktop\Sample_certificate_chain.txt",'r')
    data = f.readlines()
    
    for line in data:
        if line.strip() == "-----BEGIN CERTIFICATE-----":
            line = line.lstrip()
            f = open(r"C:\Users\dava7002\Desktop\Certificate_chain_Block"+str(Cnt)+".txt",'w')
            Flag = 1
            Cnt += 1
        if Flag>0:
            f.write(line)
        if line.strip() == "-----END CERTIFICATE-----":
            f.close()
            Flag = 0

def main():
    
    input = 'A'
    
    arg1 = "ip-172-61-49-90.eu-central-1.compute.internal";
    arg2 = 0;
    
    if patternCheck(arg1) == False:
        print("URL is invalid , Exiting...!")
        exit()
    else:
        print("URL is valid , Proceeding...!")
    
    if input == 'A':
        method1(arg1)
    elif input == 'B':
        method2(arg1,arg2)
    else:
        print("The parameter passed doesn't match any of the conditions..!")
        exit()
    
    CertficateChainBlockCreation()
        
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        print("Task Completed Successfully")
