
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_CommonMode_Toroid_Vertical_L43.2mm_W22.9mm_Px17.78mm_Py30.48mm_Bourns_8100"
    hexID = "FZKINLCOONMODETOROIDVERTICALL432W229PX1778PY348BOURNS81"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_CommonMode_Toroid_Vertical_L43.2mm_W22.9mm_Px17.78mm_Py30.48mm_Bourns_8100', 'description': 'L_CommonMode_Toroid, Vertical series, Radial, pin pitch=17.78*30.48mm^2, , length*width=43.18*22.86mm^2, Bourns, 8100, http://datasheet.octopart.com/8120-RC-Bourns-datasheet-10228452.pdf', 'tags': 'L_CommonMode_Toroid Vertical series Radial pin pitch 17.78*30.48mm^2  length 43.18mm width 22.86mm Bourns 8100', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_CommonMode_Toroid_Vertical_L43.2mm_W22.9mm_Px17.78mm_Py30.48mm_Bourns_8100.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Inductor_THT : L_CommonMode_Toroid_Vertical_L43.2mm_W22.9mm_Px17.78mm_Py30.48mm_Bourns_8100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

