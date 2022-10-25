
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "VIPer26HD"
    hexID = "SZKREGULATORSWITCHINGVIPER26HD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'VIPer26LD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VIPer26HD', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/viper26.pdf', 'kicadSymbolki_keywords': 'SMPS Controller with MOSFET', 'kicadSymbolki_description': '800V, 10-20W, 115kHz, SMPS Controller, SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : VIPer26HD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

