from ftplib import FTP

host = "demo.wftpserver.com"
user = "demo"
password = "demo"

with FTP(host) as ftp:
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())

    with open('version.txt', 'wb') as f:
        ftp.retrbinary("RETR" + "mytest.txt", f.write, 1024)

    ftp.quit()
