
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_SATA_SAS"
    oIndex = "SAS-mini_TEConnectivity_1888174_Vertical"
    hexID = "FZKCNSATASASSASMTECONNECTIVITY1888174VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SAS-mini_TEConnectivity_1888174_Vertical', 'description': '36pin mini SAS connector, http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=1888174&DocType=Customer+Drawing&DocLang=English', 'tags': 'SAS mini connector', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_SATA_SAS.3dshapes/SAS-mini_TEConnectivity_1888174_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_SATA_SAS : SAS-mini_TEConnectivity_1888174_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

