
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TLP3023"
    hexID = "SZKISOLATORTLP323"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLP3021', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP3023', 'kicadSymbolFootprint': 'Package_DIP:Toshiba_11-7A9', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=1421&prodName=TLP3021(S)', 'kicadSymbolki_keywords': 'Photo-Triac Opto Triac', 'kicadSymbolki_description': 'Photo-Triac, Vdrm 400V, Ift 5mA, DIP6', 'kicadSymbolki_fp_filters': 'Toshiba*11?7A9*'}])
    newPart['name'].append('Isolator : TLP3023')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

