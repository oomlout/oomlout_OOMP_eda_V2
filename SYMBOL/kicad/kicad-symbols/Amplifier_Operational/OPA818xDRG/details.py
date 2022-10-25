
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA818xDRG"
    hexID = "SZKAMPLIFIEROPERATIONALOPA818XDRG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA818xDRG', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_3x3mm_P0.5mm_EP1.45x2.4mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/opa818.pdf', 'kicadSymbolki_keywords': 'opamp VFA', 'kicadSymbolki_description': ' 2.7 GHz, High-Voltage, FET-Input, Low Noise, Operational Amplifier, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*1EP*3x3mm*EP1.45x2.4mm*'}])
    newPart['name'].append('Amplifier_Operational : OPA818xDRG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

