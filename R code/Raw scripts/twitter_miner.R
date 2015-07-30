library(twitteR)
library(streamR)

setwd("~/Documents/Projects/Twitter mining")
load("my_oauth.Rdata")
registerTwitterOAuth(my_oauth)

################################################################################
# FILTERSTREAM

end.date <- "2015-08-01"
keywords <- c("keyword", "another keyword", "etc.")

# Collect tweets until end.date in 3 hour sessions
while (Sys.Date() < end.date){
    current.time <- format(Sys.time(), "%Y_%m_%d_%H_%M")  #Save file
    file.name <- paste("Data/Raw data/tweets_", current.time, ".json", sep="")
    filterStream( file=file.name, track=keywords, lang = "en",
                  oauth=my_oauth, timeout=3600) ## capture tweets for 3600 seconds = 3 hours
}



