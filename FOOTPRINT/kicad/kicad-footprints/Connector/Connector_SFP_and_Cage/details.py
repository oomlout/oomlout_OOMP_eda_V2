
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector"
    oIndex = "Connector_SFP_and_Cage"
    hexID = "FZKCNCNSFPANDCAGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Connector_SFP_and_Cage', 'description': 'https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=2227302&DocType=Customer+Drawing&DocLang=English', 'tags': 'SFP+ SFP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector.3dshapes/Connector_SFP_and_Cage.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector : Connector_SFP_and_Cage')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

