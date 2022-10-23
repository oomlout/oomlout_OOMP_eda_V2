
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Switch"
    oIndex = "HMC7992"
    hexID = "SZKRFSWITCHHMC7992"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HMC7992', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-16-1EP_3x3mm_P0.5mm_EP1.7x1.7mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/HMC7992.pdf', 'kicadSymbolki_keywords': 'rf switch sp4t absorptive', 'kicadSymbolki_description': 'SP4T 100MHz-6GHz absorptive switch, 50 Ohm, LFCSP-16', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('HMC7992')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

