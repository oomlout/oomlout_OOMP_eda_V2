
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "MAX712MJE"
    hexID = "SZKBATMANAGEMENTMAX712MJE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX712CPE', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX712MJE', 'kicadSymbolFootprint': 'Package_DIP:DIP-16_W7.62mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX712-MAX713.pdf', 'kicadSymbolki_keywords': 'Fast-charge Nickel Metal Hydride (NiMH) from a DC source, ceramic, -55 to +125 Degree Celsius, PDIP-16', 'kicadSymbolki_description': 'Fast-charge Nickel Metal Hydride (NiMH) from a DC source, ceramic, -55 to +125 Degree Celsius, PDIP-16', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MAX712MJE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

