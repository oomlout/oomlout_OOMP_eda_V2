
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "PAM8302AAD"
    hexID = "SZKAMPLIFIERAUDIOPAM832AAD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PAM8302AAD', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/PAM8302A.pdf', 'kicadSymbolki_keywords': 'audio amplifier class d', 'kicadSymbolki_description': '2.5W Filterless Class-D Mono Audio Amplifier, SOIC-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Audio : PAM8302AAD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

