
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_CommonMode_Toroid_Vertical_L21.0mm_W10.0mm_Px5.08mm_Py12.70mm_Murata_5100"
    hexID = "FZKINLCOONMODETOROIDVERTICALL21W1PX58PY127M51"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_CommonMode_Toroid_Vertical_L21.0mm_W10.0mm_Px5.08mm_Py12.70mm_Murata_5100', 'description': 'L_CommonMode_Toroid, Vertical series, Radial, pin pitch=5.08*12.70mm^2, , length*width=21*10mm^2, muRATA, 5100, http://www.murata-ps.com/data/magnetics/kmp_5100.pdf', 'tags': 'L_CommonMode_Toroid Vertical series Radial pin pitch 5.08*12.70mm^2  length 21mm width 10mm muRATA 5100', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_CommonMode_Toroid_Vertical_L21.0mm_W10.0mm_Px5.08mm_Py12.70mm_Murata_5100.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Inductor_THT : L_CommonMode_Toroid_Vertical_L21.0mm_W10.0mm_Px5.08mm_Py12.70mm_Murata_5100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

