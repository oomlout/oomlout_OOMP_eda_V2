
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "ASE-xxxMHz"
    hexID = "SZKOCSASEXXXMHZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'ASE-xxxMHz', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_Abracon_ASE-4Pin_3.2x2.5mm', 'kicadSymbolDatasheet': 'http://www.abracon.com/Oscillators/ASV.pdf', 'kicadSymbolki_keywords': '3.3V CMOS SMD Crystal Clock Oscillator', 'kicadSymbolki_description': '3.3V CMOS SMD Crystal Clock Oscillator, Abracon', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*Abracon*ASE*3.2x2.5mm*'}])
    newPart['name'].append('ASE-xxxMHz')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

