import os
import shutil
import requests 
from PyPDF2 import PdfFileMerger

response = requests.request("GET", 'https://service-b39yklt6-1256763111.gz.apigw.tencentcs.com/release/getInfo/2021_04_27')

data = response.json()
print(len(data))

shutil.rmtree('./temp/')
os.mkdir("./temp")

def downLink(url, name):
  r = requests.get(url) 
  with open("./temp/" + name, "wb") as code:
        code.write(r.content)

for num in range(len(data)):
  fileName = 'rmrb20210427%s.pdf' % (str(num + 1).zfill(2))
  url = 'http://paper.people.com.cn/rmrb/images/2021-04/27/%s/rmrb20210427%s.pdf' % (str(num + 1).zfill(2), str(num + 1).zfill(2))
  print(url)
  downLink(url, fileName)
      
target_path = './temp'
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

file_merger = PdfFileMerger()
for pdf in pdf_lst:
    file_merger.append(pdf)     # 合并pdf文件

file_merger.write("./new.pdf")

# downLink('http://paper.people.com.cn/rmrb/images/2021-04/27/01/rmrb2021042701.pdf', 'rmrb2021042701.pdf')