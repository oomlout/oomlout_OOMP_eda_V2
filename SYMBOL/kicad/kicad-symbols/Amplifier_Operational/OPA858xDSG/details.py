
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA858xDSG"
    hexID = "SZKAMPLIFIEROPERATIONALOPA858XDSG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA858xDSG', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/opa858.pdf', 'kicadSymbolki_keywords': 'opamp VFA', 'kicadSymbolki_description': '5.5-GHz Gain Bandwidth Product, Gain of 7 V/V Stable, FET Input Amplifier, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*1EP*2x2mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Operational : OPA858xDSG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

