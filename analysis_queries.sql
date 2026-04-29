SELECT COUNT(*) AS total_customers,
       SUM(churned) AS churned_customers,
       ROUND(100.0 * SUM(churned) / COUNT(*), 2) AS churn_rate,
       ROUND(SUM(annual_revenue), 2) AS total_annual_revenue,
       ROUND(SUM(CASE WHEN churned = 1 THEN annual_revenue ELSE 0 END), 2) AS revenue_at_risk
FROM customer_churn;

SELECT plan_type,
       COUNT(*) AS customers,
       ROUND(AVG(monthly_spend), 2) AS avg_monthly_spend,
       ROUND(100.0 * SUM(churned) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY plan_type
ORDER BY churn_rate DESC;

SELECT region,
       COUNT(*) AS customers,
       ROUND(SUM(annual_revenue), 2) AS annual_revenue,
       ROUND(100.0 * SUM(churned) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY region
ORDER BY churn_rate DESC;
