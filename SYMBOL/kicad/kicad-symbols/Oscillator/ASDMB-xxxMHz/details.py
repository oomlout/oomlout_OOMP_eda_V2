
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "ASDMB-xxxMHz"
    hexID = "SZKOCSASDMBXXXMHZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ASDMB-xxxMHz', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_Abracon_ASDMB-4Pin_2.5x2.0mm', 'kicadSymbolDatasheet': 'https://abracon.com/Oscillators/ASDMB.pdf', 'kicadSymbolki_keywords': '1.8-3.3V SMD Ultra Miniature Crystal Clock Oscillator', 'kicadSymbolki_description': '1.8-3.3V SMD Ultra Miniature Crystal Clock Oscillator, Abracon', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*Abracon*ASDMB*2.5x2.0mm*'}])
    newPart['name'].append('ASDMB-xxxMHz')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

