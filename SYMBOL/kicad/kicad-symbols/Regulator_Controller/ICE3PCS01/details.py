
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "ICE3PCS01"
    hexID = "SZKREGULATORCONTROLLERICE3PCS1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICE3PCS01', 'kicadSymbolFootprint': 'Package_SO:SOIC-14_3.9x8.7mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-ICE3PCS01-DS-v03_00-EN.pdf?fileId=db3a304329a0f6ee0129a67ae8c02b46', 'kicadSymbolki_keywords': 'SMPS pfc controller', 'kicadSymbolki_description': 'Standalone PFC Controller in CCM, SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Controller : ICE3PCS01')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

