
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Samtec_HLE_THT"
    oIndex = "Samtec_HLE-120-02-xx-DV-PE-LC_2x20_P2.54mm_Horizontal"
    hexID = "FZKCNSAMTECHLETHTSAMTECHLE122XXDVPELC2X2P254HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Samtec_HLE-120-02-xx-DV-PE-LC_2x20_P2.54mm_Horizontal', 'description': 'Samtec HLE .100" Tiger Beam Cost-effective Single Beam Socket Strip, HLE-120-02-xx-DV-PE-LC, 20 Pins per row (http://suddendocs.samtec.com/prints/hle-1xx-02-xx-dv-xe-xx-mkt.pdf, http://suddendocs.samtec.com/prints/hle-thru.pdf), generated with kicad-footprint-generator', 'tags': 'connector Samtec HLE top entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Samtec_HLE_THT.3dshapes/Samtec_HLE-120-02-xx-DV-PE-LC_2x20_P2.54mm_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Samtec_HLE_THT : Samtec_HLE-120-02-xx-DV-PE-LC_2x20_P2.54mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

