
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Triac_Thyristor"
    oIndex = "Z0107MN"
    hexID = "SZKTRIACTHYRISTORZ17MN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Z0103MN', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'Z0107MN', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/z01.pdf', 'kicadSymbolki_keywords': '4Q Triac', 'kicadSymbolki_description': '4Q Triac, 1A RMS, 600V VDRM, 5mA Igt, 10mA Ih, SOT-223', 'kicadSymbolki_fp_filters': 'SOT*223*'}])
    newPart['name'].append('Triac_Thyristor : Z0107MN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

