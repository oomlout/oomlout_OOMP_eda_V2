
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA1692xD"
    hexID = "SZKAMPLIFIEROPERATIONALOPA1692XD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCS2325D', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA1692xD', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/opa1692.pdf', 'kicadSymbolki_keywords': 'VFA opamp', 'kicadSymbolki_description': 'Dual SoundPlus Low Power, Low Noise & Low Distortion Audio Operational Amplifiers, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Operational : OPA1692xD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

