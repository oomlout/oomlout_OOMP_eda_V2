
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_T-1_P2.54mm_Vertical_AnodeUp"
    hexID = "FZKDDT1P254VERTICALANODEUP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_T-1_P2.54mm_Vertical_AnodeUp', 'description': 'Diode, T-1 series, Axial, Vertical, pin pitch=2.54mm, , length*diameter=3.2*2.6mm^2, , http://www.diodes.com/_files/packages/T-1.pdf', 'tags': 'Diode T-1 series Axial Vertical pin pitch 2.54mm  length 3.2mm diameter 2.6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_T-1_P2.54mm_Vertical_AnodeUp.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : D_T-1_P2.54mm_Vertical_AnodeUp')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

