
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Box_L13.0mm_W4.0mm_P9.00mm"
    hexID = "FZKRRBOXL13W4P9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Box_L13.0mm_W4.0mm_P9.00mm', 'description': 'Resistor, Box series, Radial, pin pitch=9.00mm, 2W, length*width=13.0*4.0mm^2, http://www.produktinfo.conrad.com/datenblaetter/425000-449999/443860-da-01-de-METALLBAND_WIDERSTAND_0_1_OHM_5W_5Pr.pdf', 'tags': 'Resistor Box series Radial pin pitch 9.00mm 2W length 13.0mm width 4.0mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Box_L13.0mm_W4.0mm_P9.00mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Box_L13.0mm_W4.0mm_P9.00mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

