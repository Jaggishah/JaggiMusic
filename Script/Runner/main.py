from Helpers.scrapping import Scrathers
from Helpers.logger import setup_logger
from Helpers.variables import DATABASE_URL, SINGLE_IDENTIFIER, DB_STRING
from Helpers.CRUD import MongoDBClient

logger = setup_logger()
scrather = Scrathers()
# uri=DB_STRING
dbConnection = MongoDBClient()

class Main:
    def __init__(self):
        dbConnection.connect(logger)
        for i in range(10,0,-1):
            self.fetching(i)
        dbConnection.close(logger=logger)
       

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
                    "title" : text.split('-')[1] if len(text.split('-')) == 2 else text,
                    "artist" : text.split('-')[0] if len(text.split('-')) == 2 else text,
                    "artwork" : scrather.getImage(new_page),
                    "url" : scrather.getLinks(new_page)
                    }
                songs.append(songs_data)
        logger.info("fetching song - " + str(songs))
        dbConnection.insert_data("single_track",songs[::-1],logger)
        logger.info("fetching end with insertion.... " )

    

  