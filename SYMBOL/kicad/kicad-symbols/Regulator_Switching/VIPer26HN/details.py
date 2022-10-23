
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "VIPer26HN"
    hexID = "SZKREGULATORSWITCHINGVIPER26HN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'VIPer26LN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VIPer26HN', 'kicadSymbolFootprint': 'Package_DIP:DIP-8-N6_W7.62mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/viper26.pdf', 'kicadSymbolki_keywords': 'SMPS Controller with MOSFET', 'kicadSymbolki_description': '800V, 10-20W, 115kHz, SMPS Controller, DIP-7', 'kicadSymbolki_fp_filters': 'DIP*N6*W7.62mm*'}])
    newPart['name'].append('VIPer26HN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

