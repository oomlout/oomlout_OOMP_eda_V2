
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "Diode_Bridge_15.1x15.1x6.3mm_P10.9mm"
    hexID = "FZKDDIODEBRIDGE151X151X63P19"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diode_Bridge_15.1x15.1x6.3mm_P10.9mm', 'description': 'Single phase bridge rectifier case 15.1x15.1mm, pitch 10.9mm, see https://diotec.com/tl_files/diotec/files/pdf/datasheets/pb1000.pdf', 'tags': 'Diode Bridge PB10xxS', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_15.1x15.1x6.3mm_P10.9mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : Diode_Bridge_15.1x15.1x6.3mm_P10.9mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

