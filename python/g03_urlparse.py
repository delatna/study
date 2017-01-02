import urllib.request

result = urllib.request.urlparse("http://eureka.re.kr/eureka/main.php?cmd=board&bid=11&mode=view&idx=442")

print("[1] result = ", result)

## import를 간단하게 처리하자

from urllib.request import urlparse


result = urlparse("http://eureka.re.kr/eureka/main.php?cmd=board&bid=11&mode=view&idx=442")

print("[2] result = ", result)


