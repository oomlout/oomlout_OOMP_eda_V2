
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "IDDD06G65C6"
    hexID = "SZKDIODEIDDD6G65C6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IDDD04G65C6', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'IDDD06G65C6', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Infineon_PG-HDSOP-10-1', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IDDD06G65C6-DS-v02_00-EN.pdf?fileId=5546d462625a528f01628f86ff8c0e09', 'kicadSymbolki_keywords': 'sic diode', 'kicadSymbolki_description': '650V, 6A, SiC Schottky Diode, CoolSiC, PG-HDSOP-10-1 (DDPAK)', 'kicadSymbolki_fp_filters': 'Infineon*PG*HDSOP*'}])
    newPart['name'].append('Diode : IDDD06G65C6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

