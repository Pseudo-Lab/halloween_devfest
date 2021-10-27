candy <- read.csv('candy-data.csv')

summary(candy)

library(ggplot2)
library(ggdendro)

rownames(candy) <- candy[,1]
candy <- candy[,-1]


hc <- hclust(dist(candy[,1:9]))
hcd <- as.dendrogram(hc)
ggdendrogram(hc, rotate = TRUE, theme_dendro = FALSE)
