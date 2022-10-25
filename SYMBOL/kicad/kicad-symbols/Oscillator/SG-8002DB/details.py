
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "SG-8002DB"
    hexID = "SZKOCSSG82DB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'SG-8002DB', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SeikoEpson_SG-8002DB', 'kicadSymbolDatasheet': 'https://support.epson.biz/td/api/doc_check.php?dl=brief_SG-8002DB&lang=en', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'Crystal Clock Oscillator, DIP14-style plastic package', 'kicadSymbolki_fp_filters': 'Oscillator*SeikoEpson*SG?8002DB*'}])
    newPart['name'].append('Oscillator : SG-8002DB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

