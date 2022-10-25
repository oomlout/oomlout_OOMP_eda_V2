
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "NUP4202"
    hexID = "SZKPOWERPROTECTIONNUP422"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NUP4202', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/NUP4202W1-D.PDF', 'kicadSymbolki_keywords': 'ESD Protection diodes  transient suppressor', 'kicadSymbolki_description': 'Transient voltage suppressor designed to protect high speed data lines from ESD, EFT, and lightning', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('Power_Protection : NUP4202')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

