





-- DATA validation and Threshold based checks 


-- (1,1,1) : complete data validation is passed
-- if any col val is 0 then failed i,e.. (0,1,1) , (1,0,1) etc
SELECT 
-- we are setting the threshold in this if clause checks 
-- output of IF is 1 then check success 
-- output of IF is 0 then check failed  
IF(success_no_attempt_check > 0.995,1,0),
IF(avg_product_orders_per_category_check > 0.995,1,0),
IF(new_coustmers_count_check > 0.995,1,0)
FROM(
        SELECT 
        a1.success_no_attempt_check AS success_no_attempt_check,
        b1.avg_product_orders_per_category_check AS avg_product_orders_per_category_check ,
        c1.new_coustmers_count_check AS new_coustmers_count_check
        FROM
        (
                (
                    -- check 1 
                    SELECT 
                     -- paymnet session has success but no attempt should be <1%
                     SUM ( CASE WHEN m_payment_event_amt > 0 AND m_payment_attempts = 0 THEN 0 ELSE END )*1.0 
                     / SUM ( CASE WHEN m_payment_submission_successes > 0 THEN 1 ELSE 0 END )  AS success_no_attempt_check


                )a1

                CROSS JOIN

                (
                    -- check 2
                    select tot_orders/dist_prod_cnt as avg_product_orders_per_category_check 
                    (
                     select count (Order_ids) tot_orders from orders 
                    )t1 
                    cross join 
                    (
                    select count (distinct product_id) as dist_prod_cnt from product_info
                    )t2
                )b1

                CROSS JOIN

                (   -- check 3
                    select count(*) as new_coustmers_count_check 
                    from table_i where date = '2022-02-22'
                )c1

        )
)

