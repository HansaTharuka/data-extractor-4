# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:27:03 2019

@author: Viva
"""

from selenium import webdriver
import shutil
import requests
import codecs
import re

driver = webdriver.Chrome(executable_path=r'C:/src/chromedriver_win32/chromedriver.exe' )
driver.get('https://mbasic.facebook.com')

email = driver.find_element_by_id("m_login_email")
email.send_keys('nirmaldarshana1234@gmail.com\t')

password = driver.find_element_by_xpath('html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/div[2]/form/ul/li[2]/div/input')
password.send_keys('n3n4d3d4\n')

j = 2146 #for the image and comment file naming

link_file = codecs.open("Links/links.txt", "r", "utf8")
links = link_file.readlines()
link_file.close()

for link in links:
    
    #should come in a loop: start loop 1
    driver.get(link)
    
    #first_post = driver.find_elements_by_tag_name('a')[26]
    #img_class = first_post.get_attribute('class') 
    
#    for x in range(40):
##    while(True):
#        img_posts = driver.find_elements_by_xpath("//*[contains(@alt, 'Image may contain')]/parent::a")
#        
#        #start loop 2
#        for i in range(len(img_posts)):
#            img_posts[i].click()
#            img = driver.find_elements_by_tag_name('img')[1]
#            src = img.get_attribute('src')
#            
#            response = requests.get(src, stream=True)
#            outfile = open('img{0}.jpg'.format(j), 'wb') #filename should be changed to increment gradually
#            shutil.copyfileobj(response.raw, outfile)
#            del response
#            outfile.close()
#            try:       
#                comments = driver.find_element_by_xpath('//div/div/div[2]/div/div/div/div/div[3]/div[2]/div/div/div[4]').text   
#                comment_file = codecs.open("cmt{0}.txt".format(j), "w+", "utf16") #file name should be changed to increment
#                comment_file.write(comments)
#                comment_file.close()
#            except:
#                comments = driver.find_element_by_xpath('//div/div/div[2]/div/div/div[2]/div/div[5]').text   
#                comment_file = codecs.open("cmt{0}.txt".format(j), "w+", "utf16") #file name should be changed to increment
#                comment_file.write(comments)
#                comment_file.close()        
#            finally:
#                driver.execute_script("window.history.go(-1)")
#                img_posts = driver.find_elements_by_xpath("//*[contains(@alt, 'Image may contain')]/parent::a")
#                j = j + 1
#            
#        #end loop 2
#        show_more = driver.find_elements_by_link_text('Show more')
#        len(show_more)
#        if(len(show_more)>0):
#            show_more[0].click()
#        else:
#            break
        
        
    for ii in range(900):
        
        img = driver.find_elements_by_tag_name('img')[1]
        src = img.get_attribute('src')
        
        response = requests.get(src, stream=True)
        outfile = open('E:/Projects/Client/data-extractor-4/Images/img{0}.jpg'.format(j), 'wb') #filename should be changed to increment gradually
        shutil.copyfileobj(response.raw, outfile)
        del response
        outfile.close()

#       for pages        
        desc = driver.title
        
        url = driver.current_url
        
#       for froups
#        desc = driver.find_element_by_xpath('//div/div/div[2]/div/div/div/div/div[3]/div/div/div').text

        reactLink = driver.find_elements_by_xpath("//div/div/div[2]/div/div/div/div/div[3]/div[2]/div/div/div[2]/a")
        
        publisheddate= f= driver.find_element_by_css_selector("#MPhotoContent > div._2vj7._2phz.acw.apl > div.desc.attachment.mfss > span > div > div > abbr").text
                                                              
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
        
        desc = desc + " \n\n" + url
        desc = desc + " \n\n" + reactCountText
        desc = desc + " \n\n" + publisheddate
        
        desc_file = codecs.open("E:/Projects/Client/data-extractor-4/Descriptions/desc{0}.txt".format(j), "w+", "utf16")
        desc_file.write(desc)
        desc_file.close()
        caption = ''
        
# =============================================================================
#         next = driver.find_elements_by_link_text('Next')[0].get_attribute('href')
#         allComments = ''
#         comments = ''
#         commentsWithReplies = ''
#         
#         while True:
#             try:       
#                 comments = driver.find_element_by_xpath('//div/div/div[2]/div/div/div/div/div[3]/div[2]/div/div/div[4]').text   
#             except:
#                 try:
#                     comments = driver.find_element_by_xpath('//div/div/div[2]/div/div/div[2]/div/div[5]').text
#                 except:
#                     break
#         
# #           finally:
#                
# #                img_posts = driver.find_elements_by_xpath("//*[contains(@alt, 'Image may contain')]/parent::a")
#             moreComments = driver.find_elements_by_partial_link_text('View more comments')
#             if len(moreComments) > 0:
#                 more = moreComments[0].get_attribute("href")
# 
#             
#             repliedCount = driver.find_elements_by_partial_link_text("replied")
#             
# #            if len(replyLinks) > 0:
# #                repliedAt = re.finditer("replied .", comments)
#             
#             allReplies = []
#             
#             replyLinks = []
#             for replied in repliedCount:
#                 replyLinks.append(replied.get_attribute("href"))
#             
#             for l in replyLinks:
#                 replies = ''
#                 driver.get(l)
#                 while True:
#                     prevRep = driver.find_elements_by_partial_link_text("View previous replies")
#                     if len(prevRep) > 0:
#                         prevRep[0].click()
#                         continue
#                     else:
#                         break
#                 while True:                        
#                     replies = replies + driver.find_element_by_xpath('//div/div/div[2]/div/div/div[3]').text
#                     nextRep = driver.find_elements_by_partial_link_text("View next replies")
#                     if len(nextRep) > 0:
#                         nextRep[0].click()
#                         continue
#                     else:
#                         break                
#                 allReplies.append(replies)
#             
#             addLen = 0
#             commentsWithReplies = comments
#             
#             for indx, indAt in enumerate(re.finditer("replied .", comments)):
#                 appendPos = indAt.end() + addLen
#                 commentsWithReplies = commentsWithReplies[:appendPos] + ' { '+ allReplies[indx] + ' } ' + commentsWithReplies[appendPos:]
#                 addLen = addLen + 6 + len(allReplies[indx])
#             
#             allComments = allComments + commentsWithReplies
#             
#             if len(moreComments) > 0:
#                 driver.get(more)
#                 continue
#             else:
#                 comment_file = codecs.open("cmt{0}.txt".format(j), "w+", "utf16") #file name should be changed to increment
#                 comment_file.write(allComments)
#                 comment_file.close()
#                 break
# =============================================================================
            
        j = j + 1
        driver.get(next)

