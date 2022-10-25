
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LD39150DT18"
    hexID = "SZKREGULATORLINEARLD3915DT18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LD39150DT18', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-3_TabPin2', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/ld39150.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo fixed positive', 'kicadSymbolki_description': '1.5A Ultra Low Dropout regulator, positive, 1.8V fixed output, TO-252', 'kicadSymbolki_fp_filters': 'TO?252*TabPin2*'}])
    newPart['name'].append('Regulator_Linear : LD39150DT18')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

