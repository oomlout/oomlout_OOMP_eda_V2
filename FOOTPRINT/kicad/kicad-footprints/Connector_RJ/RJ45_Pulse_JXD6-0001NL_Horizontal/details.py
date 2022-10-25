
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_RJ"
    oIndex = "RJ45_Pulse_JXD6-0001NL_Horizontal"
    hexID = "FZKCNRJRJ45PULSEJXD61NLHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RJ45_Pulse_JXD6-0001NL_Horizontal', 'description': 'RJ45 ethernet transformer with magnetics (https://productfinder.pulseeng.com/doc_type/WEB301/doc_num/JXD6-0001NL/doc_part/JXD6-0001NL.pdf)', 'tags': 'ethernet 8p8c transformer magjack', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Pulse_JXD6-0001NL_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_RJ : RJ45_Pulse_JXD6-0001NL_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

