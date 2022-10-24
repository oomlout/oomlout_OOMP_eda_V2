
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L28.6mm_W14.3mm_P11.43mm_Bourns_5700"
    hexID = "FZKINLTOROIDVERTICALL286W143P1143BOURNS57"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L28.6mm_W14.3mm_P11.43mm_Bourns_5700', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=11.43mm, , length*width=28.6*14.3mm^2, Bourns, 5700, http://www.bourns.com/docs/Product-Datasheets/5700_series.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 11.43mm  length 28.6mm width 14.3mm Bourns 5700', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L28.6mm_W14.3mm_P11.43mm_Bourns_5700.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L28.6mm_W14.3mm_P11.43mm_Bourns_5700')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

