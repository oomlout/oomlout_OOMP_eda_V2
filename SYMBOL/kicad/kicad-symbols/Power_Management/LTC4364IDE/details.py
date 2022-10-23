
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LTC4364IDE"
    hexID = "SZKPOWERMANAGEMENTLTC4364IDE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC4364CDE', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4364IDE', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-14-1EP_3x4mm_P0.5mm_EP1.7x3.3mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/436412f.pdf', 'kicadSymbolki_keywords': 'surge overvoltage undervoltage reverse-polarity protection diode ORing MOSFET driver', 'kicadSymbolki_description': 'Surge stopper with ideal diode, UV and OV protection -40V to +80V in DFN-14 package, -40°C to +85°C', 'kicadSymbolki_fp_filters': 'DFN*3x4mm*P0.5mm*'}])
    newPart['name'].append('LTC4364IDE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

