
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "MAX713ESE"
    hexID = "SZKBATMANAGEMENTMAX713ESE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX712CSE', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX713ESE', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX712-MAX713.pdf', 'kicadSymbolki_keywords': 'Fast-charge Nickel Cadmium (NiCd) from a DC source, -40 to +85 Degree Celsius, SOIC-16', 'kicadSymbolki_description': 'Fast-charge Nickel Cadmium (NiCd) from a DC source, -40 to +85 Degree Celsius, SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9mm*P1.27mm*'}])
    newPart['name'].append('MAX713ESE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

