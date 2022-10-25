
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "TS881xCx"
    hexID = "SZKAMPLIFIEROPERATIONALTS881XCX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP6001x-LT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TS881xCx', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'http://www.st.com/content/ccc/resource/technical/document/datasheet/a2/60/3e/5d/b2/c1/4a/e9/DM00057901.pdf/files/DM00057901.pdf/jcr:content/translations/en.DM00057901.pdf', 'kicadSymbolki_keywords': 'single comparator', 'kicadSymbolki_description': 'Rail-to-rail 0.9V nanopower comparator, SC-70-5', 'kicadSymbolki_fp_filters': '*SC?70*'}])
    newPart['name'].append('Amplifier_Operational : TS881xCx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

