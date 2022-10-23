
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Coaxial"
    oIndex = "U.FL_Molex_MCRF_73412-0110_Vertical"
    hexID = "FZKCNCOAUFLMXMCRF7341211VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'U.FL_Molex_MCRF_73412-0110_Vertical', 'description': 'Molex Microcoaxial RF Connectors (MCRF), mates Hirose U.FL, (http://www.molex.com/pdm_docs/sd/734120110_sd.pdf)', 'tags': 'mcrf hirose ufl u.fl microcoaxial', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/U.FL_Molex_MCRF_73412-0110_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Coaxial : U.FL_Molex_MCRF_73412-0110_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

