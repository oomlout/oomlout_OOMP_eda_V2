
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_L7.5mm_W4.6mm_P5.00mm_Neosid_SD75"
    hexID = "FZKINLRL75W46P5NEOSIDSD75"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_L7.5mm_W4.6mm_P5.00mm_Neosid_SD75', 'description': 'Inductor, Radial series, Radial, pin pitch=5.00mm, , length*width=7.5*4.6mm^2, Neosid, SD75, http://www.neosid.de/produktblaetter/neosid_Festinduktivitaet_Sd75.pdf', 'tags': 'Inductor Radial series Radial pin pitch 5.00mm  length 7.5mm width 4.6mm Neosid SD75', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_L7.5mm_W4.6mm_P5.00mm_Neosid_SD75.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_L7.5mm_W4.6mm_P5.00mm_Neosid_SD75')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

