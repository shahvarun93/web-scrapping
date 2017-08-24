import re
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def lookup(i1,i2):
    url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q='+i1+'+'+i2+'&s=nm'

    conn = urllib.request.urlopen(url)
    html = conn.read()

    soup = BeautifulSoup(html)
    links = soup.find_all("td",{"class": "result_text"})

    for tag in links:
        link = tag.get('href', None)

    actor_id=soup.findAll('a', href=re.compile('^/name/nm'))
    for tag in actor_id:
        link = tag.get('href', None)
        break

    new_link=link[6:15]     #actor id fetched
    print(new_link)
    sort_movies(new_link)
    # movies_list(comp_url)

def sort_movies(link):

    conn = urllib.request.urlopen('http://www.imdb.com/filmosearch?sort=user_rating&explore=title_type&role='+link+'&ref_=nm_flmg_shw_3')
    html = conn.read()

    soup = BeautifulSoup(html)
    links = soup.select('h3.lister-item-header')
    imdb=soup.select('div.ratings-bar strong')
    output=[]
    output1=[]

    for i in links:
        output.append(i.text)

    for j in imdb:
        output1.append(j.text)
    write_html(output,output1)



def write_html(o1,o2):
    with open('mypage.html', 'w') as myFile:
        myFile.write('<html>')
        myFile.write('<body>')
        myFile.write('<ul>')
        x1 = combine(o1)
        x2 = combine(o2)
        for i, j in zip(x1, x2):
            s=i, "-" ,j
            myFile.write('<li>%s - %s</li>' % (i,j));
            print(s)

        myFile.write('</ul>')
        myFile.write('</body>')
        myFile.write('</html>')

def combine(ans):
    for x in ans:
        yield x

if __name__ == "__main__":

    prompt1=input("Enter the first name of the actor")
    prompt2 = input("Enter the last name of the actor")
    lookup(prompt1,prompt2)