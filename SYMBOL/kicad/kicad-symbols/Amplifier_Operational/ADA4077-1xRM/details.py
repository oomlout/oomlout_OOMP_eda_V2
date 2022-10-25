
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "ADA4077-1xRM"
    hexID = "SZKAMPLIFIEROPERATIONALADA4771XRM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP6L91RT-EMS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADA4077-1xRM', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADA4077-1_4077-2_4077-4.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': '4MHz, 7nV/sqrtHz, Low Offset and Drift, High Precision Amplifier, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Operational : ADA4077-1xRM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

