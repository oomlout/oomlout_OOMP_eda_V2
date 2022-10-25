
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "Comchip_ACDSV6-4448TI-G"
    hexID = "SZKDIODECOMCHIPACDSV64448TIG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BAS16TW', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'Comchip_ACDSV6-4448TI-G', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.comchiptech.com/cms/UserFiles/ACDSV6-4448TI-G%20RevA285610.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Small signal switching diode array 3 independent', 'kicadSymbolki_fp_filters': '*SOT?363*'}])
    newPart['name'].append('Diode : Comchip_ACDSV6-4448TI-G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

