setwd(getSrcDirectory(function(){})[1])

packages <-c("edl","sigmoid","readr","plotfunctions","data.table","here")
lapply(packages, function(x) {if (!require(x, character.only=T)) {install.packages(x);require(x)}})

hyper.parameters <- read_csv('../data/hyper_parameters_R.csv',show_col_types = FALSE)
print(hyper.parameters[["train_data"]])
trainData <- read_csv(hyper.parameters[["train_data"]],show_col_types = FALSE)
train0 <- createTrainingData(trainData,nruns=hyper.parameters[["nruns"]], random=T)
wm.block <- RWlearning(train0, progress = F, eta = hyper.parameters[["eta"]])
wm <- getWM(wm.block)

testData <- read_csv(hyper.parameters[["test_data"]],show_col_types = FALSE)
actFrame <- data.frame(Cues=testData[["Cues"]],
                       Question=0,Statement=0,Outcomes=testData[["Outcomes"]])
for (r in 1:nrow(testData)){
  options.activations <- c(unlist(getActivations(wm, 
                                                 cueset = actFrame$Cues[r], 
                                                 select.outcomes = "question"))[1],
                           unlist(getActivations(wm, 
                                                 cueset = actFrame$Cues[r], 
                                                 select.outcomes = "statement"))[1])
  options.activations <- c(options.activations[[names(options.activations[1])]] ,
      options.activations[[names(options.activations[2])]])

  actFrame$Question[r] <-luceChoice(relu(options.activations[1]), relu(options.activations))
  actFrame$Statement[r] <-luceChoice(relu(options.activations[2]), relu(options.activations))
}

write.csv(actFrame,file=hyper.parameters[["probability_data"]], row.names=FALSE)
write.csv(wm,file='../data/train_weights.csv', row.names=TRUE)
