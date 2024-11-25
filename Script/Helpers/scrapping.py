
import requests
from lxml import html

class Scrathers:
    def getHtmlContent(self,url, Xpath):
        try: 
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            tree = html.fromstring(response.content)
            if Xpath:
                return  tree.xpath(Xpath)
            return tree
        except requests.exceptions.Timeout:
            print(f"Error: The request to {url} timed out.")
        except requests.exceptions.RequestException as e:
            print(f"Error: An error occurred while fetching {url}. Details: {e}")
        except html.ParserError as e:
            print(f"Error: Failed to parse the HTML content from {url}. Details: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return None


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