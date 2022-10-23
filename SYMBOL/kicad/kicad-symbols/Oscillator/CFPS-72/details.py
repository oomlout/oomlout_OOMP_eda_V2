
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "CFPS-72"
    hexID = "SZKOCSCFPS72"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'CFPS-72', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_IQD_IQXO70-4Pin_7.5x5.0mm', 'kicadSymbolDatasheet': 'https://www.iqdfrequencyproducts.com/products/details/cfps-72-14-01.pdf', 'kicadSymbolki_keywords': 'XO', 'kicadSymbolki_description': '500kHz-100MHz 5V Crystal Oscillator, IQD CFPS-72', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*IQD*IQXO70*7.5x5.0mm*'}])
    newPart['name'].append('CFPS-72')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

