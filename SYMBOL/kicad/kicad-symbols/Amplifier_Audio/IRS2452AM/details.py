
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "IRS2452AM"
    hexID = "SZKAMPLIFIERAUDIOIRS2452AM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IRS2452AM', 'kicadSymbolFootprint': 'Package_DFN_QFN:Infineon_MLPQ-40-32-1EP_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IRS2452AM-DS-v01_00-EN.pdf?fileId=5546d462584d1d4a01584ee4f1f00713', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'Gate Driver Class D 2ch', 'kicadSymbolki_description': 'Class D Audio IC, PWM Modulator, +/-200V, 0.5/0.6A, MLPQ-32', 'kicadSymbolki_fp_filters': 'Infineon*MLPQ*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Audio : IRS2452AM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

