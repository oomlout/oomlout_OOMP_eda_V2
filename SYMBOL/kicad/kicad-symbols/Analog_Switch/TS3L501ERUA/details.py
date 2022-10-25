
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "TS3L501ERUA"
    hexID = "SZKANALOGSWITCHTS3L51ERUA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TS3L501ERUA', 'kicadSymbolFootprint': 'Package_DFN_QFN:WQFN-42-1EP_3.5x9mm_P0.5mm_EP2.05x7.55mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ts3l501e.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'gbit base-t lvds lvpecl video', 'kicadSymbolki_description': '8-Channel SPDT/16-Bit to 8-Bit Multiplexer and Demultiplexer, Ethernet LAN Switch With Power-Down Mode, WQFN-42', 'kicadSymbolki_fp_filters': 'WQFN*1EP*3.5x9mm*P0.5mm*'}])
    newPart['name'].append('Analog_Switch : TS3L501ERUA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

