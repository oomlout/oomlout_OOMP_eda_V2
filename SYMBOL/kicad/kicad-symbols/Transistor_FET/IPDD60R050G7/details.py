
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IPDD60R050G7"
    hexID = "SZKTRANSISTORFETIPDD6R5G7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IPDD60R050G7', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Infineon_PG-HDSOP-10-1', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IPDD60R050G7-DS-v02_00-EN.pdf?fileId=5546d4626102d35a0161707eb2f97810', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '47A Id, 600V Vds, 50mOhm, N-Channel MOSFET, CoolMOS G7, PG-HDSOP-10-1 (DDPAK)', 'kicadSymbolki_fp_filters': 'Infineon*PG*HDSOP*'}])
    newPart['name'].append('Transistor_FET : IPDD60R050G7')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

