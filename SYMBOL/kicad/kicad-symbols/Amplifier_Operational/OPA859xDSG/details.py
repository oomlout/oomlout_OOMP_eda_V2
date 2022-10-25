
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA859xDSG"
    hexID = "SZKAMPLIFIEROPERATIONALOPA859XDSG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'OPA858xDSG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA859xDSG', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/opa859.pdf', 'kicadSymbolki_keywords': 'opamp VFA', 'kicadSymbolki_description': '1.8 GHz Unity-Gain Bandwidth FET Input Amplifier, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*1EP*2x2mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Operational : OPA859xDSG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

