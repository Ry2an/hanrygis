b=0
a<-vector(mode="numeric",length=2)
a[1]=73
a[2]=135
b<-vector(mode="numeric",length=2)
b[1]=3
b[2]=53
get_points<- read.csv(file='C://HanryGIS//China-Province//Points.csv',header=T)
setwd("c://HanryGIS//China-Province//")
plot(get_points$lon,get_points$lan,xlim=a,ylim=b,pch=16,col='red',axes=F,xlab="",ylab="")
png(file="points.png", bg="transparent")
plot(get_points$lon,get_points$lan,xlim=a,ylim=b,pch=16,col='red',axes=FALSE,xlab="",ylab="")
dev.off()