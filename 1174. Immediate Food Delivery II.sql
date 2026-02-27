# Write your MySQL query statement below
WITH First_Order AS (
    SELECT customer_id, MIN(order_date) AS order_date
    FROM Delivery
    GROUP BY 1
)

SELECT ROUND(AVG(Delivery.order_date = Delivery.customer_pref_delivery_date) * 100, 2) AS immediate_percentage
FROM Delivery
JOIN First_Order ON Delivery.customer_id = First_Order.customer_id AND Delivery.order_date = First_Order.order_date;