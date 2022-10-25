
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "THS3491xDDA"
    hexID = "SZKAMPLIFIEROPERATIONALTHS3491XDDA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'THS3491xDDA', 'kicadSymbolFootprint': 'Package_SO:Texas_R-PDSO-G8_EP2.95x4.9mm_Mask2.4x3.1mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ths3491.pdf', 'kicadSymbolki_keywords': 'opamp single current feedback wideband', 'kicadSymbolki_description': '900-MHz, 500-mA High-Power Output Current Feedback Operational Amplifier, SOIC-8', 'kicadSymbolki_fp_filters': 'Texas*R*PDSO*G8*EP*'}])
    newPart['name'].append('Amplifier_Operational : THS3491xDDA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

