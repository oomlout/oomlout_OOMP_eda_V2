
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "FFB2227A"
    hexID = "SZKTRANSISTORBJTFFB2227A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC846BPN', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FFB2227A', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/FMB2227A-D.PDF', 'kicadSymbolki_keywords': 'NPN/PNP Transistor', 'kicadSymbolki_description': '500mA IC, 30V Vce, Dual NPN/PNP Transistors, SC-70-6', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('FFB2227A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

