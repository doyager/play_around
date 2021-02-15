
-- count( distinct (case when IDFCTN_DTM between current_date() - INTERVAL '30' DAY and current_date() and SYMP.SYMP_TYPE_NM = 'COVID-19' and SYMP.FRST_IDFCTN_IND='Y' then MCID end) ) as

select STE.ST_CD, STE.ST_NM, sum(CAST (0 as INT)) coverage_counts, 
			case when SYMP.SYMP_TYP_NM = 'COVID-19' and SYMP.FRST_IDFCT_IND='Y' then count(DISTINCT MEMBER_ID) else 0 end as  numOfCases,
			count( distinct (case when DTM between current_date() - INTERVAL '30' DAY and current_date() and SYMP.SYMP_TYPE_NM = 'COVID-19' and SYMP.FRST_IDFCTN_IND='Y' then MCID end) ) as numOfCasesThirtyDayCumSum,
			case when IDFC_SRC_NAME='LAB' then count(DISTINCT MEMBER_ID) else 0 end as labsProcessed,
			SYMP.CONTY_FIPS_CD as flipsCD,
			SYMP.CONTY_NM as countyName,
			count(distinct case when SRLGY_IND='Y' then MEMBER_ID end) as srglyCounts,
			count( distinct (case when IDFCTN_DTM between current_date() - INTERVAL '30' DAY and current_date() and SRLGY_IND='Y' then MCID end) ) as srglyCountsThirtyDayCumSum,
			CAST(0 AS int) as  TOTL_ADMTS_CNT,
			CAST(0 AS int) as admtCountsThirtyDayCumSum
			from Schema1.fact_mbr_symp SYMP
			inner join  Schema1.dim_st STE 
			on SYMP.ST_CD=STE.ST_CD 
			where acct_id = 'abc'   
			group by 
			STE.ST_CD , STE.ST_NAME,
			SYMP_TYPE_NAME,IDFCTN_SRC_NAME, 
			SYMP.CONTY_FIPS_CD,SYMP.CONTY_NM,SYMP.FRST_IDFCTN_IND
