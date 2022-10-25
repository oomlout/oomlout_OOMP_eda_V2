
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "SSM2120"
    hexID = "SZKAMPLIFIERAUDIOSSM212"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SSM2120', 'kicadSymbolFootprint': 'Package_DIP:DIP-22_W7.62mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/obsolete-data-sheets/105738070SSM2120.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'audio VCA', 'kicadSymbolki_description': 'Dynamic Range Pprocessor/Dual VCA, DIP-22', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Amplifier_Audio : SSM2120')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

