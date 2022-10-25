
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Bourns_SRP7028A_7.3x6.6mm"
    hexID = "FZKINDUCTORSMLBOURNSSRP728A73X66"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Bourns_SRP7028A_7.3x6.6mm', 'description': 'Shielded Power Inductors (https://www.bourns.com/docs/product-datasheets/srp7028a.pdf)', 'tags': 'Shielded Inductors Bourns SMD SRP7028A', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Bourns_SRP7028A_7.3x6.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Bourns_SRP7028A_7.3x6.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

