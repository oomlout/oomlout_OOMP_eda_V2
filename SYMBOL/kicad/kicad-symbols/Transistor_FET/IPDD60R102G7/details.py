
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IPDD60R102G7"
    hexID = "SZKTRANSISTORFETIPDD6R12G7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IPDD60R050G7', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IPDD60R102G7', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Infineon_PG-HDSOP-10-1', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IPDD60R102G7-DS-v02_00-EN.pdf?fileId=5546d4626102d35a01617087ee7379ed', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '23A Id, 600V Vds, 102mOhm, N-Channel MOSFET, CoolMOS G7, PG-HDSOP-10-1 (DDPAK)', 'kicadSymbolki_fp_filters': 'Infineon*PG*HDSOP*'}])
    newPart['name'].append('IPDD60R102G7')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

