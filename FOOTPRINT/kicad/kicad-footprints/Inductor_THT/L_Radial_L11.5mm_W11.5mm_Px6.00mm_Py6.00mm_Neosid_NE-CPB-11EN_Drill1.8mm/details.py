
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_L11.5mm_W11.5mm_Px6.00mm_Py6.00mm_Neosid_NE-CPB-11EN_Drill1.8mm"
    hexID = "FZKINLRL115W115PX6PY6NEOSIDNECPB11ENDRILL18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_L11.5mm_W11.5mm_Px6.00mm_Py6.00mm_Neosid_NE-CPB-11EN_Drill1.8mm', 'description': 'Inductor, Radial series, Radial, pin pitch=6.00*6.00mm^2, , length*width=11.5*11.5mm^2, Neosid, NE-CPB-11EN, Drill1.8mm, http://www.neosid.de/produktblaetter/neosid_Festinduktivitaet_NE_CPB11EN.pdf', 'tags': 'Inductor Radial series Radial pin pitch 6.00*6.00mm^2  length 11.5mm width 11.5mm Neosid NE-CPB-11EN Drill1.8mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_L11.5mm_W11.5mm_Px6.00mm_Py6.00mm_Neosid_NE-CPB-11EN_Drill1.8mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_L11.5mm_W11.5mm_Px6.00mm_Py6.00mm_Neosid_NE-CPB-11EN_Drill1.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

