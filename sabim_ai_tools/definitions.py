# sabim_ai_tols/definitions.py

"""Global definitions of the package"""

# Bibtex format and conventions. Here we used only specific fiels and format but it can be extend as desired. 
bibtex_format = {"type": ["article"], 
                "fields":{"title":str, "shorttitle":str, "author":str, "year":int, "month":str, "journal":str, "volume":int, "number":int, "pages":int, "publisher":str,"issn":str,"doi":str,"urldate":str,"abstract":str,"keywords":str,"file":str} }

bibtex_format_mysql = {
    "type": ["article"],
    "fields": {
        "id": "INT PRIMARY KEY AUTO_INCREMENT",          # Auto-incrementing primary key for unique identification
        "bibkey": "VARCHAR(255)",                        # BibTeX key, variable-length string
        "title": "TEXT",                                 # Title of the work, supports long text
        "shorttitle": "VARCHAR(255)",                    # Shortened title, variable-length string
        "author": "TEXT",                                # Author(s) name(s), supports long text
        "year": "YEAR",                                  # Year of publication
        "month": "VARCHAR(20)",                          # Month of publication (as a string)
        "journal": "VARCHAR(255)",                       # Name of the journal
        "volume": "INT",                                 # Volume number
        "number": "INT",                                 # Issue number
        "pages": "VARCHAR(50)",                          # Page range (e.g., "123-130")
        "publisher": "VARCHAR(255)",                     # Name of the publisher
        "issn": "VARCHAR(20)",                           # ISSN number
        "doi": "VARCHAR(255)",                           # DOI (Digital Object Identifier)
        "urldate": "DATE",                               # URL access date
        "abstract": "TEXT",                              # Abstract of the article
        "keywords": "TEXT",                              # Keywords, typically stored as a text field
        "file": "VARCHAR(255)"                           # Path or filename of the associated file
    }
}

