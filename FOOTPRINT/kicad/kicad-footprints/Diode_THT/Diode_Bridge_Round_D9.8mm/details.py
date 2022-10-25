
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "Diode_Bridge_Round_D9.8mm"
    hexID = "FZKDDIODEBRIDGEROUNDD98"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diode_Bridge_Round_D9.8mm', 'description': '4-lead round diode bridge package, diameter 9.8mm, pin pitch 5.08mm, see http://www.vishay.com/docs/88769/woo5g.pdf', 'tags': 'diode bridge 9.8mm WOG pitch 5.08mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_Round_D9.8mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : Diode_Bridge_Round_D9.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

