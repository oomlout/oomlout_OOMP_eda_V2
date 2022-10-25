
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LMH6702MA"
    hexID = "SZKAMPLIFIEROPERATIONALLMH672MA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'OPA333xxD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMH6702MA', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmh6702.pdf', 'kicadSymbolki_keywords': 'opamp single low distortion wideband', 'kicadSymbolki_description': '1.7 GHz Ultra-Low Distortion Wideband Op Amp, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Operational : LMH6702MA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

