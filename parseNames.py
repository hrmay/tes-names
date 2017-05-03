from bs4 import BeautifulSoup
import requests
import re

games = ("Arena", "Daggerfall", "Redguard", "Morrowind", "Shadowkey", "Oblivion", "Skyrim", "Online", "Legends", "Out-of-Game Books", "Lore")

def filterNames(sections):
    
    namesList = list()
    
    for section in sections:
            #clean out all the junk HTML
            section = re.sub(r"\n", ", ", section)
            section = re.sub(r"</?h[0-9]>", "", section)
            section = re.sub(r"[eE]dit<", "<", section)
            section = re.sub(r"</?[ap(br)(sup)(div)][^>]*>", "", section)
            section = re.sub(r"[0-9]+x: ", "", section)
            section = re.sub(r"\n", ", ", section)
            section = re.sub(r"( )*\([ 0-9\,(tomb)\?]*\)", "", section)
            section = re.sub(r"/", ", ", section)
            section = re.sub(r"[^a-zA-Z(\, )\-']*", "", section)
            section = re.sub(r"\([ a-zA-Z]+\)", "", section)
            section = re.sub(r"([a-df-z])( [A-Z])", r"\1,\2", section)
            section = re.sub(r"\-\-(.)*", "", section)
            section = re.sub(r"'", "''", section)
            
            #Split into names
            names = section.split(", ")
            
            #Get rid of things that slip by for whatever reason
            names = [x for x in names if x not in games]
            names = [x for x in names if "Names" not in x]
            names = [x for x in names if len(x) <= 40]
            names = [x.strip() for x in names]
            names = [x for x in names if "Male" not in x and "Female" not in x and "Family"
                not in x and "Clan" not in x and "clan" not in x and "Title" not in x and "modified" not in x]
            names = [x for x in names if x != "at" and x!= "Most"]
            names = [x for x in names if "Nord" not in x]
            
            #Get rid of empty values
            names = filter(None, names)
            namesList.append(names)
            
    return namesList
    
    

def parseNames(url, keep):
    r = requests.get(url)

    data = r.text
    
    soup = BeautifulSoup(data, "html5lib")
    
    for table in soup.find_all("table"):
        table.decompose()
        
    for small in soup.find_all("small"):
        small.decompose()
    
    soup.find("div", id="footer").decompose()
    
    for li in soup.find_all("li"):
        li.decompose()
    
    for ul in soup.find_all("ul"):
        ul.decompose()
       
        
    for bold in soup.find_all("b"):
        bold.decompose()
        
    for h3 in soup.find_all("h3"):
        h3.decompose()
    
    #Grab each section: male, female, and family
    sections = re.split(r"<h2[^>]*>", str(soup))
    sections = [x for x in sections if sections.index(x) in keep]

    
    namesList = filterNames(sections)
    
    #namesSet = set(namesList)
    
    return namesList;