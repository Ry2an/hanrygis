library(sp)
library(maptools)
gpclibPermit()
get_shp=readShapeSpatial(file.path("C:/HanryGIS/China-Province/shp/bou2_4p.shp"))
get_shp$NAME[899]=get_shp$NAME[896]
a<-vector(mode="numeric",length=2)
a[1]=73
a[2]=135
b<-vector(mode="numeric",length=2)
b[1]=3
b[2]=53

setwd("c://HanryGIS//China-Province//")
plot(get_shp,xlim=a,ylim=b)
png(file="base.png", bg="transparent")
plot(get_shp,xlim=a,ylim=b)
dev.off()
setwd("c://HanryGIS//China-Province//")
plot(get_shp,xlim=a,ylim=b)
jpeg(file="base.jpeg")
plot(get_shp,xlim=a,ylim=b)
dev.off()
