
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "NCS4325"
    hexID = "SZKAMPLIFIEROPERATIONALNCS4325"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCS4325', 'kicadSymbolFootprint': 'Package_SO:SOIC-14_3.9x8.7mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/NCS325-D.PDF', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'quad opamp low-power', 'kicadSymbolki_description': 'Quad operational amplifier, 50uV Offset, 0.25uV/C, 35uA Zero-Drift, SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Operational : NCS4325')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

