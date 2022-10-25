
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xGxx"
    oIndex = "NC7SZ125P5X"
    hexID = "SZK74XGXXNC7SZ125P5X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NC7SZ125M5X', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NC7SZ125P5X', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pdf/datasheet/nc7sz125-d.pdf', 'kicadSymbolki_keywords': 'buffer three-state', 'kicadSymbolki_description': 'TinyLogic UHS Buffer with Three-State Output, SOT-353', 'kicadSymbolki_fp_filters': 'SOT*353*'}])
    newPart['name'].append('74xGxx : NC7SZ125P5X')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

