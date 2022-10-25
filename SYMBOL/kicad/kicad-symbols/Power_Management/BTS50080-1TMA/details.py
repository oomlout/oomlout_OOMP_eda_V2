
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BTS50080-1TMA"
    hexID = "SZKPOWERMANAGEMENTBTS581TMA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BTS50055-1TMA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BTS50080-1TMA', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-7_TabPin4', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BTS50080-1TMA-DS-v01_00-EN.pdf?fileId=5546d4625a888733015aa435d7fe1153', 'kicadSymbolki_keywords': 'BTS50080 PROFET', 'kicadSymbolki_description': 'Smart High-Side Power Switch, PROFET, Single, 16mOhm, 9.5A, 38V, TO220-7', 'kicadSymbolki_fp_filters': 'TO*263*TabPin4*'}])
    newPart['name'].append('Power_Management : BTS50080-1TMA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

