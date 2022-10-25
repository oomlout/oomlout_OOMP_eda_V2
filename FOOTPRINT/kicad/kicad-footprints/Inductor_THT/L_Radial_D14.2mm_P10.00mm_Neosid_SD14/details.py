
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D14.2mm_P10.00mm_Neosid_SD14"
    hexID = "FZKINLRD142P1NEOSIDSD14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D14.2mm_P10.00mm_Neosid_SD14', 'description': 'Inductor, Radial series, Radial, pin pitch=10.00mm, , diameter=14.2mm, Neosid, SD14, http://www.neosid.de/produktblaetter/neosid_Festinduktivitaet_Sd14.pdf', 'tags': 'Inductor Radial series Radial pin pitch 10.00mm  diameter 14.2mm Neosid SD14', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D14.2mm_P10.00mm_Neosid_SD14.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D14.2mm_P10.00mm_Neosid_SD14')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

