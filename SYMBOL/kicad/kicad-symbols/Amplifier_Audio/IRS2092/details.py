
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "IRS2092"
    hexID = "SZKAMPLIFIERAUDIOIRS292"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IRS2092', 'kicadSymbolFootprint': 'Package_DIP:DIP-16_W7.62mm', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/irs2092.pdf?fileId=5546d462533600a401535675f1be2790', 'kicadSymbolki_keywords': 'Gate Driver Class D', 'kicadSymbolki_description': 'Protected Digital Audio Amplifier, PWM Modulator, +/-100V, 1.0/1.2A, PDIP-16', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Amplifier_Audio : IRS2092')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

