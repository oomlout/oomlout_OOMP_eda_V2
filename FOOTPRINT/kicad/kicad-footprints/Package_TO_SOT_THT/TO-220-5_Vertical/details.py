
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "TO-220-5_Vertical"
    hexID = "FZKSOTTO225VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-220-5_Vertical', 'description': 'TO-220-5, Vertical, RM 1.7mm, Pentawatt, Multiwatt-5, see http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/ltc-legacy-to-220/to-220_5_05-08-1421_straight_lead.pdf', 'tags': 'TO-220-5 Vertical RM 1.7mm Pentawatt Multiwatt-5', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-220-5_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_THT : TO-220-5_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

