import re

def method1(arg1):
    print(arg1)
    
def method2(arg1,arg2):
    print(arg1,arg2)
    

def patternCheck(arg1):
    pattern = '^ip-.*\.eu-central-1.compute.internal$'
    URLmatch = re.match(pattern ,arg1)!=None
    return URLmatch

def CreateAndWriteFile(fname,data):
    fpath = "C:/Users/dava7002/Desktop/"
    f = open(fpath+fname+".txt",'w')
    f.write(data)
    f.close

def CertficateChainBlockCreation(Dict):
    CreateAndWriteFile("Certificate",Dict[1])
    Cert_chain = re.findall('-----BEGIN CERTIFICATE-----.+?-----END CERTIFICATE-----',Dict[2])
    CreateAndWriteFile("Certificate_Chain_Block1",Cert_chain[0])
    CreateAndWriteFile("Certificate_Chain_Block2",Cert_chain[1])


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
    
    Dict = dict({1: 'CONNECTED(00000003) depth=1 /C=US/CN=YaST Default CA (dlopEldap)/emailAddress=postmaster@site verify error:num=19:self signed certificate in certificate chain verify return:0', 2: 'Certificate chain 0 s:/C=US/CN=dlopldap.site/emailAddress=postmaster@site i:/C=US/CN=YaST Default CA (dlopldap)/emailAddress=postmaster@site -----BEGIN CERTIFICATE----- MIIEUTCCAzmgAwIBAgIBATANBgkqhkiG9w0BAQUFADBSMQswCQYDVQQGEwJVUzEj MCEGA1UEAxMaWWFTVCBEZWZhdWx0IENBIChkbG9wbGRhcCkxHjAcBgkqhkiG9w0B CQEWD3Bvc3RtYXN0ZXJAc2l0ZTAeFw0wNzA4MDMxMjQwNTdaFw0wODA4MDIxMjQw NTdaMEUxCzAJBgNVBAYTAlVTMRYwFAYDVQQDEw1kbG9wbGRhcC5zaXRlMR4wHAYJ KoZIhvcNAQkBFg9wb3N0bWFzdGVyQHNpdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IB DwAwggEKAoIBAQDYBetFqZE5FFaeKc5n220KWcXFa1ys9ZOyHDwjVtOvm2Rgd/77 KM8TOsFq5HyUCUYzYwdC07VuBU3u2qgAleY/0nN+pKP89ohY/rYQbsblHA8QrXVP LmBuKM3kN/MGyN0bKFYrfhAFy7bU1hreyNbcLdUZAmfunYX9YUk4lX8eOHRuMDgp VMw+L8I0c80PtjwvQLDpjw3HRTch3HQLSK3+vCA9WQFmJmHuj5aZiFqqUiCRnOmW zdlbJ9bolStln1luK3+ZYs5vGriR0k303TEZgRdBXcoPFAjVzLY3YjXg4PLwePQq eeZjzWNgQyBasYoKnZ6L/ysspzrUlgBTvbTtAgMBAAGjggE9MIIBOTAJBgNVHRME AjAAMDAGCWCGSAGG+EIBDQQjFiFZYVNUIEdlbmVyYXRlZCBTZXJ2ZXIgQ2VydGlm aWNhdGUwEQYJYIZIAYb4QgEBBAQDAgZAMAsGA1UdDwQEAwIFoDAdBgNVHQ4EFgQU GuSiFwDmaqtRK2fNeqoVFSRd2aEwgYIGA1UdIwR7MHmAFGEVkfLO9/CKNHdY/FQ8 Smu+cF2uoVakVDBSMQswCQYDVQQGEwJVUzEjMCEGA1UEAxMaWWFTVCBEZWZhdWx0 IENBIChkbG9wbGRhcCkxHjAcBgkqhkiG9w0BCQEWD3Bvc3RtYXN0ZXJAc2l0ZYIJ AONqNX/09CYAMBoGA1UdEQQTMBGBD3Bvc3RtYXN0ZXJAc2l0ZTAaBgNVHRIEEzAR gQ9wb3N0bWFzdGVyQHNpdGUwDQYJKoZIhvcNAQEFBQADggEBACiEMDMFZq2ZfBHh 9POKRJ9867BOb0TGmzk/Iw0WT+MbFR5m0a04Ke36tQcluKYSkXxXryrwk+pwDdo4 SXXXf6+cgUT+/te1ifCmjEq3o7zTi1E7wYoXz8q93j8PUjNhhfNfKlfVa4tapwhS z0woT9ie+Bltt8zdbwtBx13iYolHqgxEv2jnKhFSKnW01XlPSyGEMpY/ZNitwA4N 5Qs3iOj6U+oo3xHkB/dDHgSP6DGurc+jo9doLifyVX9AUUCfLbO/U3sCBneVVelJ d31X/QEV/5Njrpj1ZrrnpF+xgUbSLqN5vYhL6pdbuk8Kv9OZPtSKjhobNYD5k1lt nmqVdrc= -----END CERTIFICATE----- 1 s:/C=US/CN=YaST Default CA (dlopldap)/emailAddress=postmaster@site i:/C=US/CN=YaST Default CA (dlopldap)/emailAddress=postmaster@site -----BEGIN CERTIFICATE----- MIIEaDCCA1CgAwIBAgIJAONqNX/09CYAMA0GCSqGSIb3DQEBBQUAMFIxCzAJBgNV BAYTAlVTMSMwIQYDVQQDExpZYVNUIERlZmF1bHQgQ0EgKGRsb3BsZGFwKTEeMBwG CSqGSIb3DQEJARYPcG9zdG1hc3RlckBzaXRlMB4XDTA3MDgwMzEyNDA1NloXDTE3 MDczMTEyNDA1NlowUjELMAkGA1UEBhMCVVMxIzAhBgNVBAMTGllhU1QgRGVmYXVs dCBDQSAoZGxvcGxkYXApMR4wHAYJKoZIhvcNAQkBFg9wb3N0bWFzdGVyQHNpdGUw ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCshFlzTizSuhvcWfBwHjhy X9PgH3C3fFXLW7nOjgtmGMq5PqUBpe8ZtyLVvaTW+F7G836arjGUFHdcNmQgDCDD JU48UyNCa+koBqrjD8YCbEGnz8IpNnbIrxFD4XDWtOlEKPCcChtP0SoifkN31SDQ k0yJMGIeukbF7Ns25+rF+booxvgVeQ4/KQG5NU1U5Parq+G+sFEGTB6q2kpjpCMB M80F730u2H2rluBdAgUB+wAUTp+P+KqNKXI0mZuKI9cid167tz5u3IybWwZlNj8I kH8TDRT+Cne8XSfwJtND2jm2JnK9vHfvxgdxkCpD53bVVcssCf6Id0x5/KePSCvF AgMBAAGjggE/MIIBOzAPBgNVHRMBAf8EBTADAQH/MCwGCWCGSAGG+EIBDQQfFh1Z YVNUIEdlbmVyYXRlZCBDQSBDZXJ0aWZpY2F0ZTARBglghkgBhvhCAQEEBAMCAQYw CwYDVR0PBAQDAgEGMB0GA1UdDgQWBBRhFZHyzvfwijR3WPxUPEprvnBdrjCBggYD VR0jBHsweYAUYRWR8s738Io0d1j8VDxKa75wXa6hVqRUMFIxCzAJBgNVBAYTAlVT MSMwIQYDVQQDExpZYVNUIERlZmF1bHQgQ0EgKGRsb3BsZGFwKTEeMBwGCSqGSIb3 DQEJARYPcG9zdG1hc3RlckBzaXRlggkA42o1f/T0JgAwGgYDVR0RBBMwEYEPcG9z dG1hc3RlckBzaXRlMBoGA1UdEgQTMBGBD3Bvc3RtYXN0ZXJAc2l0ZTANBgkqhkiG 9w0BAQUFAAOCAQEARSQFVo0CQZk80bRF39Ikj6FfV8Ex1vYaDsebYsmEeoK/lPOg jII09lfW0S/80Sd096B76txHMAZLAOBJKD1wsZH4PMyxVbW/J5S8CeQmspUT1yVo qJygQB45/JNpyagIdMN/gI0MT/EOv+AVwaPXDh2yNqRGVo6w3/jd4Pj7H8mp43U2 pARRyeJCNeOSMI5DLOyQpmU2REDNcrfRdhjVHBLIqavENZVqGHJ2xWobjJ6llr+b NF+Vw+HrPnEuRFimqCuRs9yRbOxNX9OvJhUQdp1PctvB48WmeBNcUeE+7Ymy2H9J DEKomkn6L5hzQCA6RD3FR6qROBOuNNSWWwEyGQ== -----END CERTIFICATE----- --- Server certificate subject=/C=US/CN=dlopldap.site/emailAddress=postmaster@site issuer=/C=US/CN=YaST Default CA (dlopldap)/emailAddress=postmaster@site --- No client certificate CA names sent --- SSL handshake has read 2406 bytes and written 468 bytes --- New, TLSv1/SSLv3, Cipher is AES256-SHA Server public key is 2048 bit Compression: NONE Expansion: NONE SSL-Session: Protocol : TLSv1 Cipher : AES256-SHA Session-ID: 60DA3D90FD3D716C2C47BC71D3B08A3932288ABA01B02BCEF9D08F06E0035A38 Session-ID-ctx: Master-Key: 33F4F8CF6112475A88501239FB4D4BA80D53E5B89848482AA81A58894FAB1C99 05137F3AD15E94EFD276CD84B7C7EF38 Key-Arg : None Start Time: 1210860425 Timeout : 300 (sec) Verify return code: 19 (self signed certificate in certificate chain) --- DONE'})
    
    CertficateChainBlockCreation(Dict)
        
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        print("Task Completed Successfully")
