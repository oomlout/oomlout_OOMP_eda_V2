
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "SG-3030CM"
    hexID = "SZKOCSSG33CM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'SG-3030CM', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_SeikoEpson_SG3030CM', 'kicadSymbolDatasheet': 'https://support.epson.biz/td/api/doc_check.php?mode=dl&lang=en&Parts=SG-3030CM', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': '32.768kHz Crystal Oscillator (SPXO)', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*SeikoEpson*SG3030CM*'}])
    newPart['name'].append('SG-3030CM')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

