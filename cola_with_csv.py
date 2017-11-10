import requests
from bs4 import BeautifulSoup

url = 'http://www.parknshop.com/BrandList/COCA-COLA/b/COCA-COLA'
r = requests.get(url)
r_text = r.text
soup = BeautifulSoup(r_text,'html.parser')
table = soup.find('div', class_='product-container')

filename = 'cola.csv'
headers = 'Product', 'Size', 'Price'
f = open(filename,'w')
f.write(str(headers)+'\n')



for td in table.find_all('div', class_='item'):
    name = td.find('div',class_='name')    
    volumn =td.find('div', class_='volumn')    
    price = td.find('div', class_='price discount')
    print('Product: '+ name.text.strip())
    print('Size: '   + volumn.text.strip())
    print('Price: '  + price.text.strip())
    
    f.write(name.text.strip().replace(',','|') + ','+ volumn.text.strip() + ',' + price.text.strip()+'\n')

f.close()
