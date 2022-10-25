
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Samtec"
    oIndex = "Samtec_FMC_ASP-134486-01_10x40_P1.27mm_Vertical"
    hexID = "FZKCNSAMTECSAMTECFMCASP13448611X4P127VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Samtec_FMC_ASP-134486-01_10x40_P1.27mm_Vertical', 'description': 'http://suddendocs.samtec.com/prints/asp-134486-01-mkt.pdf', 'tags': 'FMC HPC', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Samtec.3dshapes/Samtec_FMC_ASP-134486-01_10x40_P1.27mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Samtec : Samtec_FMC_ASP-134486-01_10x40_P1.27mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

