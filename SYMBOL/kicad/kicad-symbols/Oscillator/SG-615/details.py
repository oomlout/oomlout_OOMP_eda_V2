
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "SG-615"
    hexID = "SZKOCSSG615"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SG-8002JA', 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'SG-615', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_SeikoEpson_SG8002JA-4Pin_14.0x8.7mm', 'kicadSymbolDatasheet': 'https://support.epson.biz/td/api/doc_check.php?mode=dl&lang=en&Parts=SG-51P', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'CMOS Clock Oscillator', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*SeikoEpson*SG8002JA*14.0x8.7mm*'}])
    newPart['name'].append('Oscillator : SG-615')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

