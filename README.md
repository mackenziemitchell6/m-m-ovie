# m-m-ovie
This project aimed to explore and analyze movie and actor data, with the aim of deriving insights
to advise a fictional start-up movie studio on ways to maximize profits and ensure success.

## Context
The idea of “personal brands” is growing through social media - actors & actresses have been able to advertise their projects more than ever before. We will focus on movie casts and their overall public brands for this analysis.

## Strategic Analysis
Different metrics of success of an actor’s personal brand such as salary, social media following, and overall popularity ranking will be used in order to determine if these metrics have an impact on profitability and success of a movie, what that impact may be, and which actors will improve the chance of producing a successful movie.

## Process
We sourced and scraped data from three sources:  IMDB, Fandango, and Fan Page List.
All data was sourced via web scraping (i.e., no REST API calls were used).

The data pipeline consisted of sourcing (scraping) data, cleaning it, loading it into
a MySQL DB on Amazon RDS, and visualizing the data with Matplotlib.


![](/graphs_saved_as_.png/data-pipeline.png)


## Analysis

![](/graphs_saved_as_.png/BO_v_Pop.png)

![](/graphs_saved_as_.png/BO_v_Social.png)

![](/graphs_saved_as_.png/BO_v_Sal.png)

![](/graphs_saved_as_.png/movies_3.png)

![](/graphs_saved_as_.png/movies_4.png)
