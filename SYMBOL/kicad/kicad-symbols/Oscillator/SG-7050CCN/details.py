
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "SG-7050CCN"
    hexID = "SZKOCSSG75CCN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SG-8002CA', 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'SG-7050CCN', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_SeikoEpson_SG8002CA-4Pin_7.0x5.0mm', 'kicadSymbolDatasheet': 'https://support.epson.biz/td/api/doc_check.php?dl=brief_SG7050CAN&lang=en', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'CMOS Clock Oscillator 2.5 to 50 MHz', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*SeikoEpson*SG8002CA*7.0x5.0mm*'}])
    newPart['name'].append('Oscillator : SG-7050CCN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

