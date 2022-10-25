
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_L8.0mm_W8.0mm_P5.00mm_Neosid_SD8"
    hexID = "FZKINLRL8W8P5NEOSIDSD8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_L8.0mm_W8.0mm_P5.00mm_Neosid_SD8', 'description': 'Inductor, Radial series, Radial, pin pitch=5.00mm, , length*width=8*8mm^2, Neosid, SD8, http://www.neosid.de/produktblaetter/neosid_Festinduktivitaet_Sd8.pdf', 'tags': 'Inductor Radial series Radial pin pitch 5.00mm  length 8mm width 8mm Neosid SD8', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_L8.0mm_W8.0mm_P5.00mm_Neosid_SD8.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_L8.0mm_W8.0mm_P5.00mm_Neosid_SD8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

