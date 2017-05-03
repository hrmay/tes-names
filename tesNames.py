from bs4 import BeautifulSoup
import requests
import re
from parseNames import *

#ALTMER NAMES
altmerMNames, altmerFNames = parseNames("http://en.uesp.net/wiki/Lore:Altmer_Names", (2,3))

#ARGONIAN NAMES
argonianMNames, argonianFNames = parseNames("http://en.uesp.net/wiki/Lore:Argonian_Names", (3,4))

#BOSMER NAMES
bosmerMNames, bosmerFNames, bosmerSNames = parseNames("http://en.uesp.net/wiki/Lore:Bosmer_Names", (2,3,4))

#BRETON NAMES
bretonMNames, bretonFNames, bretonSNames = parseNames("http://en.uesp.net/wiki/Lore:Breton_Names", (2,3,4))

#DUNMER NAMES
dunmerMNames, dunmerFNames, dunmerSNames = parseNames("http://en.uesp.net/wiki/Lore:Dunmer_Names", (2,3,4))

#IMPERIAL NAMES
imperialMNames, imperialFNames, imperialSNames = parseNames("http://en.uesp.net/wiki/Lore:Imperial_Names", (2,3,5))

#KHAJIIT NAMES
khajiitMNames, khajiitFNames = parseNames("http://en.uesp.net/wiki/Lore:Khajiit_Names", (3,4))

#NORD NAMES
nordMNames, nordFNames, nordSNames = parseNames("http://en.uesp.net/wiki/Lore:Nord_Names", (1,2,3))

#ORC NAMES
orcMNames, orcFNames = parseNames("http://en.uesp.net/wiki/Lore:Orc_Names", (2,3))

#REDGUARD NAMES
redguardMNames, redguardFNames = parseNames("http://en.uesp.net/wiki/Lore:Redguard_Names", (1,2))

with open("tesNames.sql", 'w') as f:
    
    f.write("""-- Connect and create
\c postgres;
DROP DATABASE IF EXISTS tesNames;
CREATE DATABASE tesNames;
\c tesNames;
        
DROP TABLE IF EXISTS Names;
        
CREATE TABLE Names {
    NameID      SERIAL NOT NULL,
    Race        VARCHAR(20) NOT NULL,
    NameType    CHAR(1) NOT NULL,
    Name        VARCHAR(40) NOT NULL
};

""")

    #INPUT ALTMER NAMES
    for name in altmerMNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Altmer', 'm', '" + name + "');\n")
    for name in altmerFNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Altmer', 'f', '" + name + "');\n")
    
    #INPUT ARGONIAN NAMES
    for name in argonianMNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Argonian', 'm', '" + name + "');\n")
    for name in argonianFNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Argonian', 'f', '" + name + "');\n")
    
    #INPUT BOSMER NAMES
    for name in bosmerMNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Bosmer', 'm', '" + name + "');\n")
    for name in bosmerFNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Bosmer', 'f', '" + name + "');\n")
    for name in bosmerSNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Bosmer', 's', '" + name + "');\n")
    
    #INPUT BRETON NAMES    
    for name in bretonMNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Breton', 'm', '" + name + "');\n")
    for name in bretonFNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Breton', 'f', '" + name + "');\n")
    for name in bretonSNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Breton', 's', '" + name + "');\n")
    
    #INPUT DUNMER NAMES
    for name in dunmerMNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Dunmer', 'm', '" + name + "');\n")
    for name in dunmerFNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Dunmer', 'f', '" + name + "');\n")
    for name in dunmerSNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Dunmer', 's', '" + name + "');\n")
        
    #INPUT IMPERIAL NAMES
    for name in imperialMNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Imperial', 'm', '" + name + "');\n")
    for name in imperialFNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Imperial', 'f', '" + name + "');\n")
    for name in imperialSNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Imperial', 's', '" + name + "');\n")
        
    #INPUT KHAJIIT NAMES
    for name in khajiitMNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Khajiit', 'm', '" + name + "');\n")
    for name in khajiitFNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Khajiit', 'f', '" + name + "');\n")

    #INPUT NORD NAMES
    for name in nordMNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Nord', 'm', '" + name + "');\n")
    for name in nordFNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Nord', 'f', '" + name + "');\n")
    for name in nordSNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Nord', 's', '" + name + "');\n")
        
    #INPUT ORC NAMES
    for name in orcMNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Orc', 'm', '" + name + "');\n")
    for name in orcFNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Orc', 'f', '" + name + "');\n")
        
    #INPUT KHAJIIT NAMES
    for name in redguardMNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Redguard', 'm', '" + name + "');\n")
    for name in redguardFNames:
        f.write("INSERT INTO Names (Race, NameType, Name) VALUES ('Redguard', 'f', '" + name + "');\n")