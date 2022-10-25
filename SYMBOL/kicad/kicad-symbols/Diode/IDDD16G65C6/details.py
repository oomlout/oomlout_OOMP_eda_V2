
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "IDDD16G65C6"
    hexID = "SZKDIODEIDDD16G65C6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IDDD04G65C6', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'IDDD16G65C6', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Infineon_PG-HDSOP-10-1', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IDDD16G65C6-DS-v02_00-EN.pdf?fileId=5546d462625a528f01628f8711b50e0c', 'kicadSymbolki_keywords': 'sic diode', 'kicadSymbolki_description': '650V, 16A, SiC Schottky Diode, CoolSiC, PG-HDSOP-10-1 (DDPAK)', 'kicadSymbolki_fp_filters': 'Infineon*PG*HDSOP*'}])
    newPart['name'].append('Diode : IDDD16G65C6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

