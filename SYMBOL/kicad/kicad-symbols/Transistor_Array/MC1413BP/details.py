
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Array"
    oIndex = "MC1413BP"
    hexID = "SZKTRANSISTORARRAYMC1413BP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC1413D', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC1413BP', 'kicadSymbolFootprint': 'Package_DIP:DIP-16_W7.62mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/MC1413-D.PDF', 'kicadSymbolki_keywords': 'darlington transistor array', 'kicadSymbolki_description': 'High Voltage, High Current Darlington Transistor Arrays,  TTL/CMOS-compatible, PDIP-16', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Transistor_Array : MC1413BP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

