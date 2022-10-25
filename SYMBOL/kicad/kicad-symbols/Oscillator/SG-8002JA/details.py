
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "SG-8002JA"
    hexID = "SZKOCSSG82JA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'SG-8002JA', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_SeikoEpson_SG8002JA-4Pin_14.0x8.7mm', 'kicadSymbolDatasheet': 'https://support.epson.biz/td/api/doc_check.php?mode=dl&lang=en&Parts=SG-8002DC', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'CMOS Clock Oscillator', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*SeikoEpson*SG8002JA*14.0x8.7mm*'}])
    newPart['name'].append('Oscillator : SG-8002JA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

