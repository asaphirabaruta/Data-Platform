select
    sex,
    job_title,
    count(*)                    as user_count,
    avg(age)                    as avg_age,
    min(age)                    as youngest_age,
    max(age)                    as oldest_age
from {{ ref('stg_users') }}
group by sex, job_title
order by user_count desc
