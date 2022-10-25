
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BTS5016SDA"
    hexID = "SZKPOWERMANAGEMENTBTS516SDA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BTS50080-1TEA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BTS5016SDA', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-4', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-BTS5016SDA-DS-v01_01-EN.pdf?fileId=5546d4625a888733015aa41a6c38112d', 'kicadSymbolki_keywords': 'infineon power switch', 'kicadSymbolki_description': 'Smart High-Side Power Switch, PROFET, Single, 32mOhm, 5.5A, 20V, TO252-5', 'kicadSymbolki_fp_filters': 'TO*252*'}])
    newPart['name'].append('Power_Management : BTS5016SDA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

