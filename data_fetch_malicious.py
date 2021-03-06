"""
This Module is for Extracting Phishing URLs from Phishtank.com
"""

import re 
import csv
import time
import urllib.request as req
import urllib.parse as prs

def extrac_relevant_info(dat,my_file):
	"""
	Function to extract the relevant Link from a given Page of DMOZ open repository and write it to a file
	"""
	patt=r'<td valign="center" class="value">http[^<]*'		###Regular Expression for matching and searching Relevant Link on the Page
	links=re.findall(patt,dat) #Parsing Data Using Regex
	print('The total of %i spam links are as follows : '%len(links))
	for i in links:
		i=i.replace(r'<td valign="center" class="value">','')
		print('Writing link :',i)
		my_file.writerow([i,1])		### Writing the Link to Dataset File
	print('\n')
	#time.sleep(1)

#### Actual Code where exection Begins
try:
	url='https://www.phishtank.com/phish_search.php'		### Specifying URL to being with
	headers={}
	headers['user-agent']="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
	### Specified the HTTP headers to use
	savefile=open('malicious_url.csv','a')
	savefile_obj=csv.writer(savefile)
	#savefile_obj.writerow(['URL','Lable'])

	for i in range(250):
		## Entering the POST parameters
		values={'page':str(i),'valid':'y','active':'all','Search':'Search'}
		data=prs.urlencode(values)		
		data=data.encode('utf-8')		#### encoding URL to UTF-8
		#print(x.read())
		myreq=req.Request(url,data=data,headers=headers)	
		resp=req.urlopen(myreq) #Making Request
		respData=str(resp.read()) #Reading Response
		print('Page no:',i)
		extrac_relevant_info(dat=respData,my_file=savefile_obj)
		time.sleep(2)
	savefile.close()

except Exception as e:
	print(str(e))