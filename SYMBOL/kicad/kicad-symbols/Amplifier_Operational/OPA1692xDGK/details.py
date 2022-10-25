
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA1692xDGK"
    hexID = "SZKAMPLIFIEROPERATIONALOPA1692XDGK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'OPA2197xDGK', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA1692xDGK', 'kicadSymbolFootprint': 'Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/opa1692.pdf', 'kicadSymbolki_keywords': 'VFA opamp', 'kicadSymbolki_description': 'Dual SoundPlus Low Power, Low Noise & Low Distortion Audio Operational Amplifiers, VSSOP-8', 'kicadSymbolki_fp_filters': 'VSSOP*3.0x3.0mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Operational : OPA1692xDGK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

