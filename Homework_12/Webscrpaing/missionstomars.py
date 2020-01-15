
def scrape():

    from bs4 import BeautifulSoup as bs
    import pandas as pd
    from splinter import Browser


    executable_path = {'executable_path':'chromedriver.exe'}
    browser=Browser('chrome',**executable_path,headless=False)

    url='https://mars.nasa.gov/news'
    browser.visit(url)
    html=browser.html
    soup=bs(html,'html.parser')

    classlists=soup.find_all(class_="list_text")
    titletext=[]
    paratext=[]
    for classlist in classlists:
        titletext.append((classlist.find_all(class_='content_title'))[0].a.text)
        paratext.append((classlist.find_all(class_='article_teaser_body'))[0].text)

    url1='https://www.jpl.nasa.gov'
    url2='/spaceimages/?search=&category=Mars'
    browser.visit((url1+url2))
    html1=browser.html
    button = browser.find_by_id('full_image')
    button.click()
    soup1=bs(html1,'html.parser')
    imgsrc=soup1.footer.a['data-fancybox-href']
    featured_image_url=url1+imgsrc
    
    url='https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html=browser.html
    soup=bs(html,'html.parser')
    mars_weather=soup.find('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text

    url2='https://space-facts.com/mars/'
    browser.visit(url2)
    html=browser.html
    soup=bs(html,'html.parser')
    table=soup.find_all('table')[0]
    tabledata=pd.read_html(str(table))
    tabledf=tabledata[0]
    tabledf.rename(columns={0:'Description',1:''},inplace=True)
    tabledf.set_index('Description')
    tablehtml=tabledf.to_html()

    url3='https://astrogeology.usgs.gov'
    url4='/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url3+url4)
    html2=browser.html
    soup=bs(html2,'html.parser')
    marshemi=soup.find_all('a',class_='itemLink product-item')
    urllist=[]
    for i in [1,3,5,7]:
        urllist.append(url3+marshemi[i]['href'])

    hemisphere_image_urls = [
        {"title": "", "img_url": ""},
        {"title": "", "img_url": ""},
        {"title": "", "img_url": ""},
        {"title": "", "img_url": ""},
    ]

    for j in range(len(urllist)):
        
        browser.visit(urllist[j])
        html1=browser.html
        soup1=bs(html1,'html.parser')
        imgsrc=soup1.find_all('img',class_='wide-image')[0]['src']
        hemisphere_image_urls[j]['img_url']=url3+imgsrc
        hemisphere_image_urls[j]['title']=marshemi[((j*2)+1)].h3.text

    results_dict = {"Mars_News_Titles":titletext,
        "Mars_News_Paragraphs":paratext,
        "Main_Image":featured_image_url,
        "Mars_Weather":mars_weather,
        "Mars_Details_inTablehtml":tablehtml,
        "Hemisphere_Images":hemisphere_image_urls
        }
    # Close the browser after scraping
    browser.quit()
    return(results_dict)





