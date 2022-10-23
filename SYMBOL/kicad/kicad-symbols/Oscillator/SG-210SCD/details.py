
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "SG-210SCD"
    hexID = "SZKOCSSG21SCD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SG-210SED', 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'SG-210SCD', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_SeikoEpson_SG210-4Pin_2.5x2.0mm', 'kicadSymbolDatasheet': 'https://support.epson.biz/td/api/doc_check.php?mode=dl&lang=en&Parts=SG-210SED', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'Crystal Oscillator Low Profile / High Stability SPXO', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*SeikoEpson*SG210*2.5x2.0mm*'}])
    newPart['name'].append('SG-210SCD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

