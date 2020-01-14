library(sp)
library(maptools)
gpclibPermit()
get_shp=readShapeSpatial(file.path("C:/HanryGIS/China-Province/shp/bou2_4p.shp"))
get_shp$NAME[899]=get_shp$NAME[896]
get_csv<-read.csv("C:/HanryGIS/China-Province/Variables.csv",sep=",",header=T)
a<-vector(mode="numeric",length=2)
a[1]=73
a[2]=135
b<-vector(mode="numeric",length=2)
b[1]=3
b[2]=53

for(i in 1:925){
  if(get_shp$AREA[i]>0.1){
    for(j in 1:33){
      if(get_shp$NAME[i]==get_csv$NAME[j]){
        get_shp$new1[i]<-get_csv$X1[j]
      }
    }
  }
}
setwd("c://HanryGIS//China-Province//")
spplot(get_shp,"new1",col=gray(5:1/6))
jpeg(file="simple.jpeg")
spplot(get_shp,"new1",col=gray(5:1/6))
dev.off()