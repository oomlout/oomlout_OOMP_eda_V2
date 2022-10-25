
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA847xD"
    hexID = "SZKAMPLIFIEROPERATIONALOPA847XD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'OPA890xD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA847xD', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/opa847.pdf', 'kicadSymbolki_keywords': 'single opamp wideband low-power', 'kicadSymbolki_description': 'Single Low-Power, 3.9GHz, Wideband, Ultra-Low Noise, Voltage-Feedback Operational Amplifier with Disable, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Operational : OPA847xD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

