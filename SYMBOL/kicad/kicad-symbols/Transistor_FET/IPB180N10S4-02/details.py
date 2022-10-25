
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IPB180N10S4-02"
    hexID = "SZKTRANSISTORFETIPB18N1S42"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IPB180N10S4-02', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-6', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IPB180N10S4_02-DS-v01_00-en.pdf?fileId=db3a30433d1d0bbe013d2129cf8a2f88', 'kicadSymbolki_keywords': 'OptiMOS-T2 Power MOSFET N-MOS', 'kicadSymbolki_description': '180A Id, 100V Vds, OptiMOS-T2 N-Channel Power MOSFET, 2.5mOhm Ron, Qg (typ) 156nC, TO-263-6', 'kicadSymbolki_fp_filters': 'TO?263?6*'}])
    newPart['name'].append('Transistor_FET : IPB180N10S4-02')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

