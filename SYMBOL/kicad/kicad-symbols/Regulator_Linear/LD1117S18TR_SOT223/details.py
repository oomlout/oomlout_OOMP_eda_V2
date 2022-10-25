
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LD1117S18TR_SOT223"
    hexID = "SZKREGULATORLINEARLD1117S18TRSOT223"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AP1117-15', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LD1117S18TR_SOT223', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00000544.pdf', 'kicadSymbolki_keywords': 'REGULATOR LDO 1.8V', 'kicadSymbolki_description': '800mA Fixed Low Drop Positive Voltage Regulator, Fixed Output 1.8V, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*TabPin2*'}])
    newPart['name'].append('Regulator_Linear : LD1117S18TR_SOT223')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

