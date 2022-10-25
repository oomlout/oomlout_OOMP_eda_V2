
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IPD50R380CE"
    hexID = "SZKTRANSISTORFETIPD5R38CE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IPD50R380CE', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IPD50R380CE-DS-v02_01-en.pdf?fileId=db3a30433ecb86d4013ed0a2ef580f38', 'kicadSymbolki_keywords': 'CoolMOS Power MOSFET N-MOS', 'kicadSymbolki_description': '14.1A Id, 500V Vds, CoolMOS N-Channel Power MOSFET, 380mOhm Ron, 24.8nC Qg (typ), TO-252-2', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Transistor_FET : IPD50R380CE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

