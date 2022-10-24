
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D12.0mm_P10.00mm_Neosid_SD12k_style1"
    hexID = "FZKINLRD12P1NEOSIDSD12KSTYLE1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D12.0mm_P10.00mm_Neosid_SD12k_style1', 'description': 'Inductor, Radial series, Radial, pin pitch=10.00mm, , diameter=12.0mm, Neosid, SD12k, style1, http://www.neosid.de/produktblaetter/neosid_Festinduktivitaet_Sd12k.pdf', 'tags': 'Inductor Radial series Radial pin pitch 10.00mm  diameter 12.0mm Neosid SD12k style1', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D12.0mm_P10.00mm_Neosid_SD12k_style1.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D12.0mm_P10.00mm_Neosid_SD12k_style1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

