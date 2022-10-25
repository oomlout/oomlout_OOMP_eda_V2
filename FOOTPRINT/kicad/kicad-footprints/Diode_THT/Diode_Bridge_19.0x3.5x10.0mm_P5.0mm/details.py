
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "Diode_Bridge_19.0x3.5x10.0mm_P5.0mm"
    hexID = "FZKDDIODEBRIDGE19X35X1P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diode_Bridge_19.0x3.5x10.0mm_P5.0mm', 'description': 'Vishay GBU rectifier package, 5.08mm pitch, see http://www.vishay.com/docs/88606/g3sba20.pdf', 'tags': 'Vishay GBU rectifier diode bridge', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_19.0x3.5x10.0mm_P5.0mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : Diode_Bridge_19.0x3.5x10.0mm_P5.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

