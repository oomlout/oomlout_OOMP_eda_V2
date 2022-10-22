
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LTC6082xGN"
    hexID = "SZKAMPLIFIEROPERATIONALLTC682XGN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC6082xGN', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/60812fd.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'quad opamp', 'kicadSymbolki_description': 'Precision Quad CMOS Rail-to-Rail Input/Output Amplifiers, SSOP-16', 'kicadSymbolki_fp_filters': 'SSOP*3.9x4.9mm*P0.635mm* SOIC*3.9x9.9mm*P1.27mm* QSOP*3.9x4.9mm*P0.635mm*'}])
    newPart['name'].append('LTC6082xGN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

