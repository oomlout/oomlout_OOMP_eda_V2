
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "PAM2305CGF180"
    hexID = "SZKREGULATORSWITCHINGPAM235CGF18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PAM2305CGF330', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PAM2305CGF180', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-6-1EP_2x2mm_P0.65mm_EP1x1.6mm', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/PAM2305.pdf', 'kicadSymbolki_keywords': 'Voltage regulator switching buck fixed output analog', 'kicadSymbolki_description': '1A, Step-Down DC/DC-Converter, 1.8V Fixed Output Voltage, 1.5MHz, DFN-6', 'kicadSymbolki_fp_filters': 'DFN*EP*2x2mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Switching : PAM2305CGF180')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

