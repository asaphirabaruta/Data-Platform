select
    user_id::int                         as user_id,
    first_name                           as first_name,
    last_name                            as last_name,
    lower(sex)                           as sex,
    lower(email)                         as email,
    phone                                as phone,
    date_of_birth::date                 as date_of_birth,
    job_title                            as job_title,
    concat(first_name, ' ', last_name)  as full_name,
    date_part('year', age(date_of_birth))::int as age
from {{ source('raw', 'users') }}
