
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "ABLNO"
    hexID = "SZKOCSABLNO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'ABLNO', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_Abracon_ABLNO', 'kicadSymbolDatasheet': 'https://abracon.com/Precisiontiming/ABLNO.pdf', 'kicadSymbolki_keywords': 'XO VCXO', 'kicadSymbolki_description': 'LVCMOS Ultra Low Phase Noise XO / VCXO, Abracon ABLNO', 'kicadSymbolki_fp_filters': 'Oscillator*Abracon*ABLNO*'}])
    newPart['name'].append('ABLNO')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

