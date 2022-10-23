
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "SG-211"
    hexID = "SZKOCSSG211"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SG-210STF', 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'SG-211', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_SeikoEpson_SG210-4Pin_2.5x2.0mm', 'kicadSymbolDatasheet': 'https://support.epson.biz/td/api/doc_check.php?mode=dl&lang=en&Parts=SG-211SEE', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'CMOS Crystal Oscillator SPXO', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*SeikoEpson*SG210*2.5x2.0mm*'}])
    newPart['name'].append('SG-211')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

