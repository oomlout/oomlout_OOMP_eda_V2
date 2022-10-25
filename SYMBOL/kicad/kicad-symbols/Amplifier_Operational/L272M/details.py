
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "L272M"
    hexID = "SZKAMPLIFIEROPERATIONALL272M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L272M', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm_LongPads', 'kicadSymbolDatasheet': 'www.st.com/resource/en/datasheet/l272.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'dual power opamp', 'kicadSymbolki_description': 'Dual Power Operation Amplifier, DIP-8', 'kicadSymbolki_fp_filters': '*DIP*W7.62mm*'}])
    newPart['name'].append('Amplifier_Operational : L272M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

