
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Samtec_HLE_THT"
    oIndex = "Samtec_HLE-138-02-xx-DV-TE_2x38_P2.54mm_Horizontal"
    hexID = "FZKCNSAMTECHLETHTSAMTECHLE1382XXDVTE2X38P254HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Samtec_HLE-138-02-xx-DV-TE_2x38_P2.54mm_Horizontal', 'description': 'Samtec HLE .100" Tiger Beam Cost-effective Single Beam Socket Strip, HLE-138-02-xx-DV-TE, 38 Pins per row (http://suddendocs.samtec.com/prints/hle-1xx-02-xx-dv-xe-xx-mkt.pdf, http://suddendocs.samtec.com/prints/hle-thru.pdf), generated with kicad-footprint-generator', 'tags': 'connector Samtec HLE top entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Samtec_HLE_THT.3dshapes/Samtec_HLE-138-02-xx-DV-TE_2x38_P2.54mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Samtec_HLE_THT : Samtec_HLE-138-02-xx-DV-TE_2x38_P2.54mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

