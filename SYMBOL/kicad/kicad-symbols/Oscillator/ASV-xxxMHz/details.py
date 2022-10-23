
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "ASV-xxxMHz"
    hexID = "SZKOCSASVXXXMHZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'ASV-xxxMHz', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_Abracon_ASV-4Pin_7.0x5.1mm', 'kicadSymbolDatasheet': 'http://www.abracon.com/Oscillators/ASV.pdf', 'kicadSymbolki_keywords': '3.3V HCMOS SMD Crystal Clock Oscillator', 'kicadSymbolki_description': '3.3V HCMOS SMD Crystal Clock Oscillator, Abracon', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*Abracon*ASV*7.0x5.1mm*'}])
    newPart['name'].append('ASV-xxxMHz')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

