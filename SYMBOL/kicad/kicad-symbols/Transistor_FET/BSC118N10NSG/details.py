
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BSC118N10NSG"
    hexID = "SZKTRANSISTORFETBSC118N1NSG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CSD17578Q5A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSC118N10NSG', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TDSON-8-1', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-BSC118N10NS-DS-v01_08-en.pdf?fileId=db3a3043163797a6011647fdc2d4071c', 'kicadSymbolki_keywords': 'OptiMOS Power MOSFET N-MOS', 'kicadSymbolki_description': '71A Id, 100V Vds, OptiMOS N-Channel Power MOSFET, 11.8mOhm Ron, Qg (typ) 42.0nC, PG-TDSON-8', 'kicadSymbolki_fp_filters': 'TDSON*'}])
    newPart['name'].append('Transistor_FET : BSC118N10NSG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

