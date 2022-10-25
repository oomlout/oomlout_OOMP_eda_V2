
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_AMASS"
    oIndex = "AMASS_XT60-F_1x02_P7.20mm_Vertical"
    hexID = "FZKCNAMASSAMASSXT6F1X2P72VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'AMASS_XT60-F_1x02_P7.20mm_Vertical', 'description': 'AMASS female XT60, through hole, vertical, https://www.tme.eu/Document/2d152ced3b7a446066e6c419d84bb460/XT60%20SPEC.pdf', 'tags': 'XT60 female vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_AMASS.3dshapes/AMASS_XT60-F_1x02_P7.2mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_AMASS : AMASS_XT60-F_1x02_P7.20mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

