
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "IRS20965S"
    hexID = "SZKAMPLIFIERAUDIOIRS2965S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IRS20965S', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irs20965spbf.pdf?fileId=5546d462533600a4015356761d8b279b', 'kicadSymbolki_keywords': 'Gate Driver Class D', 'kicadSymbolki_description': 'Class D Audio Driver, +/-100V, 2.0/2.0A, SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Audio : IRS20965S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

