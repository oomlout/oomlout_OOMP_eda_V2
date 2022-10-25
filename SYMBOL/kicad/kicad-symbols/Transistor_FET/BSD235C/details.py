
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BSD235C"
    hexID = "SZKTRANSISTORFETBSD235C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSD235C', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BSD235C-DS-v02_04-EN.pdf?fileId=db3a30433580b371013585a2d0d53326', 'kicadSymbolki_keywords': 'OptiMOS MOSFET complementary nmos pmos enhanced avalanche AEC Q101 super logic infineon', 'kicadSymbolki_description': '-0.53/+0.95A Id, -20/+20V Vds, P/N-Channel MOSFET, SOT-363, Infineon', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('Transistor_FET : BSD235C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

