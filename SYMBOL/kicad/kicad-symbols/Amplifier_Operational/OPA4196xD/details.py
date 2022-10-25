
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA4196xD"
    hexID = "SZKAMPLIFIEROPERATIONALOPA4196XD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'OPA4197xD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA4196xD', 'kicadSymbolFootprint': 'Package_SO:SOIC-14_3.9x8.7mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/opa4196.pdf', 'kicadSymbolki_keywords': 'quad opamp rtor', 'kicadSymbolki_description': 'Quad, Low-Power, Low Offset Voltage, Rail-to-Rail Operational Amplifier, SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Operational : OPA4196xD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

