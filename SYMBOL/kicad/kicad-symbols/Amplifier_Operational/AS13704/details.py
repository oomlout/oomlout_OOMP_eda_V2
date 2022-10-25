
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "AS13704"
    hexID = "SZKAMPLIFIEROPERATIONALAS1374"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS13704', 'kicadSymbolFootprint': 'Package_SO:SSOP-24_3.9x8.7mm_P0.635mm', 'kicadSymbolDatasheet': 'http://www.alfarzpp.lv/eng/sc/AS13704.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'operational transconductance amplifier OTA', 'kicadSymbolki_description': 'Quad Operational Transconductance Amplifiers (OTA), with linearizing diodes, SSOP24', 'kicadSymbolki_fp_filters': 'SSOP*3.9x8.7mm*P0.635mm*'}])
    newPart['name'].append('Amplifier_Operational : AS13704')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

