
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "L7815"
    hexID = "SZKREGULATORLINEARL7815"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'L7805', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L7815', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.st.com/content/ccc/resource/technical/document/datasheet/41/4f/b3/b0/12/d4/47/88/CD00000444.pdf/files/CD00000444.pdf/jcr:content/translations/en.CD00000444.pdf', 'kicadSymbolki_keywords': 'Voltage Regulator 1.5A Positive', 'kicadSymbolki_description': 'Positive 1.5A 35V Linear Regulator, Fixed Output 15V, TO-220/TO-263/TO-252', 'kicadSymbolki_fp_filters': 'TO?252* TO?263* TO?220*'}])
    newPart['name'].append('Regulator_Linear : L7815')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

