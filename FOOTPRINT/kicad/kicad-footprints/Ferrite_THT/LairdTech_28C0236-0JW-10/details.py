
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Ferrite_THT"
    oIndex = "LairdTech_28C0236-0JW-10"
    hexID = "FZKFLAIRDTECH28C236JW1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LairdTech_28C0236-0JW-10', 'description': 'Ferrite, vertical, LairdTech 28C0236-0JW-10, https://assets.lairdtech.com/home/brandworld/files/28C0236-0JW-10.pdf, JW Miller core https://www.bourns.com/products/magnetic-products/j.w.-miller-through-hole-ferrite-beads-emi-filters', 'tags': 'Ferrite vertical LairdTech 28C0236-0JW-10', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Ferrite_THT.3dshapes/LairdTech_28C0236-0JW-10.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Ferrite_THT : LairdTech_28C0236-0JW-10')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

