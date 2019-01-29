
# window functions

# moving avg over 4 rows 
# moving average over 4 rows including current one [i.e. last 3 records and current one]
# so for first 3 rows in the result data set , for row 1 - it is avg of only first col , for row 2 - avg of row1 & row 2
# for row 3 - avg of row 1,2,3 and from row 4 - it will have the avg for four rows - row 1,2,3,4 
# for row 5 - avg of row 2,3,4 and row 5

from groceries
select id, revenue, day,
avg(revenue) over (
order by id
rows between 3 preceding and current row
)
as running_avgerage;

# moving average over all the top records including current one, ie,.for row 3 moving_avg woudl be, avg includes  row1,2 and row3
eg 2: for row 10 moving_avg would be, avg includes  row1,2,3,4,5...9 and row10

from groceries
select id, revenue, day,
avg(revenue) over (
order by id
rows between unbounded preceding and current row
)
as running_avgerage;

# sums up the revenue over entire partition
# running sum over a day with out order by id -> sums up the count over entire partition  , 
from groceries
select id, revenue, day,
sum(revenue) over (
partition by day
)
as running_sum;



# running total per day , here we order by id within the partition

from groceries
select id, revenue, day,
sum(id) over (
partition by day
order by id)
as running_total;

# running count over a day , i.e. group by each day and count per day group  wihtin group, here we order by id within the partition
from groceries
select id, revenue, day,
count(id) over (
partition by day
order by id)
as running_count;

Note : if we dont use order by id with in the over function , then the total_count for all the rows will be same 
as the count will not be all" unbounded preceding including current one" i.e for row 3 it is rows 1, 2 and row 3 but it will be "unbounded preceding and 
unbounded following " ie.. for ever row it includes all the rows above it and all rows below it hence the total
coutn will be same for all the rows with in the day partition

# running count over a day with out order by id -> sums up the count over entire partition  , 

from groceries
select id, revenue, day,
count(id) over (
partition by day
)
as running_count;

