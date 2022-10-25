
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "SG-531"
    hexID = "SZKOCSSG531"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SG-8002DC', 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'SG-531', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SeikoEpson_SG-8002DC', 'kicadSymbolDatasheet': 'https://support.epson.biz/td/api/doc_check.php?mode=dl&lang=en&Parts=SG-51P', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'CMOS Crystal Clock Oscillator, DIP8-style plastic package', 'kicadSymbolki_fp_filters': 'Oscillator*SeikoEpson*SG?8002DC*'}])
    newPart['name'].append('Oscillator : SG-531')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

