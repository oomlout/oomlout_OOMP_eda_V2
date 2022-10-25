
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "ICE2PCS04"
    hexID = "SZKREGULATORCONTROLLERICE2PCS4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ICE1PCS02', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICE2PCS04', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-ICE2PCS04-DS-v02_01-en.pdf?fileId=db3a30431936bc4b01193b4e467952a9', 'kicadSymbolki_keywords': 'SMPS pfc controller', 'kicadSymbolki_description': 'Standalone PFC Controller in CCM With Input Brown-Out Protection, 133kHz, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Controller : ICE2PCS04')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

