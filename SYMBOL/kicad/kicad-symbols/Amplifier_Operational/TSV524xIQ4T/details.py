
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "TSV524xIQ4T"
    hexID = "SZKAMPLIFIEROPERATIONALTSV524XIQ4T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSV524xIQ4T', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_3x3mm_P0.5mm_EP1.7x1.7mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/tsv521.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'quad opamp', 'kicadSymbolki_description': 'Quad CMOS Rail-to-Rail Input/Output Amplifier, 1.15MHz GBP, QFN-16', 'kicadSymbolki_fp_filters': 'QFN*3x3mm*P0.5mm*EP1.7x1.7mm*'}])
    newPart['name'].append('TSV524xIQ4T')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

