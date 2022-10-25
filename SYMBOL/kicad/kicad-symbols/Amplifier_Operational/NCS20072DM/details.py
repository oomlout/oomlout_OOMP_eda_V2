
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "NCS20072DM"
    hexID = "SZKAMPLIFIEROPERATIONALNCS272DM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCS2325DM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCS20072DM', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NCS20071-D.PDF', 'kicadSymbolki_keywords': 'dual rail-to-rail output opamp vfa', 'kicadSymbolki_description': 'Dual, 2.8V/µs, Rail-to-Rail Output, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Operational : NCS20072DM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

