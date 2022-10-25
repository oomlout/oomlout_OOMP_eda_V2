
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_SPDT_Finder_40.31"
    hexID = "FZKRELRELAYSPDTFINDER431"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_SPDT_Finder_40.31', 'description': 'Relay DPDT Finder 40.31, Pitch 3.5mm/7.5mm, https://www.finder-relais.net/de/finder-relais-serie-40.pdf', 'tags': 'Relay DPDT Finder 40.31 Pitch 3.5mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_SPDT_Finder_40.31.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Relay_THT : Relay_SPDT_Finder_40.31')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

