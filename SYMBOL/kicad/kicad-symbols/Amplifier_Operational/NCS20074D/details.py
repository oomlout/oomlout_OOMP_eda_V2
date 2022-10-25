
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "NCS20074D"
    hexID = "SZKAMPLIFIEROPERATIONALNCS274D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCS4325', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCS20074D', 'kicadSymbolFootprint': 'Package_SO:SOIC-14_3.9x8.7mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NCS20071-D.PDF', 'kicadSymbolki_keywords': 'quad rail-to-rail output opamp vfa', 'kicadSymbolki_description': 'Quad, 2.8V/µs, Rail-to-Rail Output, SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Operational : NCS20074D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

