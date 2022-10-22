
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LTC6082xDHC"
    hexID = "SZKAMPLIFIEROPERATIONALLTC682XDHC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC6082xDHC', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-16-1EP_3x5mm_P0.5mm_EP1.66x4.4mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/60812fd.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'quad opamp', 'kicadSymbolki_description': 'Precision Quad CMOS Rail-to-Rail Input/Output Amplifiers, DFN-16', 'kicadSymbolki_fp_filters': 'DFN*3x5mm*P0.5mm*'}])
    newPart['name'].append('LTC6082xDHC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

