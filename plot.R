#Plot the data from calculation which will show the distribution of CpG percentage among positions

library("ggplot2")
library("dplyr")
data <- read.table(file = 'proopiomelanocortin_CpG.txt', header = F)
names(data) <- c('Position','Obs_Exp_CpG')
sp<-ggplot(data,aes(x = Position,y=Obs_Exp_CpG))+geom_line(color="orange")
sp + geom_hline(yintercept=0.6,linetype="dashed",col="magenta")
dev.off()
