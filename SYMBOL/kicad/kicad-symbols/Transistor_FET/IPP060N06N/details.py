
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IPP060N06N"
    hexID = "SZKTRANSISTORFETIPP6N6N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BUZ11', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IPP060N06N', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IPP060N06N-DS-v02_02-en.pdf?fileId=db3a30433727a44301372c06d9d7498a', 'kicadSymbolki_keywords': 'N-Channel Power MOSFET Infineon', 'kicadSymbolki_description': '45A Id, 60V Vds, Single N-Channel Power MOSFET, 6mOhm Ron, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Transistor_FET : IPP060N06N')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

