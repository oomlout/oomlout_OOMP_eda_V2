
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_CommonMode_Toroid_Vertical_L39.4mm_W20.3mm_Px15.24mm_Py22.86mm_Bourns_8100"
    hexID = "FZKINLCOONMODETOROIDVERTICALL394W23PX1524PY2286BOURNS81"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_CommonMode_Toroid_Vertical_L39.4mm_W20.3mm_Px15.24mm_Py22.86mm_Bourns_8100', 'description': 'L_CommonMode_Toroid, Vertical series, Radial, pin pitch=15.24*22.86mm^2, , length*width=39.37*20.32mm^2, Bourns, 8100, http://datasheet.octopart.com/8120-RC-Bourns-datasheet-10228452.pdf', 'tags': 'L_CommonMode_Toroid Vertical series Radial pin pitch 15.24*22.86mm^2  length 39.37mm width 20.32mm Bourns 8100', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_CommonMode_Toroid_Vertical_L39.4mm_W20.3mm_Px15.24mm_Py22.86mm_Bourns_8100.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Inductor_THT : L_CommonMode_Toroid_Vertical_L39.4mm_W20.3mm_Px15.24mm_Py22.86mm_Bourns_8100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

