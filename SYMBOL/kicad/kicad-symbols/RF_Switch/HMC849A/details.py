
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Switch"
    oIndex = "HMC849A"
    hexID = "SZKRFSWITCHHMC849A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HMC849A', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-16-1EP_4x4mm_P0.65mm_EP2.4x2.4mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/hmc849a.pdf', 'kicadSymbolki_keywords': 'RF SPDT switch', 'kicadSymbolki_description': 'High Isolation SPDT Non-Reflective Switch, DC-6GHz, Matched to 50 Ohm, LFCSP-16', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*4x4mm*P0.65mm*'}])
    newPart['name'].append('HMC849A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

