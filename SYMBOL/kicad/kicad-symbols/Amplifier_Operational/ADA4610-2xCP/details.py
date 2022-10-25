
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "ADA4610-2xCP"
    hexID = "SZKAMPLIFIEROPERATIONALADA4612XCP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADA4610-2xCP', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-8-1EP_3x3mm_P0.5mm_EP1.6x2.34mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADA4610-1_4610-2_4610-4.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'dual opamp', 'kicadSymbolki_description': 'Dual Low Noise, Precision, Rail-to-Rail Output, JFET Op Amp, LFCSP-8', 'kicadSymbolki_fp_filters': 'LFCSP*3x3mm*P0.5mm*EP1.6x2.34mm*'}])
    newPart['name'].append('Amplifier_Operational : ADA4610-2xCP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

