
import requests
from lxml import html

class Scrathers:
    def getHtmlContent(self,url, Xpath):
        response = requests.get(url)
        tree = html.fromstring(response.content)
        if Xpath:
            return  tree.xpath(Xpath)
        return tree

    def getImage(self,tree):
        img_tags = tree.xpath("//img")
        for img in img_tags:
            src = img.get("src")  
            if src and "covers" in src:
                return src
        return None
            
    def getLinks(self,tree):
        anchor_tags = tree.xpath("//a")
        links = []
        for anchor in anchor_tags:
            href = anchor.get("href") 
            if href and  href.endswith(".mp3"):
                links.append(href)
        
        return links if len(links) > 0 else None