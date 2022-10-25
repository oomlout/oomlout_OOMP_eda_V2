
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "SG-5032CCN"
    hexID = "SZKOCSSG532CCN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SG-8002LB', 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'SG-5032CCN', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_SeikoEpson_SG8002LB-4Pin_5.0x3.2mm', 'kicadSymbolDatasheet': 'https://support.epson.biz/td/api/doc_check.php?dl=brief_SG5032CCN&lang=en', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'CMOS Clock Oscillator 2.5 to 50 MHz', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*SeikoEpson*SG8002LB*5.0x3.2mm*'}])
    newPart['name'].append('Oscillator : SG-5032CCN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

