
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TLP3021"
    hexID = "SZKISOLATORTLP321"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP3021', 'kicadSymbolFootprint': 'Package_DIP:Toshiba_11-7A9', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=1421&prodName=TLP3021(S)', 'kicadSymbolki_keywords': 'Photo-Triac Opto Triac', 'kicadSymbolki_description': 'Photo-Triac, Vdrm 400V, Ift 15mA, DIP6', 'kicadSymbolki_fp_filters': 'Toshiba*11?7A9*'}])
    newPart['name'].append('TLP3021')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

