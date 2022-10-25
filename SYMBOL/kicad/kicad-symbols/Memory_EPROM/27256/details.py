
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EPROM"
    oIndex = "27256"
    hexID = "SZKMEMORYEPROM27256"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '27C256', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '27256', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W15.24mm', 'kicadSymbolDatasheet': 'http://datasheet.octopart.com/D27256-2-Intel-datasheet-17852618.pdf', 'kicadSymbolki_keywords': 'Erasable EPROM 256 KiBit', 'kicadSymbolki_description': 'UV Erasable EPROM 256 KiBit, [Obsolete 2000-11]', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('Memory_EPROM : 27256')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

