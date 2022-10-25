
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "L6491"
    hexID = "SZKDRIVERFETL6491"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L6491', 'kicadSymbolFootprint': 'Package_SO:SO-14_3.9x8.65mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/l6491.pdf', 'kicadSymbolki_keywords': 'fet driver', 'kicadSymbolki_description': 'High voltage high and low-side 4 A gate driver, SO-14', 'kicadSymbolki_fp_filters': 'SO*3.9x8.65mm*P1.27mm*'}])
    newPart['name'].append('Driver_FET : L6491')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

