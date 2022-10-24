
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D21.8mm_P19.10mm_Bourns_2100"
    hexID = "FZKINLTOROIDHORIZONTALD218P191BOURNS21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D21.8mm_P19.10mm_Bourns_2100', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=19.10mm, , diameter=21.8mm, Bourns, 2100, http://www.bourns.com/docs/Product-Datasheets/2100_series.pdf?sfvrsn=3', 'tags': 'L_Toroid Horizontal series Radial pin pitch 19.10mm  diameter 21.8mm Bourns 2100', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D21.8mm_P19.10mm_Bourns_2100.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D21.8mm_P19.10mm_Bourns_2100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

