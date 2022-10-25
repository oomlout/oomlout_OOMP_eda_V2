
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "Diode_Bridge_32.0x5.6x17.0mm_P10.0mm_P7.5mm"
    hexID = "FZKDDIODEBRIDGE32X56X17P1P75"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diode_Bridge_32.0x5.6x17.0mm_P10.0mm_P7.5mm', 'description': 'Diotec 32x5.6x17mm rectifier package, 7.5mm/10mm pitch, see https://diotec.com/tl_files/diotec/files/pdf/datasheets/b40c3700.pdf', 'tags': 'Diotec rectifier diode bridge', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_32.0x5.6x17.0mm_P10.0mm_P7.5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : Diode_Bridge_32.0x5.6x17.0mm_P10.0mm_P7.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

