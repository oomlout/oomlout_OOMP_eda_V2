
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "PAM2305BJE280"
    hexID = "SZKREGULATORSWITCHINGPAM235BJE28"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PAM2305BJE330', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PAM2305BJE280', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_3x3mm_P0.5mm_EP1.7x1.7mm', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/PAM2305.pdf', 'kicadSymbolki_keywords': 'Voltage regulator switching buck fixed output analog', 'kicadSymbolki_description': '1A, Step-Down DC/DC-Converter, 2.8V Fixed Output Voltage, 1.5MHz, QFN-16', 'kicadSymbolki_fp_filters': 'QFN*EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('PAM2305BJE280')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

