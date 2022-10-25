
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "LME49600"
    hexID = "SZKAMPLIFIERAUDIOLME496"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LME49600', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-5_TabPin3', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lme49600.pdf', 'kicadSymbolki_keywords': 'audio buffer amplifier', 'kicadSymbolki_description': 'High-Performance, High-Fidelity, High-Current Headphone Buffer, 250mA, TO-263', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Amplifier_Audio : LME49600')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

