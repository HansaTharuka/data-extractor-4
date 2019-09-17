# -*- coding: utf-8 -*-

def extractdata():
    from selenium import webdriver
    import shutil
    import requests
    import codecs
    import re
    
    import sys
    sys.path.append("")
    from mongotest import insert_data
    
    driver = webdriver.Chrome(executable_path=r'C:/src/chromedriver_win32/chromedriver.exe' )
    driver.get('https://mbasic.facebook.com')
    
    email = driver.find_element_by_id("m_login_email")
    email.send_keys('madhavi.r.jayasinghe@gmail.com\t')
    
    password = driver.find_element_by_xpath('html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/div[2]/form/ul/li[2]/div/input')
    password.send_keys('madhavi.7\n')
    
    j = 1 #for the image and comment file naming
    myallcomments=''
    
    link_file = codecs.open("E:/Projects/Client/data-extractor-4/Links/links.txt", "r", "utf8")
    links = link_file.readlines()
    link_file.close()
    
    for link in links:
        driver.get(link)    
        for ii in range(5):
            
            img = driver.find_elements_by_tag_name('img')[1]
            src = img.get_attribute('src')
            print(src)
            response = requests.get(src, stream=True)
            outfile = open('E:/Projects/Client/data-extractor-4/Azure/{0}.jpg'.format(j), 'wb') #filename should be changed to increment gradually
            shutil.copyfileobj(response.raw, outfile)
            del response
            outfile.close()
    
    #       for pages        
            desc = driver.title
            
            start = desc.find('Promo Code') + 13
            end = desc.find('Valid', start)
    # =============================================================================
    #         promocode= desc[start:end]
    #         promocode = promocode + "\n\n" + desc.split('Valid')[1].split('T&C')[0]
    # =============================================================================
            
            url = driver.current_url
            
            publisheddate = driver.find_element_by_css_selector("#MPhotoContent > div._2vj7._2phz.acw.apl > div.desc.attachment.mfss > span > div > div > abbr").text
            reactLink = driver.find_elements_by_xpath("//div/div/div[2]/div/div/div/div/div[3]/div[2]/div/div/div[2]/a")
            
            reactCountText = ""
                    
            if(len(reactLink)!=0 and reactLink[0].text ):
                reactLink[0].click()
                reactCount = driver.find_elements_by_xpath("//div/div/div[2]/div/table/tbody/tr/td/div/div/a")
                
                for element in reactCount:
                    imgElements = element.find_elements_by_xpath(".//img")
                    if(len(imgElements) != 0):
                        reactCountText = reactCountText + " " + imgElements[0].get_attribute("alt")
                        reactCountText = reactCountText + " " + element.find_elements_by_xpath(".//span")[0].text + "\n"
                    
                    
                driver.execute_script("window.history.go(-1)")
            else:
                reactCountText = "No Reacts"
            
    # =============================================================================
    #         desc = desc + " \n\n" + url
    #         desc = desc + " \n\n" + publisheddate
    # =============================================================================
            from datetime import date
            from bson import ObjectId
            today = ''.format(date.today())
            data3 ={"idno":str(ii+1),"ocrtext":"","description":desc,"sourceurl":url,"extracteddate":publisheddate,"extracteddate":today}
            insert_data(data3)
            
# =============================================================================
#             desc_file = codecs.open("E:/Projects/Client/data-extractor-4/ExtractedData/Descriptions/desc{0}.txt".format(j), "w+", "utf16")
#             desc_file.write(desc)
#             desc_file.close()
# =============================================================================
            caption = ''
            
            next = driver.find_elements_by_link_text('Next')[0].get_attribute('href')
            allComments = ''
            comments = ''
            commentsWithReplies = ''
            
            while True:
                try:       
                    comments = driver.find_element_by_xpath('//div/div/div[2]/div/div/div/div/div[3]/div[2]/div/div/div[4]').text   
                except:
                    try:
                        comments = driver.find_element_by_xpath('//div/div/div[2]/div/div/div[2]/div/div[5]').text
                    except:
                        break
            
    
                moreComments = driver.find_elements_by_partial_link_text('View more comments')
                if len(moreComments) > 0:
                    more = moreComments[0].get_attribute("href")
    
                
                repliedCount = driver.find_elements_by_partial_link_text("replied")            
                allReplies = []            
                replyLinks = []
                for replied in repliedCount:
                    replyLinks.append(replied.get_attribute("href"))
                
                for l in replyLinks:
                    replies = ''
                    driver.get(l)
                    while True:
                        prevRep = driver.find_elements_by_partial_link_text("View previous replies")
                        if len(prevRep) > 0:
                            prevRep[0].click()
                            continue
                        else:
                            break
                    while True:                        
                        replies = replies + driver.find_element_by_xpath('//div/div/div[2]/div/div/div[3]').text
                        nextRep = driver.find_elements_by_partial_link_text("View next replies")
                        if len(nextRep) > 0:
                            nextRep[0].click()
                            continue
                        else:
                            break                
                    allReplies.append(replies)
                
                addLen = 0
                commentsWithReplies = comments
                
                for indx, indAt in enumerate(re.finditer("replied .", comments)):
                    appendPos = indAt.end() + addLen
                    commentsWithReplies = commentsWithReplies[:appendPos] + ' { '+ allReplies[indx] + ' } ' + commentsWithReplies[appendPos:]
                    addLen = addLen + 6 + len(allReplies[indx])
                
                allComments = allComments + commentsWithReplies
                
                
                if len(moreComments) > 0:
                    driver.get(more)
                    continue
                else:
                    print(allComments)
# =============================================================================
#                     comment_file = codecs.open("E:/Projects/Client/data-extractor-4/ExtractedData/Comment/cmt{0}.txt".format(j), "w+", "utf16") #file name should be changed to increment
#                     comment_file.write(allComments)
#                     comment_file.close()
# =============================================================================
                    break
               
    
            j = j + 1
            driver.get(next)
    
    driver.close()

extractdata()
    
