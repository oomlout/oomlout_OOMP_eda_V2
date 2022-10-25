
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "CM1213A-01SO"
    hexID = "SZKPOWERPROTECTIONCM1213A1SO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'CM1213A-01SO', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/CM1213A-D.PDF', 'kicadSymbolki_keywords': 'ESD Protection diodes transient suppressor', 'kicadSymbolki_description': 'Single Channel ESD Protection Array', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Power_Protection : CM1213A-01SO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

