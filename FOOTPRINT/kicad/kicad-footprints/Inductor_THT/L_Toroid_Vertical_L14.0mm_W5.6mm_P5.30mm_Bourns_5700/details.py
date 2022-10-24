
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L14.0mm_W5.6mm_P5.30mm_Bourns_5700"
    hexID = "FZKINLTOROIDVERTICALL14W56P53BOURNS57"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L14.0mm_W5.6mm_P5.30mm_Bourns_5700', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=5.30mm, , length*width=14*5.6mm^2, Bourns, 5700, http://www.bourns.com/docs/Product-Datasheets/5700_series.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 5.30mm  length 14mm width 5.6mm Bourns 5700', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L14.0mm_W5.6mm_P5.30mm_Bourns_5700.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L14.0mm_W5.6mm_P5.30mm_Bourns_5700')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

