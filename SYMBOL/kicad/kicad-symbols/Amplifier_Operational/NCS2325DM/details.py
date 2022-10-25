
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "NCS2325DM"
    hexID = "SZKAMPLIFIEROPERATIONALNCS2325DM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCS2325DM', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/PowerSolutions/document/NCS325-D.PDF', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'dual opamp low-power', 'kicadSymbolki_description': 'Dual operational amplifier, 50uV Offset, 0.25uV/C, 35uA Zero-Drift, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Operational : NCS2325DM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

