
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "ADA4610-4xCP"
    hexID = "SZKAMPLIFIEROPERATIONALADA4614XCP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADA4610-4xCP', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADA4610-1_4610-2_4610-4.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'quad opamp', 'kicadSymbolki_description': 'Quad Low Noise, Precision, Rail-to-Rail Output, JFET Op Amp, LFCSP-16', 'kicadSymbolki_fp_filters': 'LFCSP*4x4mm*P0.65mm*EP2.1x2.1mm*'}])
    newPart['name'].append('ADA4610-4xCP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

