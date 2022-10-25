
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "VNP10N07"
    hexID = "SZKTRANSISTORFETVNP1N7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BUZ11', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'VNP10N07', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/vnp10n07.pdf', 'kicadSymbolki_keywords': 'N-Channel Power MOSFET OMNIFET', 'kicadSymbolki_description': '10A Id, 70V Vds, N-Channel Power MOSFET, fully autoprotected, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Transistor_FET : VNP10N07')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

