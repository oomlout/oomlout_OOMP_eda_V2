
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "LM4810"
    hexID = "SZKAMPLIFIERAUDIOLM481"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4810', 'kicadSymbolFootprint': 'Package_SO:TSSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4810.pdf', 'kicadSymbolki_keywords': 'audio amplifier headphone', 'kicadSymbolki_description': 'Boomer Dual 105mW Headphone Amplifier with Active-High Shutdown Mode, VSSOP-8', 'kicadSymbolki_fp_filters': 'TSSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Audio : LM4810')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

