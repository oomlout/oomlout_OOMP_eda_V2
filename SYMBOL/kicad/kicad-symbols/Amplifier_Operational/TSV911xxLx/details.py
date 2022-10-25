
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "TSV911xxLx"
    hexID = "SZKAMPLIFIEROPERATIONALTSV911XXLX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP6L91T-EOT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSV911xxLx', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'www.st.com/resource/en/datasheet/tsv911.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Single rail-to-rail input/output 8 MHz operational amplifiers, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Amplifier_Operational : TSV911xxLx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

