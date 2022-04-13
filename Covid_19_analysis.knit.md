
<!-- rnb-text-begin -->

---
title: "COVID-19 Variants Analysis"
output: html_notebook
---


<!-- rnb-text-end -->



<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-output-begin eyJkYXRhIjoiRkFMU0UgUmVnaXN0ZXJlZCBTMyBtZXRob2RzIG92ZXJ3cml0dGVuIGJ5ICdkYnBseXInOlxuRkFMU0UgICBtZXRob2QgICAgICAgICBmcm9tXG5GQUxTRSAgIHByaW50LnRibF9sYXp5ICAgICBcbkZBTFNFICAgcHJpbnQudGJsX3NxbCAgICAgIFxuRkFMU0UgLS0gQXR0YWNoaW5nIHBhY2thZ2VzIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIHRpZHl2ZXJzZSAxLjMuMSAtLVxuRkFMU0UgdiBnZ3Bsb3QyIDMuMy41ICAgICB2IHB1cnJyICAgMC4zLjRcbkZBTFNFIHYgdGliYmxlICAzLjEuNiAgICAgdiBkcGx5ciAgIDEuMC43XG5GQUxTRSB2IHRpZHlyICAgMS4xLjQgICAgIHYgc3RyaW5nciAxLjQuMFxuRkFMU0UgdiByZWFkciAgIDIuMS4xICAgICB2IGZvcmNhdHMgMC41LjFcbkZBTFNFIC0tIENvbmZsaWN0cyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSB0aWR5dmVyc2VfY29uZmxpY3RzKCkgLS1cbkZBTFNFIHggZHBseXI6OmZpbHRlcigpIG1hc2tzIHN0YXRzOjpmaWx0ZXIoKVxuRkFMU0UgeCBkcGx5cjo6bGFnKCkgICAgbWFza3Mgc3RhdHM6OmxhZygpXG5GQUxTRSBcbkZBTFNFIEF0dGFjaGluZyBwYWNrYWdlOiDigJhzY2FsZXPigJlcbkZBTFNFIFxuRkFMU0UgVGhlIGZvbGxvd2luZyBvYmplY3QgaXMgbWFza2VkIGZyb20g4oCYcGFja2FnZTpwdXJycuKAmTpcbkZBTFNFIFxuRkFMU0UgICAgIGRpc2NhcmRcbkZBTFNFIFxuRkFMU0UgVGhlIGZvbGxvd2luZyBvYmplY3QgaXMgbWFza2VkIGZyb20g4oCYcGFja2FnZTpyZWFkcuKAmTpcbkZBTFNFIFxuRkFMU0UgICAgIGNvbF9mYWN0b3JcbkZBTFNFIFxuRkFMU0UgUmVnaXN0ZXJlZCBTMyBtZXRob2Qgb3ZlcndyaXR0ZW4gYnkgJ2RhdGEudGFibGUnOlxuRkFMU0UgICBtZXRob2QgICAgICAgICAgIGZyb21cbkZBTFNFICAgcHJpbnQuZGF0YS50YWJsZSAgICAgXG5GQUxTRSBSZWdpc3RlcmVkIFMzIG1ldGhvZCBvdmVyd3JpdHRlbiBieSAnaHRtbHdpZGdldHMnOlxuRkFMU0UgICBtZXRob2QgICAgICAgICAgIGZyb20gICAgICAgICBcbkZBTFNFICAgcHJpbnQuaHRtbHdpZGdldCB0b29sczpyc3R1ZGlvXG5GQUxTRSBcbkZBTFNFIEF0dGFjaGluZyBwYWNrYWdlOiDigJhwbG90bHnigJlcbkZBTFNFIFxuRkFMU0UgVGhlIGZvbGxvd2luZyBvYmplY3QgaXMgbWFza2VkIGZyb20g4oCYcGFja2FnZTpnZ3Bsb3Qy4oCZOlxuRkFMU0UgXG5GQUxTRSAgICAgbGFzdF9wbG90XG5GQUxTRSBcbkZBTFNFIFRoZSBmb2xsb3dpbmcgb2JqZWN0IGlzIG1hc2tlZCBmcm9tIOKAmHBhY2thZ2U6c3RhdHPigJk6XG5GQUxTRSBcbkZBTFNFICAgICBmaWx0ZXJcbkZBTFNFIFxuRkFMU0UgVGhlIGZvbGxvd2luZyBvYmplY3QgaXMgbWFza2VkIGZyb20g4oCYcGFja2FnZTpncmFwaGljc+KAmTpcbkZBTFNFIFxuRkFMU0UgICAgIGxheW91dFxuRkFMU0UgXG5GQUxTRSBkYXRhLnRhYmxlIDEuMTQuMiB1c2luZyA0IHRocmVhZHMgKHNlZSA/Z2V0RFR0aHJlYWRzKS4gIExhdGVzdCBuZXdzOiByLWRhdGF0YWJsZS5jb21cbkZBTFNFIFxuRkFMU0UgQXR0YWNoaW5nIHBhY2thZ2U6IOKAmGRhdGEudGFibGXigJlcbkZBTFNFIFxuRkFMU0UgVGhlIGZvbGxvd2luZyBvYmplY3RzIGFyZSBtYXNrZWQgZnJvbSDigJhwYWNrYWdlOmRwbHly4oCZOlxuRkFMU0UgXG5GQUxTRSAgICAgYmV0d2VlbiwgZmlyc3QsIGxhc3RcbkZBTFNFIFxuRkFMU0UgVGhlIGZvbGxvd2luZyBvYmplY3QgaXMgbWFza2VkIGZyb20g4oCYcGFja2FnZTpwdXJycuKAmTpcbkZBTFNFIFxuRkFMU0UgICAgIHRyYW5zcG9zZVxuRkFMU0UgXG5GQUxTRSBcbkZBTFNFIEF0dGFjaGluZyBwYWNrYWdlOiDigJhsdWJyaWRhdGXigJlcbkZBTFNFIFxuRkFMU0UgVGhlIGZvbGxvd2luZyBvYmplY3RzIGFyZSBtYXNrZWQgZnJvbSDigJhwYWNrYWdlOmRhdGEudGFibGXigJk6XG5GQUxTRSBcbkZBTFNFICAgICBob3VyLCBpc293ZWVrLCBtZGF5LCBtaW51dGUsIG1vbnRoLCBxdWFydGVyLCBzZWNvbmQsIHdkYXksIHdlZWssIHlkYXksIHllYXJcbkZBTFNFIFxuRkFMU0UgVGhlIGZvbGxvd2luZyBvYmplY3RzIGFyZSBtYXNrZWQgZnJvbSDigJhwYWNrYWdlOmJhc2XigJk6XG5GQUxTRSBcbkZBTFNFICAgICBkYXRlLCBpbnRlcnNlY3QsIHNldGRpZmYsIHVuaW9uXG5GQUxTRSBcbkZBTFNFIExvYWRpbmcgcmVxdWlyZWQgcGFja2FnZToga2FibGVFeHRyYVxuRkFMU0UgXG5GQUxTRSBBdHRhY2hpbmcgcGFja2FnZTog4oCYa2FibGVFeHRyYeKAmVxuRkFMU0UgXG5GQUxTRSBUaGUgZm9sbG93aW5nIG9iamVjdCBpcyBtYXNrZWQgZnJvbSDigJhwYWNrYWdlOmRwbHly4oCZOlxuRkFMU0UgXG5GQUxTRSAgICAgZ3JvdXBfcm93c1xuRkFMU0UgXG5GQUxTRSBcbkZBTFNFIEF0dGFjaGluZyBwYWNrYWdlOiDigJh0aW1ldGvigJlcbkZBTFNFIFxuRkFMU0UgVGhlIGZvbGxvd2luZyBvYmplY3QgaXMgbWFza2VkIGZyb20g4oCYcGFja2FnZTpkYXRhLnRhYmxl4oCZOlxuRkFMU0UgXG5GQUxTRSAgICAgOj1cbkZBTFNFIFxuRkFMU0UgTG9hZGluZyByZXF1aXJlZCBwYWNrYWdlOiBzdmRcbkZBTFNFIExvYWRpbmcgcmVxdWlyZWQgcGFja2FnZTogZm9yZWNhc3RcbkZBTFNFIFJlZ2lzdGVyZWQgUzMgbWV0aG9kIG92ZXJ3cml0dGVuIGJ5ICdxdWFudG1vZCc6XG5GQUxTRSAgIG1ldGhvZCAgICAgICAgICAgIGZyb21cbkZBTFNFICAgYXMuem9vLmRhdGEuZnJhbWUgem9vIFxuRkFMU0UgXG5GQUxTRSBBdHRhY2hpbmcgcGFja2FnZTog4oCYUnNzYeKAmVxuRkFMU0UgXG5GQUxTRSBUaGUgZm9sbG93aW5nIG9iamVjdCBpcyBtYXNrZWQgZnJvbSDigJhwYWNrYWdlOnN0YXRz4oCZOlxuRkFMU0UgXG5GQUxTRSAgICAgZGVjb21wb3NlXG4ifQ== -->

```
FALSE Registered S3 methods overwritten by 'dbplyr':
FALSE   method         from
FALSE   print.tbl_lazy     
FALSE   print.tbl_sql      
FALSE -- Attaching packages -------------------------------------------------------------------------------------------------------- tidyverse 1.3.1 --
FALSE v ggplot2 3.3.5     v purrr   0.3.4
FALSE v tibble  3.1.6     v dplyr   1.0.7
FALSE v tidyr   1.1.4     v stringr 1.4.0
FALSE v readr   2.1.1     v forcats 0.5.1
FALSE -- Conflicts ----------------------------------------------------------------------------------------------------------- tidyverse_conflicts() --
FALSE x dplyr::filter() masks stats::filter()
FALSE x dplyr::lag()    masks stats::lag()
FALSE 
FALSE Attaching package: ‘scales’
FALSE 
FALSE The following object is masked from ‘package:purrr’:
FALSE 
FALSE     discard
FALSE 
FALSE The following object is masked from ‘package:readr’:
FALSE 
FALSE     col_factor
FALSE 
FALSE Registered S3 method overwritten by 'data.table':
FALSE   method           from
FALSE   print.data.table     
FALSE Registered S3 method overwritten by 'htmlwidgets':
FALSE   method           from         
FALSE   print.htmlwidget tools:rstudio
FALSE 
FALSE Attaching package: ‘plotly’
FALSE 
FALSE The following object is masked from ‘package:ggplot2’:
FALSE 
FALSE     last_plot
FALSE 
FALSE The following object is masked from ‘package:stats’:
FALSE 
FALSE     filter
FALSE 
FALSE The following object is masked from ‘package:graphics’:
FALSE 
FALSE     layout
FALSE 
FALSE data.table 1.14.2 using 4 threads (see ?getDTthreads).  Latest news: r-datatable.com
FALSE 
FALSE Attaching package: ‘data.table’
FALSE 
FALSE The following objects are masked from ‘package:dplyr’:
FALSE 
FALSE     between, first, last
FALSE 
FALSE The following object is masked from ‘package:purrr’:
FALSE 
FALSE     transpose
FALSE 
FALSE 
FALSE Attaching package: ‘lubridate’
FALSE 
FALSE The following objects are masked from ‘package:data.table’:
FALSE 
FALSE     hour, isoweek, mday, minute, month, quarter, second, wday, week, yday, year
FALSE 
FALSE The following objects are masked from ‘package:base’:
FALSE 
FALSE     date, intersect, setdiff, union
FALSE 
FALSE Loading required package: kableExtra
FALSE 
FALSE Attaching package: ‘kableExtra’
FALSE 
FALSE The following object is masked from ‘package:dplyr’:
FALSE 
FALSE     group_rows
FALSE 
FALSE 
FALSE Attaching package: ‘timetk’
FALSE 
FALSE The following object is masked from ‘package:data.table’:
FALSE 
FALSE     :=
FALSE 
FALSE Loading required package: svd
FALSE Loading required package: forecast
FALSE Registered S3 method overwritten by 'quantmod':
FALSE   method            from
FALSE   as.zoo.data.frame zoo 
FALSE 
FALSE Attaching package: ‘Rssa’
FALSE 
FALSE The following object is masked from ‘package:stats’:
FALSE 
FALSE     decompose
```



<!-- rnb-output-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->




<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->



<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuY292aWQkZGF0ZSAlPiUgXG4gIHJhbmdlKClcblxuZ2lzYWlkJGRhdGUgJT4lIFxuICByYW5nZSgpXG5gYGAifQ== -->

```r
covid$date %>% 
  range()

gisaid$date %>% 
  range()
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuY292aWRfTkFzIDwtIGNvdmlkICU+JSBcbiAgZ3JvdXBfYnkobG9jYXRpb24pICU+JSBcbiAgc3VtbWFyaXNlX2FsbChmdW5zKHN1bShpcy5uYSguKSkpKSAlPiUgXG4gIHBpdm90X2xvbmdlcihjb2xzID0gLWxvY2F0aW9uLCBuYW1lc190byA9IFwiVmFyaWFibGVcIiwgdmFsdWVzX3RvID0gXCJOQXNcIikgJT4lIFxuICBtdXRhdGUoUGVyY2VudCA9IHJvdW5kKE5BcyAvIG5yb3coY292aWQpICogMTAwICwyKSkgJT4lIFxuICBhcnJhbmdlKC1OQXMpXG5gYGAifQ== -->

```r
covid_NAs <- covid %>% 
  group_by(location) %>% 
  summarise_all(funs(sum(is.na(.)))) %>% 
  pivot_longer(cols = -location, names_to = "Variable", values_to = "NAs") %>% 
  mutate(Percent = round(NAs / nrow(covid) * 100 ,2)) %>% 
  arrange(-NAs)
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuY292aWRfTkFzICU+JSBcbiAgZ3JvdXBfYnkobG9jYXRpb24pICU+JSBcbiAgc3VtbWFyaXNlKHRvdGFsX3BjdF9uYSA9IHN1bShQZXJjZW50KSkgJT4lIFxuICBhcnJhbmdlKHRvdGFsX3BjdF9uYSkgJT4lIFxuICBkYXRhdGFibGUoZmlsdGVyID0gJ3RvcCcpXG5gYGAifQ== -->

```r
covid_NAs %>% 
  group_by(location) %>% 
  summarise(total_pct_na = sum(Percent)) %>% 
  arrange(total_pct_na) %>% 
  datatable(filter = 'top')
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuI0hlbHBlciBmdW5jdGlvbiBmb3IgZmlsdGVyaW5nIGRhdGFcbm15X2RhdGEgPC0gZnVuY3Rpb24oY291bnRyeV9jb3ZpZF9maWx0ZXIsIGNvdW50cnlfZ2lzYWlkX2ZpbHRlcil7XG4gIGRhdGEgPC0gY292aWQgJT4lIFxuICAgIGZpbHRlcihsb2NhdGlvbiA9PSBjb3VudHJ5X2NvdmlkX2ZpbHRlcilcbiAgZ2lzYWlkX2RhdGEgPC0gZ2lzYWlkX3ZhcmlhbnRzICU+JSBcbiAgICBmaWx0ZXIoQ291bnRyeSA9PSBjb3VudHJ5X2dpc2FpZF9maWx0ZXIpXG4gIGRhdGEgPC0gbGVmdF9qb2luKGRhdGEsIGdpc2FpZF9kYXRhLCBieSA9IFwiZGF0ZVwiKVxuICBkYXRhXG59XG5cbnVzIDwtIG15X2RhdGEoXCJVbml0ZWQgU3RhdGVzXCIsIFwiVVNBXCIpXG5gYGAifQ== -->

```r
#Helper function for filtering data
my_data <- function(country_covid_filter, country_gisaid_filter){
  data <- covid %>% 
    filter(location == country_covid_filter)
  gisaid_data <- gisaid_variants %>% 
    filter(Country == country_gisaid_filter)
  data <- left_join(data, gisaid_data, by = "date")
  data
}

us <- my_data("United States", "USA")
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->




<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxudmFyaWFudHNfcGxvdCA8LSBnZ3Bsb3QoZGF0YSA9IHVzLCBhZXMoeCA9IGRhdGUpKSArXG4gIGdlb21fYXJlYShhZXMoeSA9IHBlcmNfc2VxdWVuY2VzLCBjb2xvciA9IHZhcmlhbnQsIGZpbGwgPSB2YXJpYW50KSwgcG9zaXRpb24gPSBcImRvZGdlXCIsIHNob3cubGVnZW5kID0gRkFMU0UpICtcbiAgdGhlbWVfbWluaW1hbCgpXG5cblxuY2FzZXNfcGxvdCA8LVxuICBnZ3Bsb3QoZGF0YSA9IHVzLCBhZXMoeCA9IGRhdGUpKSArXG4gIGdlb21fbGluZShhZXMoeSA9IG5ld19jYXNlc19wZXJfbWlsbGlvbiksIHNob3cubGVnZW5kID0gRkFMU0UpICtcbiAgZ2VvbV9saW5lKGFlcyh5ID0gbmV3X2RlYXRoc19wZXJfbWlsbGlvbikpICsgXG4gIHRoZW1lX21pbmltYWwoKVxuXG5cbmRlYXRoc19wbG90IDwtIGdncGxvdChkYXRhID0gdXMsIGFlcyh4ID0gZGF0ZSkpICtcbiAgZ2VvbV9saW5lKGFlcyh5ID0gbmV3X2RlYXRoc19wZXJfbWlsbGlvbikpICsgXG4gIHRoZW1lX21pbmltYWwoKVxuXG5cbnZhY2NpbmF0aW9uc19wbG90IDwtIGdncGxvdCh1cywgYWVzKHggPSBkYXRlKSkgK1xuICBnZW9tX2xpbmUoYWVzKHkgPSBuZXdfdmFjY2luYXRpb25zX3Ntb290aGVkX3Blcl9taWxsaW9uKSkgK1xuICB0aGVtZV9taW5pbWFsKClcblxuXG52YXJpYW50c19jYXNlc19wbG90IDwtIGdncGxvdChkYXRhID0gdXMsIGFlcyh4ID0gZGF0ZSkpICsgXG4gIGdlb21fYXJlYShhZXMoeSA9IHBlcmNfc2VxdWVuY2VzLCBjb2xvciA9IHZhcmlhbnQsIGZpbGwgPSB2YXJpYW50KSwgc2hvdy5sZWdlbmQgPUZBTFNFLCBhbHBoYSA9IDAuNSwgcG9zaXRpb24gPSBcImRvZGdlXCIpICsgXG4gIGdlb21fbGluZShhZXMoeSA9IG5ld19jYXNlc19zbW9vdGhlZF9wZXJfbWlsbGlvbiAvIDQwKSkgKyBcbiAgc2NhbGVfeV9jb250aW51b3VzKFwiUGVyY2VudCBvZiBTZXF1ZW5jZXNcIiwgc2VjLmF4aXM9c2VjX2F4aXMofi4qNDAsIG5hbWUgPSBcIk5ldyBDYXNlcyBQZXIgTWlsbGlvblwiKSkgKyBcbiAgdGhlbWVfbWluaW1hbCgpICsgXG4gIGxhYnModGl0bGUgPSBcIlByb3BvcnRpb24gb2YgQ292aWQgVmFyaWFudHMgdnMgTmV3IENhc2VzIFBlciBNaWxsaW9uXCIpICArXG4gIGFubm90YXRlKGdlb209XCJsYWJlbFwiLCB4PXltZCgyMDIwMDcwMSksIHk9NzUsIGxhYmVsPVwiQWxwaGEvT3RoZXJcIikgK1xuICBhbm5vdGF0ZShnZW9tPVwibGFiZWxcIiwgeD15bWQoMjAyMTA5MDEpLCB5PTc1LCBsYWJlbD1cIkRlbHRhXCIpICtcbiAgYW5ub3RhdGUoZ2VvbT1cImxhYmVsXCIsIHg9eW1kKDIwMjIwMjAxKSwgeT03NSwgbGFiZWw9XCJPbWljcm9uXCIpXG5cblxudmFyaWFudHNfZGVhdGhzX3Bsb3QgPC0gZ2dwbG90KGRhdGEgPSB1cywgYWVzKHggPSBkYXRlKSkgKyBcbiAgZ2VvbV9hcmVhKGFlcyh5ID0gcGVyY19zZXF1ZW5jZXMsIGNvbG9yID0gdmFyaWFudCwgZmlsbCA9IHZhcmlhbnQpLHNob3cubGVnZW5kID1GQUxTRSwgYWxwaGEgPSAwLjUsIHBvc2l0aW9uID0gXCJkb2RnZVwiKSArIFxuICBnZW9tX2xpbmUoYWVzKHkgPSBuZXdfZGVhdGhzX3Ntb290aGVkX3Blcl9taWxsaW9uKjUpKSArIFxuICBzY2FsZV95X2NvbnRpbnVvdXMoXCJQZXJjZW50IG9mIFNlcXVlbmNlc1wiLCBzZWMuYXhpcz1zZWNfYXhpcyh+Li81LCBuYW1lID0gXCJOZXcgRGVhdGhzIFBlciBNaWxsaW9uXCIpKSArIFxuICB0aGVtZV9taW5pbWFsKCkgKyBcbiAgbGFicyh0aXRsZSA9IFwiUHJvcG9ydGlvbiBvZiBDb3ZpZCBWYXJpYW50cyB2cyBOZXcgRGVhdGhzIFBlciBNaWxsaW9uXCIpICtcbiAgYW5ub3RhdGUoZ2VvbT1cImxhYmVsXCIsIHg9eW1kKDIwMjAwNzAxKSwgeT03NSwgbGFiZWw9XCJBbHBoYS9PdGhlclwiKSArXG4gIGFubm90YXRlKGdlb209XCJsYWJlbFwiLCB4PXltZCgyMDIxMDkwMSksIHk9NzUsIGxhYmVsPVwiRGVsdGFcIikgK1xuICBhbm5vdGF0ZShnZW9tPVwibGFiZWxcIiwgeD15bWQoMjAyMjAyMDEpLCB5PTc1LCBsYWJlbD1cIk9taWNyb25cIilcblxuXG5jYXNlc192YWNjaW5hdGlvbnNfcGxvdCA8LSBnZ3Bsb3QoZGF0YSA9IHVzLCBhZXMoeCA9IGRhdGUpKSArXG4gIGdlb21fbGluZShhZXMoeSA9IG5ld19jYXNlc19zbW9vdGhlZF9wZXJfbWlsbGlvbiksIHNob3cubGVnZW5kID0gRkFMU0UpICtcbiAgZ2VvbV9saW5lKGFlcyh5ID0gcGVvcGxlX3ZhY2NpbmF0ZWRfcGVyX2h1bmRyZWQqNTApKSArIFxuICBzY2FsZV95X2NvbnRpbnVvdXMoXCJOZXcgQ2FzZXMgUGVyIE1pbGxpb25cIiwgc2VjLmF4aXM9c2VjX2F4aXMofi4vNTAsIG5hbWUgPSBcIlBlb3BsZSBWYWNjaW5hdGVkIFBlciBIdW5kcmVkXCIpKSArIFxuICB0aGVtZV9taW5pbWFsKCkgKyBcbiAgbGFicyh0aXRsZSA9IFwiTmV3IENhc2VzIFBlciBNaWxsaW9uIHZzLiBQZW9wbGUgVmFjY2luYXRlZCBQZXIgSHVuZHJlZFwiKVxuXG5kZWF0aHNfdmFjY2luYXRpb25zX3Bsb3QgPC0gZ2dwbG90KHVzLCBhZXMoeCA9IGRhdGUpKSArXG4gIGdlb21fbGluZShhZXMoeSA9IG5ld19kZWF0aHNfcGVyX21pbGxpb24pLCBzaG93LmxlZ2VuZCA9IEZBTFNFKSArXG4gIGdlb21fbGluZShhZXMoeSA9IHBlb3BsZV9mdWxseV92YWNjaW5hdGVkX3Blcl9odW5kcmVkLzcpKSArIFxuICBzY2FsZV95X2NvbnRpbnVvdXMoXCJOZXcgRGVhdGhzIFBlciBNaWxsaW9uXCIsIHNlYy5heGlzPXNlY19heGlzKH4uKjcsIG5hbWUgPSBcIlBlb3BsZSBWYWNjaW5hdGVkIFBlciBIdW5kcmVkXCIpKSArIFxuICB0aGVtZV9taW5pbWFsKCkgKyBcbiAgbGFicyh0aXRsZSA9IFwiTmV3IERlYXRocyBQZXIgTWlsbGlvbiB2cy4gUGVvcGxlIEZ1bGx5IFZhY2NpbmF0ZWQgUGVyIEh1bmRyZWRcIilcblxuXG52YXJpYW50c19ob3NwaXRhbGl6YXRpb25zX3Bsb3QgPC0gZ2dwbG90KHVzLCBhZXMoeCA9IGRhdGUpKSArIFxuICBnZW9tX2FyZWEoYWVzKHkgPSBwZXJjX3NlcXVlbmNlcywgY29sb3IgPSB2YXJpYW50LCBmaWxsID0gdmFyaWFudCksIHNob3cubGVnZW5kID1GQUxTRSwgYWxwaGEgPSAwLjUsIHBvc2l0aW9uID0gXCJkb2RnZVwiKSArIFxuICBnZW9tX2xpbmUoYWVzKHkgPSB3ZWVrbHlfaG9zcF9hZG1pc3Npb25zX3Blcl9taWxsaW9uIC8gNSkpICsgXG4gIHNjYWxlX3lfY29udGludW91cyhcIlBlcmNlbnQgb2YgU2VxdWVuY2VzXCIsIHNlYy5heGlzPXNlY19heGlzKH4uKjUsIG5hbWUgPSBcIkhvc3BpdGFsaXphdGlvbnMgUGVyIE1pbGxpb25cIikpICsgXG4gIHRoZW1lX21pbmltYWwoKSArIFxuICBsYWJzKHRpdGxlID0gXCJQcm9wb3J0aW9uIG9mIENvdmlkIFZhcmlhbnRzIHZzIEhvc3BpdGFsaXphdGlvbnMgUGVyIE1pbGxpb25cIikgK1xuICBhbm5vdGF0ZShnZW9tPVwibGFiZWxcIiwgeD15bWQoMjAyMDA3MDEpLCB5PTc1LCBsYWJlbD1cIkFscGhhL090aGVyXCIpICtcbiAgYW5ub3RhdGUoZ2VvbT1cImxhYmVsXCIsIHg9eW1kKDIwMjEwOTAxKSwgeT03NSwgbGFiZWw9XCJEZWx0YVwiKSArXG4gIGFubm90YXRlKGdlb209XCJsYWJlbFwiLCB4PXltZCgyMDIyMDIwMSksIHk9NzUsIGxhYmVsPVwiT21pY3JvblwiKVxuXG52YXJpYW50c192YWNjaW5hdGlvbnNfcGxvdCA8LSBnZ3Bsb3QodXMsIGFlcyh4ID0gZGF0ZSkpICsgXG4gIGdlb21fYXJlYShhZXMoeSA9IHBlcmNfc2VxdWVuY2VzLCBjb2xvciA9IHZhcmlhbnQsIGZpbGwgPSB2YXJpYW50KSwgc2hvdy5sZWdlbmQgPUZBTFNFLCBhbHBoYSA9IDAuNSwgcG9zaXRpb24gPSBcImRvZGdlXCIpICsgXG4gIGdlb21fbGluZShhZXMoeSA9IHBlb3BsZV9mdWxseV92YWNjaW5hdGVkX3Blcl9odW5kcmVkKSkgKyBcbiAgc2NhbGVfeV9jb250aW51b3VzKFwiUGVyY2VudCBvZiBTZXF1ZW5jZXNcIiwgc2VjLmF4aXM9c2VjX2F4aXMofi4sIG5hbWUgPSBcIlBlb3BsZSBWYWNjaW5hdGVkIFBlciBIdW5kcmVkXCIpKSArIFxuICB0aGVtZV9taW5pbWFsKCkgKyBcbiAgbGFicyh0aXRsZSA9IFwiUHJvcG9ydGlvbiBvZiBDb3ZpZCBWYXJpYW50cyB2cyBQZW9wbGUgRnVsbHkgVmFjY2luYXRlZFwiKSArXG4gIGFubm90YXRlKGdlb209XCJsYWJlbFwiLCB4PXltZCgyMDIwMDcwMSksIHk9NzUsIGxhYmVsPVwiQWxwaGEvT3RoZXJcIikgK1xuICBhbm5vdGF0ZShnZW9tPVwibGFiZWxcIiwgeD15bWQoMjAyMTA5MDEpLCB5PTc1LCBsYWJlbD1cIkRlbHRhXCIpICtcbiAgYW5ub3RhdGUoZ2VvbT1cImxhYmVsXCIsIHg9eW1kKDIwMjIwMjAxKSwgeT03NSwgbGFiZWw9XCJPbWljcm9uXCIpXG5cbnZhcmlhbnRzX3ZhY2NpbmF0aW9uc19wbG90XG5gYGAifQ== -->

```r
variants_plot <- ggplot(data = us, aes(x = date)) +
  geom_area(aes(y = perc_sequences, color = variant, fill = variant), position = "dodge", show.legend = FALSE) +
  theme_minimal()


cases_plot <-
  ggplot(data = us, aes(x = date)) +
  geom_line(aes(y = new_cases_per_million), show.legend = FALSE) +
  geom_line(aes(y = new_deaths_per_million)) + 
  theme_minimal()


deaths_plot <- ggplot(data = us, aes(x = date)) +
  geom_line(aes(y = new_deaths_per_million)) + 
  theme_minimal()


vaccinations_plot <- ggplot(us, aes(x = date)) +
  geom_line(aes(y = new_vaccinations_smoothed_per_million)) +
  theme_minimal()


variants_cases_plot <- ggplot(data = us, aes(x = date)) + 
  geom_area(aes(y = perc_sequences, color = variant, fill = variant), show.legend =FALSE, alpha = 0.5, position = "dodge") + 
  geom_line(aes(y = new_cases_smoothed_per_million / 40)) + 
  scale_y_continuous("Percent of Sequences", sec.axis=sec_axis(~.*40, name = "New Cases Per Million")) + 
  theme_minimal() + 
  labs(title = "Proportion of Covid Variants vs New Cases Per Million")  +
  annotate(geom="label", x=ymd(20200701), y=75, label="Alpha/Other") +
  annotate(geom="label", x=ymd(20210901), y=75, label="Delta") +
  annotate(geom="label", x=ymd(20220201), y=75, label="Omicron")


variants_deaths_plot <- ggplot(data = us, aes(x = date)) + 
  geom_area(aes(y = perc_sequences, color = variant, fill = variant),show.legend =FALSE, alpha = 0.5, position = "dodge") + 
  geom_line(aes(y = new_deaths_smoothed_per_million*5)) + 
  scale_y_continuous("Percent of Sequences", sec.axis=sec_axis(~./5, name = "New Deaths Per Million")) + 
  theme_minimal() + 
  labs(title = "Proportion of Covid Variants vs New Deaths Per Million") +
  annotate(geom="label", x=ymd(20200701), y=75, label="Alpha/Other") +
  annotate(geom="label", x=ymd(20210901), y=75, label="Delta") +
  annotate(geom="label", x=ymd(20220201), y=75, label="Omicron")


cases_vaccinations_plot <- ggplot(data = us, aes(x = date)) +
  geom_line(aes(y = new_cases_smoothed_per_million), show.legend = FALSE) +
  geom_line(aes(y = people_vaccinated_per_hundred*50)) + 
  scale_y_continuous("New Cases Per Million", sec.axis=sec_axis(~./50, name = "People Vaccinated Per Hundred")) + 
  theme_minimal() + 
  labs(title = "New Cases Per Million vs. People Vaccinated Per Hundred")

deaths_vaccinations_plot <- ggplot(us, aes(x = date)) +
  geom_line(aes(y = new_deaths_per_million), show.legend = FALSE) +
  geom_line(aes(y = people_fully_vaccinated_per_hundred/7)) + 
  scale_y_continuous("New Deaths Per Million", sec.axis=sec_axis(~.*7, name = "People Vaccinated Per Hundred")) + 
  theme_minimal() + 
  labs(title = "New Deaths Per Million vs. People Fully Vaccinated Per Hundred")


variants_hospitalizations_plot <- ggplot(us, aes(x = date)) + 
  geom_area(aes(y = perc_sequences, color = variant, fill = variant), show.legend =FALSE, alpha = 0.5, position = "dodge") + 
  geom_line(aes(y = weekly_hosp_admissions_per_million / 5)) + 
  scale_y_continuous("Percent of Sequences", sec.axis=sec_axis(~.*5, name = "Hospitalizations Per Million")) + 
  theme_minimal() + 
  labs(title = "Proportion of Covid Variants vs Hospitalizations Per Million") +
  annotate(geom="label", x=ymd(20200701), y=75, label="Alpha/Other") +
  annotate(geom="label", x=ymd(20210901), y=75, label="Delta") +
  annotate(geom="label", x=ymd(20220201), y=75, label="Omicron")

variants_vaccinations_plot <- ggplot(us, aes(x = date)) + 
  geom_area(aes(y = perc_sequences, color = variant, fill = variant), show.legend =FALSE, alpha = 0.5, position = "dodge") + 
  geom_line(aes(y = people_fully_vaccinated_per_hundred)) + 
  scale_y_continuous("Percent of Sequences", sec.axis=sec_axis(~., name = "People Vaccinated Per Hundred")) + 
  theme_minimal() + 
  labs(title = "Proportion of Covid Variants vs People Fully Vaccinated") +
  annotate(geom="label", x=ymd(20200701), y=75, label="Alpha/Other") +
  annotate(geom="label", x=ymd(20210901), y=75, label="Delta") +
  annotate(geom="label", x=ymd(20220201), y=75, label="Omicron")

variants_vaccinations_plot
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxudmFjY2luYXRpb25zX3Bsb3RcbmBgYCJ9 -->

```r
vaccinations_plot
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxudmFyaWFudHNfY2FzZXNfcGxvdCA8LSBnZ3Bsb3QoZGF0YSA9IHVzLCBhZXMoeCA9IGRhdGUpKSArIFxuICBnZW9tX2FyZWEoYWVzKHkgPSBwZXJjX3NlcXVlbmNlcywgY29sb3IgPSB2YXJpYW50LCBmaWxsID0gdmFyaWFudCksIHNob3cubGVnZW5kID1GQUxTRSwgYWxwaGEgPSAwLjUsIHBvc2l0aW9uID0gXCJkb2RnZVwiKSArIFxuICBnZW9tX2xpbmUoYWVzKHkgPSBuZXdfY2FzZXNfc21vb3RoZWRfcGVyX21pbGxpb24gLyA0MCkpICsgXG4gIHNjYWxlX3lfY29udGludW91cyhcIlBlcmNlbnQgb2YgU2VxdWVuY2VzXCIsIHNlYy5heGlzPXNlY19heGlzKH4uKjQwLCBuYW1lID0gXCJOZXcgQ2FzZXMgUGVyIE1pbGxpb25cIikpICsgXG4gIHRoZW1lX21pbmltYWwoKSArIFxuICBsYWJzKHRpdGxlID0gXCJQcm9wb3J0aW9uIG9mIENvdmlkIFZhcmlhbnRzIHZzIE5ldyBDYXNlcyBQZXIgTWlsbGlvblwiKSArXG4gIGFubm90YXRlKGdlb209XCJsYWJlbFwiLCB4PXltZCgyMDIwMDcwMSksIHk9NzUsIGxhYmVsPVwiQWxwaGEvT3RoZXJcIikgK1xuICBhbm5vdGF0ZShnZW9tPVwibGFiZWxcIiwgeD15bWQoMjAyMTA5MDEpLCB5PTc1LCBsYWJlbD1cIkRlbHRhXCIpICtcbiAgYW5ub3RhdGUoZ2VvbT1cImxhYmVsXCIsIHg9eW1kKDIwMjIwMjAxKSwgeT03NSwgbGFiZWw9XCJPbWljcm9uXCIpXG5cbnZhcmlhbnRzX2Nhc2VzX3Bsb3RcbmBgYCJ9 -->

```r
variants_cases_plot <- ggplot(data = us, aes(x = date)) + 
  geom_area(aes(y = perc_sequences, color = variant, fill = variant), show.legend =FALSE, alpha = 0.5, position = "dodge") + 
  geom_line(aes(y = new_cases_smoothed_per_million / 40)) + 
  scale_y_continuous("Percent of Sequences", sec.axis=sec_axis(~.*40, name = "New Cases Per Million")) + 
  theme_minimal() + 
  labs(title = "Proportion of Covid Variants vs New Cases Per Million") +
  annotate(geom="label", x=ymd(20200701), y=75, label="Alpha/Other") +
  annotate(geom="label", x=ymd(20210901), y=75, label="Delta") +
  annotate(geom="label", x=ymd(20220201), y=75, label="Omicron")

variants_cases_plot
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxudmFyaWFudHNfaG9zcGl0YWxpemF0aW9uc19wbG90XG5gYGAifQ== -->

```r
variants_hospitalizations_plot
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxudmFyaWFudHNfZGVhdGhzX3Bsb3RcbmBgYCJ9 -->

```r
variants_deaths_plot
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



# Time Series Analysis


<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxudXMgJT4lIFxuICBwbG90X3RpbWVfc2VyaWVzKGRhdGUsIG5ld19jYXNlc19zbW9vdGhlZF9wZXJfbWlsbGlvbilcbmBgYCJ9 -->

```r
us %>% 
  plot_time_series(date, new_cases_smoothed_per_million)
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxudXMgJT4lIFxuICBwbG90X2FjZl9kaWFnbm9zdGljcyhkYXRlLCBuZXdfY2FzZXNfc21vb3RoZWRfcGVyX21pbGxpb24sIC5zaG93X3doaXRlX25vaXNlX2JhcnMgPSBUKSBcbmBgYCJ9 -->

```r
us %>% 
  plot_acf_diagnostics(date, new_cases_smoothed_per_million, .show_white_noise_bars = T) 
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->




<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuZ2lzYWlkX3ZhcmlhbnRzICU+JSBcbiAgZmlsdGVyKENvdW50cnkgPT0gXCJVU0FcIiwgdmFyaWFudCAlaW4lIGMoXCJWT0MgT21pY3JvbiBHUkEgKEIuMS4xLjUyOStCQS4qKSBcIiwgXCJWT0MgRGVsdGEgR0sgKEIuMS42MTcuMitBWS4qKSBcIiwgXCJWT0MgQWxwaGEgR1JZIChCLjEuMS43K1EuKikgXCIpKSAlPiUgXG4gIHBsb3RfdGltZV9zZXJpZXMoZGF0ZSwgcGVyY19zZXF1ZW5jZXMsIC5mYWNldF92YXJzPXZhcmlhbnQsIC5sZWdlbmRfc2hvdyA9IEZBTFNFKVxuYGBgIn0= -->

```r
gisaid_variants %>% 
  filter(Country == "USA", variant %in% c("VOC Omicron GRA (B.1.1.529+BA.*) ", "VOC Delta GK (B.1.617.2+AY.*) ", "VOC Alpha GRY (B.1.1.7+Q.*) ")) %>% 
  plot_time_series(date, perc_sequences, .facet_vars=variant, .legend_show = FALSE)
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuZ2lzYWlkX3ZhcmlhbnRzICU+JSBcbiAgZmlsdGVyKENvdW50cnkgPT0gXCJVU0FcIiwgdmFyaWFudCAlaW4lIGMoXCJWT0MgT21pY3JvbiBHUkEgKEIuMS4xLjUyOStCQS4qKSBcIiwgXCJWT0MgRGVsdGEgR0sgKEIuMS42MTcuMitBWS4qKSBcIiwgXCJWT0MgQWxwaGEgR1JZIChCLjEuMS43K1EuKikgXCIpKSAlPiUgXG4gIGdyb3VwX2J5KHZhcmlhbnQpICU+JSBcbiAgcGxvdF9hY2ZfZGlhZ25vc3RpY3MoZGF0ZSwgcGVyY19zZXF1ZW5jZXMsIC5zaG93X3doaXRlX25vaXNlX2JhcnMgPSBUKSBcbmBgYCJ9 -->

```r
gisaid_variants %>% 
  filter(Country == "USA", variant %in% c("VOC Omicron GRA (B.1.1.529+BA.*) ", "VOC Delta GK (B.1.617.2+AY.*) ", "VOC Alpha GRY (B.1.1.7+Q.*) ")) %>% 
  group_by(variant) %>% 
  plot_acf_diagnostics(date, perc_sequences, .show_white_noise_bars = T) 
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxubGlicmFyeShcInNmXCIpXG5saWJyYXJ5KFwicm5hdHVyYWxlYXJ0aFwiKVxubGlicmFyeShcInJuYXR1cmFsZWFydGhkYXRhXCIpXG5cbndvcmxkIDwtIG5lX2NvdW50cmllcyhzY2FsZSA9IFwibWVkaXVtXCIsIHJldHVybmNsYXNzID0gXCJzZlwiKVxuY2xhc3Mod29ybGQpXG5gYGAifQ== -->

```r
library("sf")
library("rnaturalearth")
library("rnaturalearthdata")

world <- ne_countries(scale = "medium", returnclass = "sf")
class(world)
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxudW5pcXVlKGdpc2FpZCRDb3VudHJ5KVxuYGBgIn0= -->

```r
unique(gisaid$Country)
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxudW5pcXVlKGNvdmlkJGxvY2F0aW9uKVxuYGBgIn0= -->

```r
unique(covid$location)
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->




<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxud29ybGRfdmFyaWFudHMgPC0gZ2lzYWlkICU+JSBcbiAgZ3JvdXBfYnkoQ291bnRyeSkgJT4lIFxuICBtdXRhdGUoQ291bnRyeSA9IGNhc2Vfd2hlbihcbiAgQ291bnRyeSA9PSBcIlVTQVwiIH4gXCJVbml0ZWQgU3RhdGVzXCIsXG4gIFRSVUUgfiBhcy5jaGFyYWN0ZXIoQ291bnRyeSlcbiAgKSkgJT4lIFxuICBzdW1tYXJpc2UobW9zdF9yZWNlbnRfZGF0ZSA9IGRhdGVbbigpXSwgXG4gICAgICAgICAgICBwcmV2YWxlbnRfdmFyaWFudCA9IHZhcmlhbnRbZGF0ZSA9PSBkYXRlW24oKV0gJiBUeXBlID09IFwiVmFyaWFudFwiICYgcGVyY19zZXF1ZW5jZXMgPT0gbWF4KHBlcmNfc2VxdWVuY2VzKV0pICU+JSBcbiAgICAgICAgICAgICNwcmV2YWxlbnRfbGluZWFnZSA9IHZhcmlhbnRbZGF0ZSA9PSBkYXRlW24oKV0gJiBUeXBlID09IFwiTGluZWFnZVwiICYgcGVyY19zZXF1ZW5jZXMgPT0gbWF4KHBlcmNfc2VxdWVuY2VzKV0pICU+JSBcbiAgcmVuYW1lKGxvY2F0aW9uID0gQ291bnRyeSlcblxud29ybGRfdmFyaWFudHMgPC0gbGVmdF9qb2luKHdvcmxkX3ZhcmlhbnRzLCBjb3ZpZFssIGMoXCJsb2NhdGlvblwiLCBcImlzb19jb2RlXCIpXSwgYnkgPSBcImxvY2F0aW9uXCIsIGFsbC54ID0gVFJVRSkgJT4lIFxuICByZW5hbWUoZ3VfYTMgPSBpc29fY29kZSlcblxud29ybGRfdmFyaWFudHNfbWFwIDwtIGxlZnRfam9pbih3b3JsZCwgd29ybGRfdmFyaWFudHMsIGJ5ID0gXCJndV9hM1wiLCBhbGwueCA9IFRSVUUpXG5gYGAifQ== -->

```r
world_variants <- gisaid %>% 
  group_by(Country) %>% 
  mutate(Country = case_when(
  Country == "USA" ~ "United States",
  TRUE ~ as.character(Country)
  )) %>% 
  summarise(most_recent_date = date[n()], 
            prevalent_variant = variant[date == date[n()] & Type == "Variant" & perc_sequences == max(perc_sequences)]) %>% 
            #prevalent_lineage = variant[date == date[n()] & Type == "Lineage" & perc_sequences == max(perc_sequences)]) %>% 
  rename(location = Country)

world_variants <- left_join(world_variants, covid[, c("location", "iso_code")], by = "location", all.x = TRUE) %>% 
  rename(gu_a3 = iso_code)

world_variants_map <- left_join(world, world_variants, by = "gu_a3", all.x = TRUE)
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxucCA8LSBnZ3Bsb3QoZGF0YSA9IHdvcmxkX3ZhcmlhbnRzX21hcCwgYWVzKGZpbGwgPSBwcmV2YWxlbnRfdmFyaWFudCkpICsgXG4gIGdlb21fc2Yoc2hvdy5sZWdlbmQgPSBGQUxTRSkgKyBcbiAgeGxhYihcIkxvbmdpdHVkZVwiKSArIFxuICB5bGFiKFwiTGF0aXR1ZGVcIikgKyBcbiAgdGhlbWUocGFuZWxzLmdyaWQubWFqb3IgPSBlbGVtZW50X2xpbmUoY29sb3IgPSBncmF5KC41KSwgbGluZXR5cGUgPSBcImRhc2hlZFwiLCBzaXplID0gMC41KSwgcGFuZWwuYmFja2dyb3VuZCA9IGVsZW1lbnRfcmVjdChmaWxsID0gXCJhbGljZWJsdWVcIikpIFxuYGBgIn0= -->

```r
p <- ggplot(data = world_variants_map, aes(fill = prevalent_variant)) + 
  geom_sf(show.legend = FALSE) + 
  xlab("Longitude") + 
  ylab("Latitude") + 
  theme(panels.grid.major = element_line(color = gray(.5), linetype = "dashed", size = 0.5), panel.background = element_rect(fill = "aliceblue")) 
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuI3BcbmBgYCJ9 -->

```r
#p
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->




<!-- rnb-text-end -->

