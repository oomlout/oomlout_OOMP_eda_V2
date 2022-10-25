
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "TL7733B"
    hexID = "SZKPOWERSUPERVISORTL7733B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TL7702A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TL7733B', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com.cn/cn/lit/ds/symlink/tl7705b.pdf', 'kicadSymbolki_keywords': 'voltage supervisor', 'kicadSymbolki_description': 'Supply-Voltage Supervisors, 3.08V, PDIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Power_Supervisor : TL7733B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

