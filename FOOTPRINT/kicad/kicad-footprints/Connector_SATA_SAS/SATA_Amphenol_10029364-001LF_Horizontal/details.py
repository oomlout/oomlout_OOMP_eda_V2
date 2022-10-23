
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_SATA_SAS"
    oIndex = "SATA_Amphenol_10029364-001LF_Horizontal"
    hexID = "FZKCNSATASASSATAAMPHENOL1293641LFHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SATA_Amphenol_10029364-001LF_Horizontal', 'description': 'https://cdn.amphenol-icc.com/media/wysiwyg/files/drawing/10029364.pdf', 'tags': 'SATA', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_SATA_SAS.3dshapes/SATA_Amphenol_10029364-001LF_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_SATA_SAS : SATA_Amphenol_10029364-001LF_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

