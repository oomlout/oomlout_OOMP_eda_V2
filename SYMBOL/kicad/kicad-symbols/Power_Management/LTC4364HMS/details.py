
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LTC4364HMS"
    hexID = "SZKPOWERMANAGEMENTLTC4364HMS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC4364CMS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4364HMS', 'kicadSymbolFootprint': 'Package_SO:MSOP-16_3x4mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/436412f.pdf', 'kicadSymbolki_keywords': 'surge overvoltage undervoltage reverse-polarity protection diode ORing MOSFET driver', 'kicadSymbolki_description': 'Surge stopper with ideal diode, UV and OV protection -40V to +80V in MSOP-16 package, -40°C to +125°C', 'kicadSymbolki_fp_filters': 'MSOP*3x4mm*P0.5mm*'}])
    newPart['name'].append('LTC4364HMS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

