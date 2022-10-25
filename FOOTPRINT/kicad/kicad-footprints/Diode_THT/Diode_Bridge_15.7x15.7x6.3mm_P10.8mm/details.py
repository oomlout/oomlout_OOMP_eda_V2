
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "Diode_Bridge_15.7x15.7x6.3mm_P10.8mm"
    hexID = "FZKDDIODEBRIDGE157X157X63P18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diode_Bridge_15.7x15.7x6.3mm_P10.8mm', 'description': 'Single phase bridge rectifier case 15.7x15.7', 'tags': 'Diode Bridge', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_15.7x15.7x6.3mm_P10.8mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : Diode_Bridge_15.7x15.7x6.3mm_P10.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

