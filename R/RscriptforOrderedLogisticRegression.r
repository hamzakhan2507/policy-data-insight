# 1. Load your data and fit the model (once)
Clean_RECS2020 <- read.csv("cleaned_data2020.csv", stringsAsFactors=FALSE)
Clean_RECS2020$SCALEE <- factor(Clean_RECS2020$SCALEE, levels=0:3, ordered=TRUE)
# Note: we’re leaving MONEYPY and RACE as numeric doubles
library(MASS)
m <- polr(SCALEE ~ MONEYPY + HOUSEHOLDER_RACE, data=Clean_RECS2020, Hess=TRUE)
# 2. Build a purely numeric grid (1:16, 1:6)
newdat <- expand.grid(
  MONEYPY          = 1:16,  # integer → will coerce to integer, so we fix it next
  HOUSEHOLDER_RACE = 1:6
)

# 3. Make them numeric doubles to match the model’s predictors
newdat$MONEYPY          <- as.numeric(newdat$MONEYPY)
newdat$HOUSEHOLDER_RACE <- as.numeric(newdat$HOUSEHOLDER_RACE)

# 4. Predict the four class‐probabilities
probs <- predict(m, newdata=newdat, type="probs")

# 5. Combine into one data frame
newdat_with_probs <- cbind(newdat, probs)

# 6. Melt to long form for ggplot
library(reshape2)
lnewdat <- melt(
  newdat_with_probs,
  id.vars       = c("MONEYPY", "HOUSEHOLDER_RACE"),
  variable.name = "SCALEE_Level",
  value.name    = "Probability"
)

# 7. (Optional) Turn the numeric codes into nicer factor labels
lnewdat$IncomeBracket <- factor(
  lnewdat$MONEYPY,
  levels = 1:16,
  labels = c(
    "Less than $5,000","$5,000–7,499","$7,500–9,999","$10,000–12,499",
    "$12,500–14,999","$15,000–19,999","$20,000–24,999","$25,000–29,999",
    "$30,000–34,999","$35,000–39,999","$40,000–49,999","$50,000–59,999",
    "$60,000–74,999","$75,000–99,999","$100,000–149,999","$150,000+"
  ),
  ordered = TRUE
)
lnewdat$RaceLabel <- factor(
  lnewdat$HOUSEHOLDER_RACE,
  levels = 1:6,
  labels = c(
    "White Alone","Black Alone","Am. Indian/AK Native",
    "Asian Alone","Pacific Isl.","Two+ Races"
  )
)

# 8. Plot with ggplot2
library(ggplot2)
ggplot(lnewdat, aes(x = IncomeBracket, y = Probability, colour = SCALEE_Level, group = SCALEE_Level)) +
  geom_line() +
  facet_grid(. ~ RaceLabel, labeller = label_both) +
  theme(
    axis.text.x     = element_text(angle = 45, hjust = 1),
    legend.position = "bottom"
  ) +
  labs(
    x     = "Income Bracket",
    title = "Predicted Probability of Disconnect‑Notice Frequency\nby Income & Race"
  )
scale_x_discrete(labels = function(x) stringr::str_wrap(x, width = 8))
library(ggplot2)
library(stringr)

ggplot(lnewdat,
       aes(x = IncomeBracket, y = Probability, 
           colour = SCALEE_Level, group = SCALEE_Level)) +
  geom_line(size = 1) +
  facet_wrap(~ RaceLabel, nrow = 2, ncol = 3) +
  scale_colour_brewer(palette = "Set2", name = "Disconnect Level") +
  scale_x_discrete(labels = function(x) str_wrap(x, width = 8)) +
  theme_light(base_size = 14) +
  theme(
    strip.text        = element_text(face = "bold", size = 12),
    axis.text.x       = element_text(angle = 45, hjust = 1),
    legend.position   = "top",
    panel.grid.minor  = element_blank()
  ) +
  labs(
    x     = "Income Bracket",
    y     = "Predicted Probability",
    title = "Predicted Disconnect Notice Frequency by Income & Race"
  )
