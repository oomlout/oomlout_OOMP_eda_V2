
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "ICE2PCS05"
    hexID = "SZKREGULATORCONTROLLERICE2PCS5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ICE1PCS01', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICE2PCS05', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-ICE2PCS05-DS-v01_02-en.pdf?fileId=db3a30431c69a49d011cdfb46a834373', 'kicadSymbolki_keywords': 'SMPS pfc controller', 'kicadSymbolki_description': 'Standalone PFC Controller in CCM, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Controller : ICE2PCS05')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

