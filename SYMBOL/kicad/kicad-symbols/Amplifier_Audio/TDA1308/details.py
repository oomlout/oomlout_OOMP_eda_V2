
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "TDA1308"
    hexID = "SZKAMPLIFIERAUDIOTDA138"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TDA1308', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/TDA1308.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'audio amplifier', 'kicadSymbolki_description': 'Class-AB Stereo Headphone Driver, SOIC-8/TSSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* TSSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Audio : TDA1308')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

