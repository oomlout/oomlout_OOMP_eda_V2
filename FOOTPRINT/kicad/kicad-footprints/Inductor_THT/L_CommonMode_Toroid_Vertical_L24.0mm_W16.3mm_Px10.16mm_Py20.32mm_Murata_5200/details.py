
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_CommonMode_Toroid_Vertical_L24.0mm_W16.3mm_Px10.16mm_Py20.32mm_Murata_5200"
    hexID = "FZKINLCOONMODETOROIDVERTICALL24W163PX116PY232M52"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_CommonMode_Toroid_Vertical_L24.0mm_W16.3mm_Px10.16mm_Py20.32mm_Murata_5200', 'description': 'L_CommonMode_Toroid, Vertical series, Radial, pin pitch=10.16*20.32mm^2, , length*width=24*16.3mm^2, muRATA, 5200, http://www.murata-ps.com/data/magnetics/kmp_5200.pdf', 'tags': 'L_CommonMode_Toroid Vertical series Radial pin pitch 10.16*20.32mm^2  length 24mm width 16.3mm muRATA 5200', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_CommonMode_Toroid_Vertical_L24.0mm_W16.3mm_Px10.16mm_Py20.32mm_Murata_5200.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Inductor_THT : L_CommonMode_Toroid_Vertical_L24.0mm_W16.3mm_Px10.16mm_Py20.32mm_Murata_5200')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

