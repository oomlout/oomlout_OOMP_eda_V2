
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BTS50080-1TEB"
    hexID = "SZKPOWERMANAGEMENTBTS581TEB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BTS50080-1TEA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BTS50080-1TEB', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-4', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BTS50080-1TEB-DS-v01_00-EN.pdf?fileId=5546d4625a888733015aa435e5601157', 'kicadSymbolki_keywords': 'infineon power switch', 'kicadSymbolki_description': 'Smart High-Side Power Switch, PROFET, Single, 16mOhm, 10A, 30V, TO252-5', 'kicadSymbolki_fp_filters': 'TO*252*'}])
    newPart['name'].append('Power_Management : BTS50080-1TEB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

