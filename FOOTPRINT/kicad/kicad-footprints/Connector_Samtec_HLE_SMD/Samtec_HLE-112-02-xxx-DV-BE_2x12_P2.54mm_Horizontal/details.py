
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Samtec_HLE_SMD"
    oIndex = "Samtec_HLE-112-02-xxx-DV-BE_2x12_P2.54mm_Horizontal"
    hexID = "FZKCNSAMTECHLESMSAMTECHLE1122XXXDVBE2X12P254HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Samtec_HLE-112-02-xxx-DV-BE_2x12_P2.54mm_Horizontal', 'description': 'Samtec HLE .100" Tiger Beam Cost-effective Single Beam Socket Strip, HLE-112-02-xxx-DV-BE, 12 Pins per row (http://suddendocs.samtec.com/prints/hle-1xx-02-xxx-dv-xx-xx-xx-mkt.pdf, http://suddendocs.samtec.com/prints/hle-dv-footprint.pdf), generated with kicad-footprint-generator', 'tags': 'connector Samtec HLE horizontal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Samtec_HLE_SMD.3dshapes/Samtec_HLE-112-02-xxx-DV_2x12_P2.54mm_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Samtec_HLE_SMD : Samtec_HLE-112-02-xxx-DV-BE_2x12_P2.54mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

