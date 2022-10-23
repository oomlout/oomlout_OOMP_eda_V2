
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "TXC-7C"
    hexID = "SZKOCSTXC7C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'TXC-7C', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_TXC_7C-4Pin_5.0x3.2mm', 'kicadSymbolDatasheet': 'http://www.txccorp.com/download/products/osc/7C_o.pdf', 'kicadSymbolki_keywords': 'CMOS SMD Crystal Clock Oscillator', 'kicadSymbolki_description': 'CMOS SMD Crystal Clock Oscillator, TXC', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*TXC*7C*5.0x3.2mm*'}])
    newPart['name'].append('TXC-7C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

