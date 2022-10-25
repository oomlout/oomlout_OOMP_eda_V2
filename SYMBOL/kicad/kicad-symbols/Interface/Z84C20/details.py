
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "Z84C20"
    hexID = "SZKINTERFACEZ84C2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Z8420', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Z84C20', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'https://www.zilog.com/appnotes_download.php?FromPage=DirectLink&dn=PS0180&ft=Product%20Specification%20(Data%20Sheet)%20%20&f=YUhSMGNEb3ZMM2QzZHk1NmFXeHZaeTVqYjIwdlpHOWpjeTk2T0RBdmNITXdNVGd3TG5Ca1pnPT0=', 'kicadSymbolki_keywords': 'Z80 PIO parallel', 'kicadSymbolki_description': 'Parallel I/O, CMOS, DIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('Interface : Z84C20')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

