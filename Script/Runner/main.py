from Helpers.scrapping import Scrathers
from Helpers.logger import setup_logger
from Helpers.variables import DATABASE_URL, SINGLE_IDENTIFIER

logger = setup_logger()
scrather = Scrathers()

class Main:
    def __init__(self):
       for i in range(1,11):
        self.fetching(i)

    def fetching(self,i : int ):
        url = f"{DATABASE_URL}{i}"
        anchor_tags = scrather.getHtmlContent(
            url,
            "//a"
        )
        songs = []
        logger.info("fetching website starting..")
        for anchor in anchor_tags:
            href = anchor.get("href") 
        
            if href.startswith(SINGLE_IDENTIFIER):
                text = anchor.text_content().strip()  # Get the text content
                
                new_page = scrather.getHtmlContent(href,None)
                songs_data = {
                    "name" : text,
                    "artwork" : scrather.getImage(new_page),
                    "links" : scrather.getLinks(new_page)
                    }
                logger.info("fetching song - " + str(songs_data))
                songs.append(songs_data)
        logger.info("fetching end.... " )

    

  