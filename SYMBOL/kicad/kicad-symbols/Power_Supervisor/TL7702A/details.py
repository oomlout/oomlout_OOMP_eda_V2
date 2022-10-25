
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "TL7702A"
    hexID = "SZKPOWERSUPERVISORTL772A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TL7702A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com.cn/cn/lit/ds/symlink/tl7705a.pdf', 'kicadSymbolki_keywords': 'voltage supervisor', 'kicadSymbolki_description': 'Supply-Voltage Supervisors, 2.53V, PDIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Power_Supervisor : TL7702A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

