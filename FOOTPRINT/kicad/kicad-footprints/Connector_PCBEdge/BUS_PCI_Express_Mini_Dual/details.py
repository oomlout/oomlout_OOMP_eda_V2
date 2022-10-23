
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PCBEdge"
    oIndex = "BUS_PCI_Express_Mini_Dual"
    hexID = "FZKCNPCBEDGEBUSPCIEXPRESSMDUAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BUS_PCI_Express_Mini_Dual', 'description': 'Mini-PCI Express bus connector full size with dual clips (https://s3.amazonaws.com/fit-iot/download/facet-cards/documents/PCI_Express_miniCard_Electromechanical_specs_rev1.2.pdf#page=28)', 'tags': 'mini pcie', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PCBEdge.3dshapes/BUS_PCI_Express_Mini_Dual.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_PCBEdge : BUS_PCI_Express_Mini_Dual')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

