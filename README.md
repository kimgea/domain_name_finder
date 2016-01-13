# domain_name_finder
Scrape the web for new and popular words and check if their domain names are taken.

**Notes**
This code is unfinished but should work. It was written fast and has parts that looks bad because of it. IT WILL NOT B FINISHED.

**Requirements**
I have not made a file for this. But you need pymongo and scrapy. 



**domain_name_scraper**
scrapes popular, trending and strange words from different sources. They will later be made to domain names and checked if they are free or taken.

**SETUP domain_name_scraper**
- config mongodb in settings
- then it should just be to run the spiders - scrappy crawl urbandict or some thin like that

**TODO domain_name_scraper**
- Clean up code and add documentation
- Add spiders from other places
- Do not add words that exist in db

**domainfinder**
Get wors collected in mogodb, make domain names from it, and checks if they are free. 

**SETUP domainfinder**
- Check if mongodp config in run.py are correct
- python run.py

**TODO domainfinder**
- Add functions thath checks domain by using other websites, so not to tax only one site
- Clean up code and add comments/documentation
- db for domain names hat are checked, and do not check checked names again
- make a better domainmaker.py that tryes diferent combinations. test.com tests.com te.st ....
