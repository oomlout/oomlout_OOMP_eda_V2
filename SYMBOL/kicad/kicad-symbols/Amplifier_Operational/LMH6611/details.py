
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LMH6611"
    hexID = "SZKAMPLIFIEROPERATIONALLMH6611"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMH6611', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmh6612.pdf', 'kicadSymbolki_keywords': 'opamp operational amplifier single', 'kicadSymbolki_description': 'Single Supply, 345 MHz, Rail-to-Rail Output, Amplifier, TSOT-23-6', 'kicadSymbolki_fp_filters': 'TSOT*23*'}])
    newPart['name'].append('Amplifier_Operational : LMH6611')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

